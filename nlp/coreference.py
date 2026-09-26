# Connect simple words like "it" to the thing mentioned before.
# This handles common patient-review examples.

import re


PRONOUNS = ["it", "they", "this", "that"]


def resolve_coreference(text):
    """Find simple references to earlier words."""

    if not isinstance(text, str) or not text.strip():
        return []

    sentences = re.split(r"(?<=[.!?])\s+", text.strip())

    results = []

    previous_entity = None

    for sentence_index, sentence in enumerate(sentences):
        words = sentence.split()

        for pronoun in PRONOUNS:
            pattern = r"\b" + pronoun + r"\b"

            match = re.search(
                pattern,
                sentence,
                re.IGNORECASE,
            )

            if match and previous_entity:
                results.append(
                    {
                        "reference": match.group(),
                        "resolved_to": previous_entity,
                        "sentence": sentence_index,
                    }
                )

        for word in words:
            clean_word = re.sub(
                r"[^A-Za-z0-9-]",
                "",
                word,
            )

            if clean_word.lower() in {
                "medication",
                "medicine",
                "drug",
                "nexplanon",
                "metformin",
                "ibuprofen",
                "aspirin",
                "sertraline",
            }:
                previous_entity = clean_word

    return results


if __name__ == "__main__":
    review = "Nexplanon caused nausea. It made me dizzy."

    print(resolve_coreference(review))
