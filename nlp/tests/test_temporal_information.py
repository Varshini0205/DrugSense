# Test time-related information.
# These checks make sure common time phrases are found.

from nlp.temporal_information import extract_temporal_information


def test_relative_time():
    result = extract_temporal_information("I started this medicine two weeks ago.")

    assert len(result) == 1
    assert result[0]["text"] == "two weeks ago"


def test_yesterday():
    result = extract_temporal_information("I had a headache yesterday.")

    assert len(result) == 1
    assert result[0]["text"] == "yesterday"


def test_after_starting_medicine():
    result = extract_temporal_information(
        "I felt better after starting the medicine."
    )

    assert len(result) == 1
    assert result[0]["text"] == "after starting the medicine"


def test_multiple_temporal_phrases():
    text = (
        "I started the medicine two weeks ago. "
        "The headache began yesterday."
    )

    result = extract_temporal_information(text)

    assert len(result) == 2
    assert result[0]["text"] == "two weeks ago"
    assert result[1]["text"] == "yesterday"


def test_empty_text():
    assert extract_temporal_information("") == []
    assert extract_temporal_information(None) == []