# Find words that show how strong a symptom is.
# Longer severity phrases are kept instead of overlapping shorter ones.

import re


SEVERITY_LEVELS = {
    "very severe": "very severe",
    "mild": "mild",
    "slight": "mild",
    "minor": "mild",
    "moderate": "moderate",
    "medium": "moderate",
    "severe": "severe",
    "serious": "severe",
    "extreme": "severe",
}


def detect_severity(text):
    """Find severity words and phrases without overlap."""

    if not isinstance(text, str):
        return []

    results = []

    for phrase, level in sorted(
        SEVERITY_LEVELS.items(),
        key=lambda item: len(item[0]),
        reverse=True,
    ):
        pattern = r"\b" + re.escape(phrase) + r"\b"

        for match in re.finditer(pattern, text, re.IGNORECASE):
            start, end = match.span()

            overlaps = any(
                start < item["end"] and end > item["start"]
                for item in results
            )

            if not overlaps:
                results.append(
                    {
                        "text": match.group(0),
                        "severity": level,
                        "start": start,
                        "end": end,
                    }
                )

    results.sort(key=lambda item: item["start"])

    return results


if __name__ == "__main__":
    review = (
        "I had mild nausea and moderate pain. "
        "Later, I experienced very severe headache."
    )

    print(detect_severity(review))