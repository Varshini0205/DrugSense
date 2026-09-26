# Test the complete NLP pipeline.
# These checks make sure all major results are returned.

from nlp.pipeline import analyze_review


def test_pipeline_returns_result():
    result = analyze_review(
        "Metformin helped my diabetes but caused nausea."
    )

    assert isinstance(result, dict)


def test_pipeline_review():
    result = analyze_review(
        "Metformin helped my diabetes."
    )

    assert result["review"] == (
        "Metformin helped my diabetes."
    )


def test_pipeline_entities():
    result = analyze_review(
        "Metformin helped my diabetes."
    )

    assert "metformin" in result["entities"]["drugs"]
    assert "diabetes" in result["entities"]["conditions"]


def test_pipeline_relations():
    result = analyze_review(
        "Metformin helped my diabetes but caused nausea."
    )

    assert len(result["relations"]) >= 1
    assert len(result["causal_relations"]) >= 1


def test_pipeline_sentiment():
    result = analyze_review(
        "The medicine helped me."
    )

    assert "sentiment" in result


def test_pipeline_timeline():
    result = analyze_review(
        "I started taking the medication. "
        "I developed nausea."
    )

    assert isinstance(result["timeline"], list)


def test_empty_review():
    result = analyze_review("")

    assert "error" in result


def test_non_string_input():
    result = analyze_review(None)

    assert "error" in result
