# Test uncertainty detection.
# These checks make sure uncertain statements are found correctly.

from nlp.uncertainty_detection import detect_uncertainty


def test_maybe():
    result = detect_uncertainty("Maybe this medicine caused nausea.")

    assert len(result) == 1
    assert result[0]["text"] == "Maybe"


def test_possibly():
    result = detect_uncertainty("This could possibly cause dizziness.")

    texts = [item["text"].lower() for item in result]

    assert "possibly" in texts
    assert "could" in texts


def test_think_and_might():
    result = detect_uncertainty("I think it might be helping.")

    texts = [item["text"].lower() for item in result]

    assert "i think" in texts
    assert "might" in texts


def test_multiple_uncertainty_phrases():
    text = "Perhaps it may help, but I am not sure."

    result = detect_uncertainty(text)

    texts = [item["text"].lower() for item in result]

    assert "perhaps" in texts
    assert "may" in texts
    assert "not sure" in texts


def test_empty_text():
    assert detect_uncertainty("") == []
    assert detect_uncertainty(None) == []