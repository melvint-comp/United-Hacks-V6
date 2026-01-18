from typing import List

EMPATHY_KEYWORDS = [
    "sorry", "understand", "feel", "that must be", "i get why",
    "makes sense", "thank you for sharing"
]

def analyze_empathy(messages: List[dict]) -> dict:
    count = 0

    for msg in messages:
        text = msg["text"].lower()
        if any(keyword in text for keyword in EMPATHY_KEYWORDS):
            count += 1

    score = count / len(messages) if messages else 0

    return {
        "empathy_signals_detected": count,
        "empathy_score": round(score, 2)
    }
