# Test score handling and errors.
# These checks make sure prediction stays safe.

from ml_predictor import (
    predict_condition,
    normalize_scores,
)


def test_prediction():
    result = predict_condition(
        "Metformin helped my diabetes."
    )

    assert result["condition"] is not None
    assert result["score"] is not None
    assert result["normalized_score"] is not None


def test_normalized_score_range():
    result = predict_condition(
        "Metformin helped my diabetes."
    )

    score = result["normalized_score"]

    assert 0.0 <= score <= 1.0


def test_top_predictions():
    result = predict_condition(
        "Metformin helped my diabetes."
    )

    assert len(
        result["top_predictions"]
    ) == 5

    for item in result["top_predictions"]:
        assert 0.0 <= item["normalized_score"] <= 1.0


def test_normalize_scores():
    scores = [1.0, 2.0, 3.0]

    result = normalize_scores(scores)

    assert len(result) == 3
    assert abs(sum(result) - 1.0) < 0.000001


def test_empty_review():
    result = predict_condition("")

    assert result["condition"] is None
    assert result["score"] is None
    assert result["normalized_score"] is None
    assert "error" in result


def test_non_string_input():
    result = predict_condition(None)

    assert result["condition"] is None
    assert "error" in result
