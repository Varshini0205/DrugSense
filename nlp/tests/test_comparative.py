# Test the change analysis code.
# These checks make sure improvement and worsening are found.

from nlp.comparative import extract_comparative_changes


def test_improved():
    result = extract_comparative_changes(
        "My acne improved."
    )

    assert result[0]["change"] == "improved"


def test_worsened():
    result = extract_comparative_changes(
        "My headaches became worse."
    )

    assert result[0]["change"] == "worsened"


def test_unchanged():
    result = extract_comparative_changes(
        "My symptoms are unchanged."
    )

    assert result[0]["change"] == "unchanged"


def test_multiple_changes():
    result = extract_comparative_changes(
        "My acne improved but my headaches became worse."
    )

    assert len(result) == 2


def test_empty_text():
    assert extract_comparative_changes("") == []


def test_non_string_input():
    assert extract_comparative_changes(None) == []
