# Detect simple positive, negative, and neutral sentiment.
# This gives each review a basic sentiment label.

import re


POSITIVE_WORDS = {
    "good",
    "great",
    "better",
    "helped",
    "helpful",
    "effective",
    "excellent",
    "amazing",
    "happy",
    "improved",
    "love",
    "relief",
}


NEGATIVE_WORDS = {
    "bad",
    "worse",
    "pain",
    "nausea",
    "headache",
    "dizziness",
    "fatigue",
    "vomiting",
    "terrible",
    "awful",
    "failed",
    "useless",
    "hate",
}


def analyze_sentiment(text):
    """Return a basic sentiment label and score."""

    if not isinstance(text, str) or not text.strip():
        return {
            "label": "neutral",
            "score": 0,
        }

    words = re.findall(r"\b[\w'-]+\b", text.lower())

    positive_count = sum(word in POSITIVE_WORDS for word in words)
    negative_count = sum(word in NEGATIVE_WORDS for word in words)

    score = positive_count - negative_count

    if score > 0:
        label = "positive"
    elif score < 0:
        label = "negative"
    else:
        label = "neutral"

    return {
        "label": label,
        "score": score,
    }


if __name__ == "__main__":
    reviews = [
        "This medicine helped me and I feel better.",
        "I had terrible nausea and headache.",
        "I started this medicine yesterday.",
    ]

    for review in reviews:
        print(analyze_sentiment(review))