# Test the coreference code.
# These checks make sure simple references are connected.

from nlp.coreference import resolve_coreference


def test_it_refers_to_drug():
    result = resolve_coreference(
        "Nexplanon caused nausea. It made me dizzy."
    )

    assert result[0]["reference"].lower() == "it"
    assert result[0]["resolved_to"].lower() == "nexplanon"


def test_medication_reference():
    result = resolve_coreference(
        "The medication helped my acne. It also improved my skin."
    )

    assert result[0]["resolved_to"].lower() == "medication"


def test_no_reference():
    result = resolve_coreference(
        "Nexplanon caused nausea."
    )

    assert result == []


def test_empty_text():
    result = resolve_coreference("")

    assert result == []


def test_non_string_input():
    result = resolve_coreference(None)

    assert result == []
