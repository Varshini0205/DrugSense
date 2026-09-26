# Find important events in a patient review.
# This records things like starting medicine or developing symptoms.

import re


EVENT_PATTERNS = {
    "MEDICATION_START": [
        "started taking",
        "started the medication",
        "began taking",
        "started using",
    ],
    "MEDICATION_STOP": [
        "stopped taking",
        "stopped the medication",
        "discontinued",
        "quit taking",
    ],
    "SYMPTOM_DEVELOPED": [
        "developed",
        "started having",
        "experienced",
        "got",
    ],
    "TREATMENT_CHANGE": [
        "increased the dose",
        "decreased the dose",
        "changed the dose",
        "switched medication",
    ],
    "IMPROVEMENT": [
        "improved",
        "got better",
        "feeling better",
    ],
    "WORSENING": [
        "got worse",
        "became worse",
        "worsened",
    ],
}


def extract_events(text):
    """Find important events in the review."""

    if not isinstance(text, str) or not text.strip():
        return []

    results = []

    for event_type, phrases in EVENT_PATTERNS.items():
        for phrase in phrases:
            pattern = r"\b" + re.escape(phrase) + r"\b"

            for match in re.finditer(
                pattern,
                text,
                re.IGNORECASE,
            ):
                results.append(
                    {
                        "event": event_type,
                        "expression": match.group(),
                        "start": match.start(),
                        "end": match.end(),
                    }
                )

    results.sort(key=lambda item: item["start"])

    filtered_results = []

    for result in results:
        overlaps = False

        for existing in filtered_results:
            if (
                result["start"] < existing["end"]
                and result["end"] > existing["start"]
            ):
                current_length = result["end"] - result["start"]
                existing_length = (
                    existing["end"] - existing["start"]
                )

                if current_length <= existing_length:
                    overlaps = True
                else:
                    filtered_results.remove(existing)

                break

        if not overlaps:
            filtered_results.append(result)

    return filtered_results


if __name__ == "__main__":
    review = (
        "I started taking the medication. "
        "Three days later I developed nausea."
    )

    print(extract_events(review))
