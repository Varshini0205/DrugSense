# Find drug, condition, and symptom names.
# Longer medical terms are kept instead of overlapping shorter terms.

import re


DRUGS = [
    "ibuprofen",
    "aspirin",
    "paracetamol",
    "metformin",
    "amoxicillin",
    "sertraline",
    "fluoxetine",
]


CONDITIONS = [
    "depression",
    "anxiety",
    "diabetes",
    "acne",
    "migraine",
    "hypertension",
    "bipolar disorder",
    "high blood pressure",
    "major depressive disorder",
]


SYMPTOMS = [
    "nausea",
    "headache",
    "dizziness",
    "pain",
    "fatigue",
    "vomiting",
    "insomnia",
    "chest pain",
]


def find_entities(text, terms):
    """Find medical terms without overlapping matches."""

    if not isinstance(text, str):
        return []

    matches = []

    for term in sorted(terms, key=len, reverse=True):
        pattern = r"\b" + re.escape(term) + r"\b"

        for match in re.finditer(pattern, text, re.IGNORECASE):
            start, end = match.span()

            overlaps = any(
                start < existing_end and end > existing_start
                for existing_start, existing_end, _ in matches
            )

            if not overlaps:
                matches.append((start, end, term))

    matches.sort(key=lambda item: item[0])

    return [term for _, _, term in matches]


def extract_entities(text):
    """Find drugs, conditions, and symptoms."""

    return {
        "drugs": find_entities(text, DRUGS),
        "conditions": find_entities(text, CONDITIONS),
        "symptoms": find_entities(text, SYMPTOMS),
    }


if __name__ == "__main__":
    review = (
        "I take metformin for high blood pressure. "
        "I also have major depressive disorder and chest pain."
    )

    print(extract_entities(review))