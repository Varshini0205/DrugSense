# Test partial results when one NLP part fails.
# The rest of the analysis should still be returned.

import nlp.pipeline as nlp_pipeline


def test_pipeline_component_failure(monkeypatch):
    def broken_sentiment(text):
        raise RuntimeError("Sentiment failed.")

    monkeypatch.setattr(
        nlp_pipeline,
        "analyze_sentiment",
        broken_sentiment,
    )

    try:
        result = nlp_pipeline.analyze_review(
            "Metformin helped my diabetes."
        )
    except RuntimeError:
        result = None

    assert result is not None
    assert "entities" in result
    assert "sentiment" in result
