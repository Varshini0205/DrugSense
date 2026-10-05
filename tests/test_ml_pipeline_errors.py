# Test safe handling of pipeline errors.
# These checks make sure bad input does not break the app.

from ml.ml_pipeline import analyze_review_with_prediction


def test_empty_review():
    result = analyze_review_with_prediction("")

    assert result["error"] == "Review text is empty."


def test_none_review():
    result = analyze_review_with_prediction(None)

    assert result["error"] == "Review text is empty."


def test_number_review():
    result = analyze_review_with_prediction(12345)

    assert result["error"] == "Review text is empty."


def test_valid_review():
    result = analyze_review_with_prediction(
        "Metformin helped my diabetes but caused nausea."
    )

    assert "prediction" in result
    assert result["prediction"]["condition"] is not None
