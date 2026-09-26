# Find changes in symptoms or conditions.
# This records whether something improved or became worse.

import re


CHANGE_PATTERNS = {
    "improved": [
        "getting better",
        "less pain",
        "improved",
        "better",
        "decreased",
        "reduced",
    ],
    "worsened": [
        "became worse",
        "getting worse",
        "more severe",
        "worsened",
        "worse",
        "increased",
    ],
    "unchanged": [
        "no change",
        "unchanged",
        "the same",
        "still the same",
    ],
}


def extract_comparative_changes(text):
    """Find words that describe a change."""

    if not isinstance(text, str) or not text.strip():
        return []

    results = []

    for change_type, phrases in CHANGE_PATTERNS.items():
        for phrase in phrases:
            pattern = r"\b" + re.escape(phrase) + r"\b"

            for match in re.finditer(
                pattern,
                text,
                re.IGNORECASE,
            ):
                results.append(
                    {
                        "expression": match.group(),
                        "change": change_type,
                        "start": match.start(),
                        "end": match.end(),
                    }
                )

    results.sort(
        key=lambda item: (
            item["start"],
            -(item["end"] - item["start"]),
        )
    )

    filtered_results = []

    for result in results:
        overlaps = False

        for existing in filtered_results:
            if (
                result["start"] < existing["end"]
                and result["end"] > existing["start"]
            ):
                overlaps = True
                break

        if not overlaps:
            filtered_results.append(result)

    return filtered_results


if __name__ == "__main__":
    review = (
        "My acne improved but my headaches became worse."
    )

    print(extract_comparative_changes(review))
