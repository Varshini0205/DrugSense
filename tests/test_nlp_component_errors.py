# Test errors from individual NLP parts.
# These checks make sure errors are recorded safely.

import nlp.pipeline as nlp_pipeline


def test_sentiment_error_is_recorded(monkeypatch):
    def broken_sentiment(text):
        raise RuntimeError("Sentiment failed.")

    monkeypatch.setattr(
        nlp_pipeline,
        "analyze_sentiment",
        broken_sentiment,
    )

    result = nlp_pipeline.analyze_review(
        "Metformin helped my diabetes."
    )

    assert "error" in result["sentiment"]
    assert result["sentiment"]["error"] == (
        "Sentiment failed."
    )


def test_entities_error_is_recorded(monkeypatch):
    def broken_entities(text):
        raise RuntimeError("Entity extraction failed.")

    monkeypatch.setattr(
        nlp_pipeline,
        "extract_entities",
        broken_entities,
    )

    result = nlp_pipeline.analyze_review(
        "Metformin helped my diabetes."
    )

    assert result["entities"]["drugs"] == []
    assert result["entities"]["conditions"] == []
    assert result["entities"]["symptoms"] == []


def test_normal_pipeline_still_works():
    result = nlp_pipeline.analyze_review(
        "Metformin helped my diabetes."
    )

    assert "entities" in result
    assert "sentiment" in result
