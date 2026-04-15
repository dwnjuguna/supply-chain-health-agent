from agent import SupplyChainHealthAgent
from scoring import interpret_score, print_score_bar
from domains import DOMAINS
from verticals import VERTICAL_PRESETS

def main():
    print("\n" + "="*55)
    print("   SUPPLY CHAIN HEALTH AGENT")
    print("   Powered by Anthropic Claude SDK")
    print("="*55 + "\n")

    verticals = list(VERTICAL_PRESETS.keys())
    print("Available industry verticals:")
    for i, v in enumerate(verticals, 1):
        print(f"  {i}. {v}")
    v_input = input("\nChoose vertical (name or number, default=general): ").strip().lower()
    if v_input.isdigit() and 1 <= int(v_input) <= len(verticals):
        vertical = verticals[int(v_input) - 1]
    elif v_input in VERTICAL_PRESETS:
        vertical = v_input
    else:
        vertical = "general"
    print(f"\nVertical selected: {vertical.upper()}")

    print("\nAssessment modes:")
    print("  g = General (industry benchmark baseline, no inputs needed)")
    print("  c = Custom  (you describe your organization's current state)")
    mode = input("\nChoose mode [g/c]: ").strip().lower()

    agent = SupplyChainHealthAgent(vertical=vertical)

    if mode == "c":
        print("\nDescribe your supply chain for each domain.")
        print("Press Enter to skip a domain.\n")
        inputs = {}
        for d in DOMAINS:
            val = input(f"  {d['label']}: ").strip()
            if val:
                inputs[d['label']] = val
        if not inputs:
            print("No inputs provided — switching to general assessment.\n")
            result = agent.run_general_assessment()
        else:
            print("\nRunning custom assessment...\n")
            result = agent.run_custom_assessment(inputs)
    else:
        print("\nRunning general assessment against industry benchmarks...\n")
        result = agent.run_general_assessment()

    # Print scores
    scores_data = result.get("scores") or {}
    domain_scores = scores_data.get("scores", {})
    overall = scores_data.get("overall", "N/A")

    print("="*55)
    print("  DOMAIN HEALTH SCORES")
    print("="*55)
    for domain, score in domain_scores.items():
        print_score_bar(domain.capitalize(), score)
    print(f"\n  {'OVERALL SCORE':<18} {'':>22} {overall}/100")
    print("="*55)

    # Print narrative
    print("\n" + result["narrative"])
    print("\n" + "="*55)

    # Follow-up loop
    print("\nYou can now ask follow-up questions about your results.")
    print("Type 'exit' to quit.\n")
    while True:
        q = input("Your question: ").strip()
        if not q or q.lower() in ("exit", "quit", "q"):
            print("\nThank you for using the Supply Chain Health Agent. Goodbye!\n")
            break
        print("\n" + agent.ask_followup(q) + "\n")

if __name__ == "__main__":
    main()
