# Find treatment results and check if they are negative.
# This helps separate "helped" from "did not help".

import re


RESPONSE_PATTERNS = {
    "improved": [
        r"\bhelped\b",
        r"\bimproved\b",
        r"\bworked\b",
        r"\bbetter\b",
        r"\brelief\b",
    ],
    "worsened": [
        r"\bmade .* worse\b",
        r"\bgot worse\b",
        r"\bworsened\b",
        r"\bworse\b",
    ],
    "no_effect": [
        r"\bdid not help\b",
        r"\bdidn't help\b",
        r"\bno improvement\b",
        r"\bnot effective\b",
        r"\bdid not work\b",
        r"\bdidn't work\b",
        r"\bnot better\b",
        r"\bdid not improve\b",
        r"\bdidn't improve\b",
    ],
}


NEGATION_WORDS = {
    "no",
    "not",
    "never",
    "didn't",
    "did",
    "without",
}


def is_negated(text, start):
    """Check whether a response phrase is preceded by negation."""

    before = text[:start].lower()

    words = re.findall(r"\b[\w']+\b", before)

    if not words:
        return False

    recent_words = words[-3:]

    return any(word in NEGATION_WORDS for word in recent_words)


def detect_treatment_response(text):
    """Find treatment responses and handle negation."""

    if not isinstance(text, str):
        return []

    results = []

    for response, patterns in RESPONSE_PATTERNS.items():
        for pattern in patterns:
            for match in re.finditer(pattern, text, re.IGNORECASE):
                start, end = match.span()

                overlaps = any(
                    start < item["end"] and end > item["start"]
                    for item in results
                )

                if overlaps:
                    continue

                detected_response = response

                if response == "improved" and is_negated(text, start):
                    detected_response = "no_effect"

                results.append(
                    {
                        "text": match.group(0),
                        "response": detected_response,
                        "start": start,
                        "end": end,
                    }
                )

    results.sort(key=lambda item: item["start"])

    return results


if __name__ == "__main__":
    reviews = [
        "The medicine helped my pain.",
        "The medicine did not help my pain.",
        "The medicine improved my symptoms.",
        "The medicine did not improve my symptoms.",
    ]

    for review in reviews:
        print(detect_treatment_response(review))