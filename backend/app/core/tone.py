
from typing import List
from textblob import TextBlob

def analyze_tone(messages: List[dict]) -> dict:
    sentiments = []

    for msg in messages:
        blob = TextBlob(msg["text"])
        sentiments.append(blob.sentiment.polarity)

    avg = sum(sentiments) / len(sentiments) if sentiments else 0

    if avg > 0.2:
        label = "Positive"
    elif avg < -0.2:
        label = "Negative"
    else:
        label = "Neutral"

    return {
        "average_polarity": round(avg, 3),
        "label": label
    }
