# Test medical entity extraction.
# These checks make sure simple and multi-word terms work correctly.

from nlp.entity_extraction import extract_entities


def test_drug_extraction():
    text = "I take metformin every day."

    result = extract_entities(text)

    assert "metformin" in result["drugs"]


def test_condition_extraction():
    text = "I have diabetes and anxiety."

    result = extract_entities(text)

    assert "diabetes" in result["conditions"]
    assert "anxiety" in result["conditions"]


def test_symptom_extraction():
    text = "I experienced nausea and dizziness."

    result = extract_entities(text)

    assert "nausea" in result["symptoms"]
    assert "dizziness" in result["symptoms"]


def test_multiple_entity_types():
    text = "Metformin helped my diabetes but caused nausea."

    result = extract_entities(text)

    assert "metformin" in result["drugs"]
    assert "diabetes" in result["conditions"]
    assert "nausea" in result["symptoms"]


def test_multi_word_entities():
    text = (
        "I have major depressive disorder and high blood pressure. "
        "I also experienced chest pain."
    )

    result = extract_entities(text)

    assert "major depressive disorder" in result["conditions"]
    assert "high blood pressure" in result["conditions"]
    assert "chest pain" in result["symptoms"]


def test_no_overlapping_entities():
    text = "I experienced chest pain."

    result = extract_entities(text)

    assert result["symptoms"] == ["chest pain"]


def test_no_entities():
    text = "The weather is pleasant today."

    result = extract_entities(text)

    assert result["drugs"] == []
    assert result["conditions"] == []
    assert result["symptoms"] == []