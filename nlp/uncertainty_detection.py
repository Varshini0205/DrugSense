# Find words and phrases that show uncertainty.
# This helps separate certain statements from possible ones.

import re


UNCERTAINTY_PATTERNS = [
    r"\bmaybe\b",
    r"\bpossibly\b",
    r"\bmight\b",
    r"\bmay\b",
    r"\bcould\b",
    r"\bperhaps\b",
    r"\bi think\b",
    r"\bnot sure\b",
    r"\bseems like\b",
    r"\bappears to\b",
]


def detect_uncertainty(text):
    """Find uncertainty phrases in the review."""

    if not isinstance(text, str):
        return []

    results = []

    for pattern in UNCERTAINTY_PATTERNS:
        for match in re.finditer(pattern, text, re.IGNORECASE):
            results.append(
                {
                    "text": match.group(0),
                    "start": match.start(),
                    "end": match.end(),
                }
            )

    results.sort(key=lambda item: item["start"])

    return results


if __name__ == "__main__":
    review = (
        "Maybe this medicine caused my headache. "
        "I think it might be helping."
    )

    print(detect_uncertainty(review))