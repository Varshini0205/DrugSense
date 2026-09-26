# Test basic sentiment detection.
# These checks make sure positive, negative, and neutral text work.

from nlp.sentiment_analysis import analyze_sentiment


def test_positive_sentiment():
    result = analyze_sentiment("This medicine helped me and I feel better.")

    assert result["label"] == "positive"
    assert result["score"] > 0


def test_negative_sentiment():
    result = analyze_sentiment("I had terrible nausea and headache.")

    assert result["label"] == "negative"
    assert result["score"] < 0


def test_neutral_sentiment():
    result = analyze_sentiment("I started this medicine yesterday.")

    assert result["label"] == "neutral"
    assert result["score"] == 0


def test_empty_text():
    result = analyze_sentiment("")

    assert result["label"] == "neutral"
    assert result["score"] == 0


def test_none_text():
    result = analyze_sentiment(None)

    assert result["label"] == "neutral"
    assert result["score"] == 0