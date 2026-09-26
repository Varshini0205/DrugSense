# Test simple negative statements.
# These checks make sure common negative phrases are found.

from nlp.negation_detection import detect_negations


def test_no_phrase():
    result = detect_negations("I have no nausea.")

    assert len(result) == 1
    assert result[0]["text"] == "nausea"


def test_without_phrase():
    result = detect_negations("I am without headache.")

    assert len(result) == 1
    assert result[0]["text"] == "headache"


def test_did_not_phrase():
    result = detect_negations("The medicine did not help.")

    assert len(result) == 1
    assert result[0]["text"] == "help"


def test_multiple_negations():
    text = "I have no nausea. I am without headache."

    result = detect_negations(text)

    assert len(result) == 2
    assert result[0]["text"] == "nausea"
    assert result[1]["text"] == "headache"


def test_empty_text():
    assert detect_negations("") == []
    assert detect_negations(None) == []