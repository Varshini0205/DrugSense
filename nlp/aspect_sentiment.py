# Find sentiment connected to a specific medical term.
# This keeps positive and negative feelings linked to the right topic.

import re

from nlp.entity_extraction import extract_entities


POSITIVE_WORDS = [
    "good",
    "great",
    "better",
    "improved",
    "helped",
    "effective",
    "happy",
    "excellent",
]

NEGATIVE_WORDS = [
    "bad",
    "worse",
    "terrible",
    "painful",
    "awful",
    "failed",
    "horrible",
    "severe",
]


def extract_aspect_sentiment(text):
    """Find sentiment near medical entities."""

    if not isinstance(text, str) or not text.strip():
        return []

    entities = extract_entities(text)

    aspects = (
        entities["drugs"]
        + entities["conditions"]
        + entities["symptoms"]
    )

    results = []

    for aspect in aspects:
        pattern = r"\b" + re.escape(aspect) + r"\b"

        for match in re.finditer(
            pattern,
            text,
            re.IGNORECASE,
        ):
            start = max(0, match.start() - 60)
            end = min(len(text), match.end() + 60)

            nearby_text = text[start:end].lower()

            positive_found = any(
                re.search(
                    r"\b" + re.escape(word) + r"\b",
                    nearby_text,
                )
                for word in POSITIVE_WORDS
            )

            negative_found = any(
                re.search(
                    r"\b" + re.escape(word) + r"\b",
                    nearby_text,
                )
                for word in NEGATIVE_WORDS
            )

            if positive_found and not negative_found:
                sentiment = "positive"
            elif negative_found and not positive_found:
                sentiment = "negative"
            elif positive_found and negative_found:
                sentiment = "mixed"
            else:
                sentiment = "neutral"

            results.append(
                {
                    "aspect": aspect,
                    "sentiment": sentiment,
                }
            )

    unique_results = []

    for result in results:
        if result not in unique_results:
            unique_results.append(result)

    return unique_results


if __name__ == "__main__":
    review = (
        "My acne improved, but I had terrible headaches."
    )

    print(extract_aspect_sentiment(review))
