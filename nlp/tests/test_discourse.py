# Test the sentence role code.
# These checks make sure common sentence types are classified.

from nlp.discourse import (
    classify_sentence_role,
    classify_sentence_roles,
)


def test_medication_start():
    assert (
        classify_sentence_role(
            "I started the medication."
        )
        == "MEDICATION_START"
    )


def test_medication_stop():
    assert (
        classify_sentence_role(
            "I stopped taking the medication."
        )
        == "MEDICATION_STOP"
    )


def test_side_effect():
    assert (
        classify_sentence_role(
            "The medication caused nausea."
        )
        == "SIDE_EFFECT"
    )


def test_improvement():
    assert (
        classify_sentence_role(
            "My pain is much better."
        )
        == "IMPROVEMENT"
    )


def test_worsening():
    assert (
        classify_sentence_role(
            "My pain is getting worse."
        )
        == "WORSENING"
    )


def test_background():
    assert (
        classify_sentence_role(
            "This medication is commonly used."
        )
        == "BACKGROUND"
    )


def test_multiple_sentences():
    result = classify_sentence_roles(
        "I started the medication. "
        "Three days later I developed nausea."
    )

    assert len(result) == 2
    assert result[0]["role"] == "MEDICATION_START"
    assert result[1]["role"] == "SIDE_EFFECT"


def test_empty_text():
    assert classify_sentence_roles("") == []


def test_non_string_input():
    assert classify_sentence_roles(None) == []
