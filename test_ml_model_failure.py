# Test model failure handling.
# This makes sure a model error is returned safely.

import ml.ml_pipeline as ml_pipeline


def test_model_exception(monkeypatch):
    def broken_prediction(text):
        raise RuntimeError("Model loading failed.")

    monkeypatch.setattr(
        ml_pipeline,
        "predict_condition",
        broken_prediction,
    )

    result = ml_pipeline.analyze_review_with_prediction(
        "Metformin helped my diabetes."
    )

    assert result["error"] == "Analysis failed."
    assert "Model loading failed." in result["details"]


def test_valid_prediction_after_failure_test():
    result = ml_pipeline.analyze_review_with_prediction(
        "Metformin helped my diabetes."
    )

    assert "prediction" in result
    assert result["prediction"]["condition"] is not None
