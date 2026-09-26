# Split a review into separate sentences.
# Also collect simple information about each sentence.

import re


def split_sentences(text):
    """Split review text into separate sentences."""

    if not isinstance(text, str):
        return []

    text = text.strip()

    if not text:
        return []

    sentences = re.split(r"(?<=[.!?])\s+", text)

    return [sentence.strip() for sentence in sentences if sentence.strip()]


def analyze_sentences(text):
    """Collect basic information about each sentence."""

    sentences = split_sentences(text)

    results = []

    for index, sentence in enumerate(sentences):
        words = re.findall(r"\b[\w'-]+\b", sentence)

        results.append(
            {
                "sentence_id": index + 1,
                "text": sentence,
                "word_count": len(words),
                "character_count": len(sentence),
            }
        )

    return results


if __name__ == "__main__":
    review = (
        "I started taking this medicine two weeks ago. "
        "It helped my symptoms. However, I experienced mild nausea."
    )

    results = analyze_sentences(review)

    for item in results:
        print(item)
        