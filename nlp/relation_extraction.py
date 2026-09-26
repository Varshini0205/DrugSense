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


RELATION_PATTERNS = [
    ("caused", r"\bcaused\b"),
    ("caused", r"\bcauses\b"),
    ("caused", r"\bcausing\b"),
    ("caused", r"\bgave me\b"),
    ("caused", r"\bresulted in\b"),
    ("helped", r"\bhelped\b"),
    ("helped", r"\bimproved\b"),
    ("helped", r"\btreated\b"),
    ("helped", r"\brelieved\b"),
]


def _find_terms(text, terms):
    found = []

    for term in terms:
        for match in re.finditer(
            rf"\b{re.escape(term)}\b",
            text,
            flags=re.IGNORECASE,
        ):
            found.append(
                {
                    "term": term.lower(),
                    "start": match.start(),
                    "end": match.end(),
                }
            )

    return sorted(found, key=lambda item: item["start"])


def extract_relations(text, entities=None):
    """
    Extract simple drug-to-medical-term relations.

    The entities argument is optional to preserve compatibility
    with the original function and existing tests.
    """

    if not isinstance(text, str) or not text.strip():
        return []

    if entities is None:
        entities = {
            "drugs": DRUGS,
            "conditions": CONDITIONS,
            "symptoms": SYMPTOMS,
        }

    drugs = entities.get("drugs", [])
    conditions = entities.get("conditions", [])
    symptoms = entities.get("symptoms", [])

    drug_terms = _find_terms(text, drugs)

    medical_terms = _find_terms(
        text,
        conditions + symptoms,
    )

    if not drug_terms or not medical_terms:
        return []

    relations = []

    sentences = list(
        re.finditer(
            r"[^.!?]+(?:[.!?]|$)",
            text,
        )
    )

    for sentence_match in sentences:

        sentence_start = sentence_match.start()
        sentence_end = sentence_match.end()

        sentence_drugs = [
            drug
            for drug in drug_terms
            if sentence_start <= drug["start"] < sentence_end
        ]

        sentence_medical = [
            term
            for term in medical_terms
            if sentence_start <= term["start"] < sentence_end
        ]

        if not sentence_drugs or not sentence_medical:
            continue

        sentence_text = text[
            sentence_start:sentence_end
        ]

        for relation_name, pattern in RELATION_PATTERNS:

            for relation_match in re.finditer(
                pattern,
                sentence_text,
                flags=re.IGNORECASE,
            ):

                relation_start = (
                    sentence_start +
                    relation_match.start()
                )

                relation_end = (
                    sentence_start +
                    relation_match.end()
                )

                previous_drugs = [
                    drug
                    for drug in sentence_drugs
                    if drug["end"] <= relation_start
                ]

                following_terms = [
                    term
                    for term in sentence_medical
                    if term["start"] >= relation_end
                ]

                if not previous_drugs:
                    continue

                if not following_terms:
                    continue

                subject = min(
                    previous_drugs,
                    key=lambda drug:
                    relation_start - drug["end"],
                )

                object_term = min(
                    following_terms,
                    key=lambda term:
                    term["start"] - relation_end,
                )

                distance = (
                    object_term["start"] -
                    relation_end
                )

                if distance > 45:
                    continue

                relation = {
                    "subject": subject["term"],
                    "relation": relation_name,
                    "object": object_term["term"],
                }

                if relation not in relations:
                    relations.append(relation)

    return relations


if __name__ == "__main__":

    sample = (
        "Metformin helped my diabetes "
        "but caused severe nausea and dizziness."
    )

    print(
        extract_relations(sample)
    )
