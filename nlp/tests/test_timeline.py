# Test the timeline code.
# These checks make sure events stay in the correct order.

from nlp.timeline import build_timeline


def test_timeline_has_events():
    result = build_timeline(
        "I started taking the medication. "
        "Three days later I developed nausea."
    )

    assert len(result) == 2


def test_event_order():
    result = build_timeline(
        "I started taking the medication. "
        "Three days later I developed nausea."
    )

    assert result[0]["event"] == "MEDICATION_START"
    assert result[1]["event"] == "SYMPTOM_DEVELOPED"


def test_timeline_position():
    result = build_timeline(
        "I started taking the medication. "
        "Three days later I developed nausea."
    )

    assert result[0]["position"] < result[1]["position"]


def test_empty_text():
    assert build_timeline("") == []


def test_non_string_input():
    assert build_timeline(None) == []
