from typing import List
from collections import Counter

def analyze_balance(messages: List[dict]) -> dict:
    speakers = [msg["sender"] for msg in messages]
    counts = Counter(speakers)

    total = sum(counts.values())
    proportions = {
        speaker: round(count / total, 2)
        for speaker, count in counts.items()
    }

    return {
        "message_count": dict(counts),
        "participation_ratio": proportions
    }
