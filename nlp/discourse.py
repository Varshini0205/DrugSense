# Classify what each sentence is mainly about.
# This gives each sentence a simple role.

import re


ROLE_PATTERNS = [
    (
        "MEDICATION_START",
        [
            "started the medication",
            "started taking",
            "began taking",
            "started using",
        ],
    ),
    (
        "MEDICATION_STOP",
        [
            "stopped the medication",
            "stopped taking",
            "discontinued",
            "quit taking",
        ],
    ),
    (
        "DOSAGE",
        [
            r"\b\d+\s*mg\b",
            "tablet",
            "pill",
            "dose",
            "dosage",
        ],
    ),
    (
        "SIDE_EFFECT",
        [
            "caused",
            "gave me",
            "developed",
            "side effect",
            "after taking",
        ],
    ),
    (
        "IMPROVEMENT",
        [
            "improved",
            "better",
            "helped",
            "relieved",
            "much better",
        ],
    ),
    (
        "WORSENING",
        [
            "worse",
            "worsened",
            "getting worse",
            "increased pain",
            "more severe",
        ],
    ),
    (
        "TREATMENT_RESPONSE",
        [
            "worked",
            "did not work",
            "working",
            "effective",
            "ineffective",
        ],
    ),
    (
        "TEMPORAL_EVENT",
        [
            "yesterday",
            "today",
            "tomorrow",
            "days later",
            "weeks later",
            "after",
            "before",
            "since",
        ],
    ),
    (
        "SYMPTOM",
        [
            "pain",
            "nausea",
            "headache",
            "dizziness",
            "fatigue",
            "vomiting",
            "insomnia",
        ],
    ),
]


def classify_sentence_role(sentence):
    """Find the main role of a sentence."""

    if not isinstance(sentence, str):
        return "BACKGROUND"

    text = sentence.strip().lower()

    if not text:
        return "BACKGROUND"

    for role, patterns in ROLE_PATTERNS:
        for pattern in patterns:
            if pattern.startswith(r"\b"):
                found = re.search(pattern, text)
            else:
                found = re.search(
                    r"\b" + re.escape(pattern) + r"\b",
                    text,
                )

            if found:
                return role

    return "BACKGROUND"


def classify_sentence_roles(text):
    """Classify each sentence in a review."""

    if not isinstance(text, str) or not text.strip():
        return []

    sentences = re.split(
        r"(?<=[.!?])\s+",
        text.strip(),
    )

    results = []

    for index, sentence in enumerate(sentences):
        results.append(
            {
                "sentence_id": index,
                "text": sentence,
                "role": classify_sentence_role(sentence),
            }
        )

    return results


if __name__ == "__main__":
    review = (
        "I started the medication. "
        "Three days later I developed nausea. "
        "My pain is much better."
    )

    print(classify_sentence_roles(review))
