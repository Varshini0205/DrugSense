# Find who experienced a symptom.
# This separates the patient from another person.

import re


OTHER_PERSON_PATTERNS = [
    "my husband",
    "my wife",
    "my mother",
    "my father",
    "my son",
    "my daughter",
    "my child",
    "my brother",
    "my sister",
    "my friend",
]


def detect_experiencer(text):
    """Find whether the experience belongs to the patient or someone else."""

    if not isinstance(text, str) or not text.strip():
        return []

    results = []

    for phrase in OTHER_PERSON_PATTERNS:
        pattern = r"\b" + re.escape(phrase) + r"\b"

        for match in re.finditer(
            pattern,
            text,
            re.IGNORECASE,
        ):
            results.append(
                {
                    "experiencer": "other person",
                    "person": match.group(),
                    "start": match.start(),
                    "end": match.end(),
                }
            )

    if results:
        return results

    patient_patterns = [
        r"\bi\b",
        r"\bme\b",
        r"\bmy\b",
        r"\bi had\b",
        r"\bi experienced\b",
    ]

    for pattern in patient_patterns:
        match = re.search(
            pattern,
            text,
            re.IGNORECASE,
        )

        if match:
            results.append(
                {
                    "experiencer": "patient",
                    "person": match.group(),
                    "start": match.start(),
                    "end": match.end(),
                }
            )
            break

    return results


if __name__ == "__main__":
    print(detect_experiencer("I had headaches."))
    print(detect_experiencer("My husband had headaches."))
