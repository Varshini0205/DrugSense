# Test the similarity code.
# These checks make sure similar text gets a higher score.

from nlp.semantic import (
    calculate_similarity,
    compare_texts,
)


def test_similar_text():
    score = calculate_similarity(
        "severe headache and nausea",
        "headache and nausea",
    )

    assert score > 0


def test_identical_text():
    score = calculate_similarity(
        "headache nausea",
        "headache nausea",
    )

    assert score == 1.0


def test_different_text():
    score = calculate_similarity(
        "headache nausea",
        "blood pressure",
    )

    assert score == 0.0


def test_empty_text():
    assert (
        calculate_similarity(
            "",
            "headache",
        )
        == 0.0
    )


def test_non_string_input():
    assert (
        calculate_similarity(
            None,
            "headache",
        )
        == 0.0
    )


def test_compare_texts():
    result = compare_texts(
        "headache nausea",
        [
            "headache nausea",
            "blood pressure",
        ],
    )

    assert result[0]["text"] == "headache nausea"
    assert result[0]["similarity"] == 1.0


def test_invalid_candidates():
    result = compare_texts(
        "headache",
        None,
    )

    assert result == []
