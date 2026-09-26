# Test the causality code.
# These checks make sure causal expressions are found.

from nlp.causality import extract_causality


def test_caused():
    result = extract_causality("The medication caused nausea.")

    assert result[0]["expression"].lower() == "caused"


def test_led_to():
    result = extract_causality("The medication led to dizziness.")

    assert result[0]["expression"].lower() == "led to"


def test_multiple_causal_expressions():
    result = extract_causality(
        "The medication caused nausea and led to dizziness."
    )

    assert len(result) == 2


def test_no_causality():
    result = extract_causality("The medication helped my condition.")

    assert result == []


def test_non_string_input():
    result = extract_causality(None)

    assert result == []
