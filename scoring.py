import json
import re

def parse_scores(text: str):
    """Extract the JSON scores block from Claude response."""
    match = re.search(r'\{[\s\S]*?"overall"[\s\S]*?\}', text)
    if not match:
        return None
    try:
        return json.loads(match.group(0))
    except json.JSONDecodeError:
        return None

def interpret_score(score: int) -> tuple:
    """Return (rating_label, description) for a 0-100 score."""
    if score >= 80:
        return "Excellent", "World-class — sustain and innovate"
    elif score >= 60:
        return "Good", "Above average — targeted improvements needed"
    elif score >= 40:
        return "Fair", "Moderate gaps — structured improvement required"
    else:
        return "At Risk", "Significant underperformance — immediate action needed"

def print_score_bar(domain: str, score: int):
    """Print a visual ASCII score bar to the terminal."""
    filled = score // 5
    bar = "█" * filled + "░" * (20 - filled)
    rating, _ = interpret_score(score)
    print(f"  {domain:<18} [{bar}] {score:>3}/100  {rating}")
