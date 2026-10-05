# Test the complete NLP and ML pipeline.
# These checks make sure valid and invalid reviews are handled.

from ml.ml_pipeline import analyze_review_with_prediction


def test_prediction_details():
    result = analyze_review_with_prediction(
        "Metformin helped my diabetes but caused nausea."
    )

    assert "prediction" in result
    assert result["prediction"]["condition"] is not None
    assert isinstance(
        result["prediction"]["score"],
        float,
    )
    assert 0.0 <= result["prediction"]["normalized_score"] <= 1.0


def test_top_predictions():
    result = analyze_review_with_prediction(
        "Metformin helped my diabetes but caused nausea."
    )

    predictions = result["prediction"]["top_predictions"]

    assert isinstance(predictions, list)
    assert len(predictions) == 5


def test_entities():
    result = analyze_review_with_prediction(
        "Metformin helped my diabetes but caused nausea."
    )

    assert "metformin" in result["entities"]["drugs"]
    assert "diabetes" in result["entities"]["conditions"]
    assert "nausea" in result["entities"]["symptoms"]


def test_side_effects():
    result = analyze_review_with_prediction(
        "Metformin helped my diabetes but caused nausea."
    )

    assert len(
        result["entities"]["side_effects"]
    ) >= 1


def test_empty_review():
    result = analyze_review_with_prediction("")

    assert "error" in result


def test_non_string_review():
    result = analyze_review_with_prediction(None)

    assert "error" in result
