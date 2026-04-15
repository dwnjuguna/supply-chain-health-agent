# 🤖 Supply Chain Health Agent

> An AI-powered supply chain diagnostic tool built on the **Anthropic Claude SDK** — assess the end-to-end health of any organization's supply chain across 8 critical domains in seconds.

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![Anthropic Claude](https://img.shields.io/badge/powered%20by-Anthropic%20Claude-purple.svg)](https://www.anthropic.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 🌟 What It Does

The Supply Chain Health Agent uses Claude AI to evaluate your supply chain across **8 SCOR-aligned domains**, benchmark your performance against world-class standards, and deliver prioritized, actionable recommendations — in under 60 seconds.

```
=======================================================
   SUPPLY CHAIN HEALTH AGENT
   Powered by Anthropic Claude SDK
=======================================================

  Demand             [██████████████░░░░░░]  72/100  Good
  Procurement        [█████████████░░░░░░░]  65/100  Good
  Manufacturing      [███████████████░░░░░]  78/100  Good
  Inventory          [█████████████░░░░░░░]  68/100  Good
  Logistics          [██████████████░░░░░░]  71/100  Good
  Warehousing        [██████████████░░░░░░]  74/100  Good
  Risk               [███████████░░░░░░░░░]  58/100  Fair
  Sustainability     [████████████░░░░░░░░]  63/100  Good

  OVERALL SCORE                             69/100
=======================================================
```

---

## 🏭 Industry Verticals Supported

| Vertical | Focus Areas | Benchmark Orgs |
|---|---|---|
| **Semiconductor** | Fab utilization, die yield, export controls, rare earth risk | TSMC, Intel, NVIDIA, ASML |
| **Automotive** | JIT/JIS delivery, zero line stoppages, EV transition | Toyota (TPS), BMW, Tesla |
| **Pharmaceutical** | Cold chain, GDP compliance, DSCSA serialization | Pfizer, Roche, J&J |
| **Retail & E-commerce** | OTIF, last-mile, omnichannel, seasonal peaks | Amazon, Walmart, Zara |
| **CPG** | Case fill rate, trade promotion, retailer compliance | P&G, Unilever, Nestlé |
| **Aerospace** | AS9100 compliance, long-lead parts, MRO, export (ITAR) | Boeing, Airbus, Lockheed |
| **Healthcare** | UDI traceability, sterile supply, GPO compliance | Medtronic, Stryker, BD |
| **General** | Standard SCOR + Gartner benchmarks across all domains | — |

---

## 📊 8 Health Domains Assessed

| Domain | SCOR Process | Key KPIs |
|---|---|---|
| Demand Planning | Plan | Forecast accuracy, bias, S&OP maturity |
| Procurement | Source | Supplier OTD, spend under management |
| Manufacturing | Make | OEE, first-pass yield, cycle time |
| Inventory | Plan/Deliver | Turns, stockout rate, E&O % |
| Logistics | Deliver | OTIF, freight cost % of revenue |
| Warehousing | Deliver | Order accuracy, utilization, lines/hour |
| Risk & Resilience | Enable | BCP coverage, TTR, supplier risk tiers |
| Sustainability | Enable | Scope 3 tracking, ESG audit coverage |

---

## 🚀 Quick Start

### 1. Clone the repo
```bash
git clone https://github.com/dwnjuguna/supply-chain-health-agent.git
cd supply-chain-health-agent
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set your API key
```bash
echo "ANTHROPIC_API_KEY=your-key-here" > .env
```
Get your API key at [console.anthropic.com](https://console.anthropic.com)

### 4. Run the agent
```bash
python3 cli.py
```

### 5. (Optional) Run the web UI
```bash
pip install streamlit
streamlit run app.py
```

---

## 🎯 Assessment Modes

**General Mode** — No inputs needed. Claude benchmarks a typical organization in your chosen vertical against Gartner and SCOR world-class standards. Great for quick overviews and executive briefings.

**Custom Mode** — Describe your organization's current state for each domain (metrics, tools, challenges). Claude benchmarks your specific situation and tailors every recommendation to your context.

---

## 💬 Follow-up Q&A

After every assessment, the agent enters interactive Q&A mode powered by full conversation history:

```
Your question: What should be our top priority in the first 90 days?
Your question: How do we compare to TSMC on manufacturing?
Your question: Give me a board-level summary in 3 bullet points
```

---

## 📁 Project Structure

```
supply-chain-health-agent/
├── agent.py          # Core agent logic & Claude API calls
├── domains.py        # Domain definitions & system prompt
├── verticals.py      # Industry vertical presets
├── scoring.py        # Score parsing & interpretation
├── cli.py            # Interactive command-line interface
├── app.py            # Streamlit web UI
├── requirements.txt  # Dependencies
└── .env              # API key (gitignored — never committed)
```

---

## 🔧 Extending the Agent

### Add a new industry vertical
Open `verticals.py` and add a new entry to `VERTICAL_PRESETS`:
```python
"your_vertical": (
    "Your vertical context. Key benchmarks, regulatory requirements, "
    "elevated risk domains, and benchmark companies."
),
```

### Add a new domain
1. Add the domain to `DOMAINS` list in `domains.py`
2. Update the JSON schema in `SYSTEM_PROMPT_BASE`
3. Document the new domain in this README

---

## 🏗️ Architecture

```
User Input
    │
    ▼
CLI / Streamlit UI
    │
    ▼
Prompt Builder (domains.py + verticals.py)
    │
    ▼
Anthropic Claude API (claude-sonnet-4)
    │
    ▼
Score Parser + Narrative Extractor (scoring.py)
    │
    ▼
Scored Report + Follow-up Q&A Loop
```

---

## 📚 Frameworks Referenced

- [SCOR Model](https://www.ascm.org/learning-development/scor/) — Supply Chain Operations Reference
- [Gartner Supply Chain Top 25](https://www.gartner.com/en/supply-chain) — World-class benchmarks
- [Anthropic Claude SDK](https://docs.anthropic.com) — AI backbone
- [ISO 28000](https://www.iso.org/standard/79612.html) — Supply chain security
- [GRI Standards](https://www.globalreporting.org) — ESG reporting

---

## 🤝 Contributing

Contributions welcome! To contribute:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-vertical`)
3. Commit your changes (`git commit -m 'feat: add aerospace vertical'`)
4. Push to the branch (`git push origin feature/new-vertical`)
5. Open a Pull Request

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

## 👤 Author

**David Njuguna**
- GitHub: [@dwnjuguna](https://github.com/dwnjuguna)

---

*Built with ❤️ using the Anthropic Claude SDK*
