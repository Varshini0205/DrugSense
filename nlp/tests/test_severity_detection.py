# Test symptom severity detection.
# These checks make sure severity levels are found correctly.

from nlp.severity_detection import detect_severity


def test_mild_severity():
    result = detect_severity("I had mild nausea.")

    assert len(result) == 1
    assert result[0]["severity"] == "mild"


def test_moderate_severity():
    result = detect_severity("I experienced moderate pain.")

    assert len(result) == 1
    assert result[0]["severity"] == "moderate"


def test_severe_severity():
    result = detect_severity("I had severe headache.")

    assert len(result) == 1
    assert result[0]["severity"] == "severe"


def test_very_severe_does_not_overlap():
    result = detect_severity("I experienced very severe pain.")

    assert len(result) == 1
    assert result[0]["text"] == "very severe"
    assert result[0]["severity"] == "very severe"


def test_multiple_severities():
    text = "I had mild nausea and moderate pain."

    result = detect_severity(text)

    assert len(result) == 2
    assert result[0]["severity"] == "mild"
    assert result[1]["severity"] == "moderate"


def test_empty_text():
    assert detect_severity("") == []
    assert detect_severity(None) == []