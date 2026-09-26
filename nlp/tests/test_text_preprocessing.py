# Test the text cleaning functions.
# These checks make sure review text is cleaned correctly.

from nlp.text_preprocessing import clean_text


def test_html_is_removed():
    text = "<p>This medicine helped me.</p>"

    result = clean_text(text)

    assert result == "this medicine helped me."


def test_url_is_removed():
    text = "This medicine helped me. Visit https://example.com"

    result = clean_text(text)

    assert result == "this medicine helped me. visit"


def test_text_is_lowercase():
    text = "This Medicine HELPED Me."

    result = clean_text(text)

    assert result == "this medicine helped me."


def test_empty_text():
    assert clean_text("") == ""
    assert clean_text(None) == ""


def test_extra_spaces_are_removed():
    text = "This    medicine     helped me."

    result = clean_text(text)

    assert result == "this medicine helped me."