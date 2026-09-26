# Test sentence splitting and sentence information.
# These checks make sure the module works correctly.

from nlp.sentence_analysis import split_sentences, analyze_sentences


def test_split_sentences():
    text = "I feel better. My pain is lower. I can sleep well."

    result = split_sentences(text)

    assert len(result) == 3
    assert result[0] == "I feel better."
    assert result[1] == "My pain is lower."
    assert result[2] == "I can sleep well."


def test_empty_text():
    assert split_sentences("") == []
    assert split_sentences(None) == []


def test_analyze_sentences():
    text = "The medicine helped me. I had mild nausea."

    result = analyze_sentences(text)

    assert len(result) == 2
    assert result[0]["sentence_id"] == 1
    assert result[1]["sentence_id"] == 2
    assert result[0]["word_count"] > 0
    assert result[1]["character_count"] > 0