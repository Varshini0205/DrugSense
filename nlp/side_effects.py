# Find symptoms that may be side effects.
# A symptom needs medicine-related evidence before being marked.

import re

from nlp.entity_extraction import extract_entities
from nlp.negation_detection import detect_negations
from nlp.causality import extract_causality


SIDE_EFFECT_CUES = [
    "after taking",
    "while taking",
    "caused",
    "gave me",
    "developed after",
    "made me",
]


def extract_side_effects(text):
    """Find symptoms that have side-effect evidence."""

    if not isinstance(text, str) or not text.strip():
        return []

    entities = extract_entities(text)
    symptoms = entities["symptoms"]

    if not symptoms:
        return []

    negations = detect_negations(text)
    causal_results = extract_causality(text)

    evidence_found = bool(causal_results)

    for cue in SIDE_EFFECT_CUES:
        if re.search(
            r"\b" + re.escape(cue) + r"\b",
            text,
            re.IGNORECASE,
        ):
            evidence_found = True
            break

    if not evidence_found:
        return []

    results = []

    for symptom in symptoms:
        symptom_pattern = r"\b" + re.escape(symptom) + r"\b"

        for match in re.finditer(
            symptom_pattern,
            text,
            re.IGNORECASE,
        ):
            is_negated = False

            for negation in negations:
                if negation["end"] <= match.start():
                    distance = match.start() - negation["end"]

                    if distance <= 40:
                        is_negated = True
                        break

            if not is_negated:
                results.append(
                    {
                        "symptom": symptom,
                        "start": match.start(),
                        "end": match.end(),
                    }
                )

    unique_results = []

    for result in results:
        if result not in unique_results:
            unique_results.append(result)

    return unique_results


if __name__ == "__main__":
    review = "The medication caused nausea but did not cause dizziness."

    print(extract_side_effects(review))
