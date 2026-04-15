DOMAINS = [
    {"key": "demand",         "label": "Demand Planning & Forecasting"},
    {"key": "procurement",    "label": "Procurement & Sourcing"},
    {"key": "manufacturing",  "label": "Manufacturing & Production"},
    {"key": "inventory",      "label": "Inventory Management"},
    {"key": "logistics",      "label": "Logistics & Transportation"},
    {"key": "warehousing",    "label": "Warehousing & Fulfillment"},
    {"key": "risk",           "label": "Risk & Resilience"},
    {"key": "sustainability", "label": "Sustainability & ESG"},
]

SYSTEM_PROMPT_BASE = """
You are a world-class supply chain analyst with expertise in SCOR methodology,
Gartner supply chain benchmarks, lean manufacturing, and agile supply chain frameworks.
Assess organizational supply chain health across 8 domains and produce structured reports.

ALWAYS return a raw JSON block first (no markdown fences), then the narrative:
{"scores":{"demand":0-100,"procurement":0-100,"manufacturing":0-100,"inventory":0-100,"logistics":0-100,"warehousing":0-100,"risk":0-100,"sustainability":0-100},"overall":0-100}

Then write these sections:
EXECUTIVE SUMMARY
TOP RISKS
DOMAIN HIGHLIGHTS
PRIORITY RECOMMENDATIONS

Be specific and cite industry benchmarks where relevant.
"""

def build_system_prompt(vertical: str = "general") -> str:
    from verticals import VERTICAL_PRESETS
    modifier = VERTICAL_PRESETS.get(vertical, "General manufacturing/industry context.")
    return SYSTEM_PROMPT_BASE + f"\n\nIndustry vertical context: {modifier}"
