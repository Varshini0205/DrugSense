# Find simple negative statements in a review.
# This helps separate symptoms from symptoms that are not present.

import re


NEGATION_PATTERNS = [
    r"\bno\s+([a-zA-Z][a-zA-Z\s-]*?)(?=[,.!?]|$)",
    r"\bwithout\s+([a-zA-Z][a-zA-Z\s-]*?)(?=[,.!?]|$)",
    r"\bnever\s+([a-zA-Z][a-zA-Z\s-]*?)(?=[,.!?]|$)",
    r"\bdid\s+not\s+([a-zA-Z][a-zA-Z\s-]*?)(?=[,.!?]|$)",
    r"\bdoes\s+not\s+([a-zA-Z][a-zA-Z\s-]*?)(?=[,.!?]|$)",
    r"\bdo\s+not\s+([a-zA-Z][a-zA-Z\s-]*?)(?=[,.!?]|$)",
]


def detect_negations(text):
    """Find phrases that appear after common negative words."""

    if not isinstance(text, str):
        return []

    results = []

    for pattern in NEGATION_PATTERNS:
        matches = re.finditer(pattern, text, re.IGNORECASE)

        for match in matches:
            phrase = match.group(1).strip()

            if phrase:
                results.append(
                    {
                        "text": phrase,
                        "start": match.start(1),
                        "end": match.end(1),
                    }
                )

    results.sort(key=lambda item: item["start"])

    return results


if __name__ == "__main__":
    review = (
        "I have no nausea. "
        "I am without headache. "
        "The medicine did not help."
    )

    print(detect_negations(review))