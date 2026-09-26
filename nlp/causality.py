# Find words that show one thing caused another.
# This keeps simple cause-and-effect information.

import re


CAUSAL_PATTERNS = [
    "caused",
    "causes",
    "causing",
    "led to",
    "resulted in",
    "gave me",
    "made me",
    "triggered",
    "because of",
    "due to",
    "developed after",
]


def extract_causality(text):
    """Find causal expressions in the text."""

    if not isinstance(text, str):
        return []

    results = []

    for phrase in CAUSAL_PATTERNS:
        pattern = r"\b" + re.escape(phrase) + r"\b"

        for match in re.finditer(
            pattern,
            text,
            re.IGNORECASE,
        ):
            results.append(
                {
                    "expression": match.group(),
                    "start": match.start(),
                    "end": match.end(),
                }
            )

    results.sort(key=lambda item: item["start"])

    return results


if __name__ == "__main__":
    review = (
        "The medication caused nausea and led to dizziness."
    )

    print(extract_causality(review))