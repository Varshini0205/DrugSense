# Test the aspect sentiment code.
# These checks make sure sentiment is linked to the right topic.

from nlp.aspect_sentiment import extract_aspect_sentiment


def test_positive_condition():
    result = extract_aspect_sentiment(
        "My acne improved."
    )

    assert {
        "aspect": "acne",
        "sentiment": "positive",
    } in result


def test_negative_symptom():
    result = extract_aspect_sentiment(
        "I had terrible nausea."
    )

    assert {
        "aspect": "nausea",
        "sentiment": "negative",
    } in result


def test_neutral_aspect():
    result = extract_aspect_sentiment(
        "I have acne."
    )

    assert {
        "aspect": "acne",
        "sentiment": "neutral",
    } in result


def test_empty_text():
    assert extract_aspect_sentiment("") == []


def test_non_string_input():
    assert extract_aspect_sentiment(None) == []
