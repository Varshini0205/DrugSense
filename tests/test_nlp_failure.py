# Test NLP failure handling.
# This makes sure an NLP error is handled safely.

import ml.ml_pipeline as ml_pipeline


def test_nlp_exception(monkeypatch):
    def broken_analysis(text):
        raise RuntimeError("NLP analysis failed.")

    monkeypatch.setattr(
        ml_pipeline,
        "analyze_review",
        broken_analysis,
    )

    result = ml_pipeline.analyze_review_with_prediction(
        "Metformin helped my diabetes."
    )

    assert result["error"] == "Analysis failed."
    assert "NLP analysis failed." in result["details"]


def test_normal_analysis_still_works():
    result = ml_pipeline.analyze_review_with_prediction(
        "Metformin helped my diabetes but caused nausea."
    )

    assert "prediction" in result
    assert result["prediction"]["condition"] is not None
