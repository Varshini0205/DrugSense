# Normalize common medical words.
# This keeps different forms under one simple name.

import re


NORMALIZATION_MAP = {
    "headaches": "headache",
    "head pain": "headache",
    "head pains": "headache",
    "nausea": "nausea",
    "depressed": "depression",
    "depressive": "depression",
    "dizzy": "dizziness",
    "dizziness": "dizziness",
    "vomiting": "vomiting",
    "vomit": "vomiting",
}


def normalize_entity(text):
    """Return a simple normalized medical term."""

    if not isinstance(text, str):
        return text

    value = text.strip().lower()

    if not value:
        return value

    if value in NORMALIZATION_MAP:
        return NORMALIZATION_MAP[value]

    return value


def normalize_entities(entities):
    """Normalize a list of medical terms."""

    if not isinstance(entities, list):
        return []

    results = []

    for entity in entities:
        normalized = normalize_entity(entity)

        if normalized and normalized not in results:
            results.append(normalized)

    return results


if __name__ == "__main__":
    print(normalize_entity("headaches"))
    print(normalize_entity("head pain"))
    print(normalize_entity("depressed"))
