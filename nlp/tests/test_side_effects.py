# Test the side effect code.
# These checks make sure symptoms are handled correctly.

from nlp.side_effects import extract_side_effects


def test_causal_side_effect():
    result = extract_side_effects(
        "The medication caused nausea."
    )

    assert result[0]["symptom"] == "nausea"


def test_after_taking():
    result = extract_side_effects(
        "After taking the medication I developed nausea."
    )

    assert result[0]["symptom"] == "nausea"


def test_no_side_effect_without_evidence():
    result = extract_side_effects(
        "I have nausea and took the medication."
    )

    assert result == []


def test_negated_side_effect():
    result = extract_side_effects(
        "The medication did not cause nausea."
    )

    assert result == []


def test_non_string_input():
    result = extract_side_effects(None)

    assert result == []
