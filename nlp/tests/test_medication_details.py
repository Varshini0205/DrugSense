# Test dosage, frequency, and duration extraction.
# These checks make sure medication details are found correctly.

from nlp.medication_details import extract_medication_details


def test_dosage_extraction():
    text = "I take 500 mg every day."

    result = extract_medication_details(text)

    assert "500 mg" in result["dosages"]


def test_frequency_extraction():
    text = "I take this medicine twice daily."

    result = extract_medication_details(text)

    assert "twice daily" in result["frequencies"]


def test_duration_with_number():
    text = "I used this medicine for 5 days."

    result = extract_medication_details(text)

    assert "for 5 days" in result["durations"]


def test_duration_with_word():
    text = "I used this medicine for two weeks."

    result = extract_medication_details(text)

    assert "for two weeks" in result["durations"]


def test_multiple_details():
    text = "I take 500 mg twice daily for two weeks."

    result = extract_medication_details(text)

    assert "500 mg" in result["dosages"]
    assert "twice daily" in result["frequencies"]
    assert "for two weeks" in result["durations"]


def test_empty_text():
    result = extract_medication_details("")

    assert result["dosages"] == []
    assert result["frequencies"] == []
    assert result["durations"] == []