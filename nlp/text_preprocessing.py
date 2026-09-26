# Clean review text before NLP analysis.
# Keep useful words and sentence punctuation.

import html
import re


def clean_text(text):
    """Clean and normalize review text."""

    if not isinstance(text, str):
        return ""

    text = html.unescape(text)

    text = re.sub(r"<[^>]+>", " ", text)

    text = re.sub(r"https?://\S+|www\.\S+", " ", text)

    text = text.lower()

    text = re.sub(r"\s+", " ", text)

    return text.strip()


if __name__ == "__main__":
    review = (
        "<p>This medicine helped me a LOT!</p> "
        "Visit https://example.com for details."
    )

    print(clean_text(review))