# Test the event extraction code.
# These checks make sure important events are found.

from nlp.events import extract_events


def test_medication_start():
    result = extract_events(
        "I started taking the medication."
    )

    assert result[0]["event"] == "MEDICATION_START"


def test_medication_stop():
    result = extract_events(
        "I stopped taking the medication."
    )

    assert result[0]["event"] == "MEDICATION_STOP"


def test_symptom_developed():
    result = extract_events(
        "I developed nausea."
    )

    assert result[0]["event"] == "SYMPTOM_DEVELOPED"


def test_treatment_change():
    result = extract_events(
        "I increased the dose."
    )

    assert result[0]["event"] == "TREATMENT_CHANGE"


def test_improvement():
    result = extract_events(
        "My acne improved."
    )

    assert result[0]["event"] == "IMPROVEMENT"


def test_worsening():
    result = extract_events(
        "My pain became worse."
    )

    assert result[0]["event"] == "WORSENING"


def test_empty_text():
    assert extract_events("") == []


def test_non_string_input():
    assert extract_events(None) == []
