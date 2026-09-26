# Find time-related phrases in a review.
# These phrases help show when something happened.

import re


TEMPORAL_PATTERNS = [
    r"\byesterday\b",
    r"\btoday\b",
    r"\btomorrow\b",
    r"\blast\s+(?:day|week|month|year)\b",
    r"\bthis\s+(?:day|week|month|year)\b",
    r"\bnext\s+(?:day|week|month|year)\b",
    r"\b\d+\s+(?:minutes?|hours?|days?|weeks?|months?|years?)\s+ago\b",
    r"\b(?:one|two|three|four|five|six|seven|eight|nine|ten)\s+"
    r"(?:minutes?|hours?|days?|weeks?|months?|years?)\s+ago\b",
    r"\bsince\s+(?:yesterday|last\s+week|last\s+month|last\s+year)\b",
    r"\bafter\s+starting\s+(?:the\s+)?medicine\b",
    r"\bbefore\s+starting\s+(?:the\s+)?medicine\b",
]


def extract_temporal_information(text):
    """Find time-related phrases."""

    if not isinstance(text, str):
        return []

    results = []

    for pattern in TEMPORAL_PATTERNS:
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
        "I started this medicine two weeks ago. "
        "I felt better after starting the medicine. "
        "The headache started yesterday."
    )

    print(extract_temporal_information(review))