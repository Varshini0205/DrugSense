# Compare two pieces of text using shared words.
# This gives us a simple similarity score.

import re


def _words(text):
    return set(
        re.findall(
            r"\b[a-zA-Z]+\b",
            text.lower(),
        )
    )


def calculate_similarity(text_a, text_b):
    """Calculate simple word overlap similarity."""

    if not isinstance(text_a, str):
        return 0.0

    if not isinstance(text_b, str):
        return 0.0

    words_a = _words(text_a)
    words_b = _words(text_b)

    if not words_a or not words_b:
        return 0.0

    intersection = words_a.intersection(words_b)
    union = words_a.union(words_b)

    return len(intersection) / len(union)


def compare_texts(text, candidates):
    """Compare text with a list of candidate texts."""

    if not isinstance(text, str):
        return []

    if not isinstance(candidates, list):
        return []

    results = []

    for candidate in candidates:
        if not isinstance(candidate, str):
            continue

        results.append(
            {
                "text": candidate,
                "similarity": calculate_similarity(
                    text,
                    candidate,
                ),
            }
        )

    results.sort(
        key=lambda item: item["similarity"],
        reverse=True,
    )

    return results


if __name__ == "__main__":
    print(
        calculate_similarity(
            "severe headache and nausea",
            "headache and nausea",
        )
    )
