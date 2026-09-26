# Test treatment response and negative response statements.
# These checks make sure treatment results are classified correctly.

from nlp.treatment_response import detect_treatment_response


def test_improved_response():
    result = detect_treatment_response("The medicine helped my pain.")

    assert result[0]["response"] == "improved"


def test_worsened_response():
    result = detect_treatment_response("My headache got worse.")

    assert result[0]["response"] == "worsened"


def test_no_effect_response():
    result = detect_treatment_response("The medicine did not help.")

    assert result[0]["response"] == "no_effect"


def test_negated_helped():
    result = detect_treatment_response("The medicine did not help my pain.")

    assert result[0]["response"] == "no_effect"


def test_negated_improved():
    result = detect_treatment_response("The medicine did not improve my symptoms.")

    assert result[0]["response"] == "no_effect"


def test_positive_improved():
    result = detect_treatment_response("The medicine improved my symptoms.")

    assert result[0]["response"] == "improved"


def test_no_overlap():
    result = detect_treatment_response("My headache got worse.")

    assert [item["text"] for item in result] == ["got worse"]


def test_empty_text():
    assert detect_treatment_response("") == []
    assert detect_treatment_response(None) == []