# Test the experiencer code.
# These checks make sure the correct person is found.

from nlp.experiencer import detect_experiencer


def test_patient():
    result = detect_experiencer("I had headaches.")

    assert result[0]["experiencer"] == "patient"


def test_other_person():
    result = detect_experiencer(
        "My husband had headaches."
    )

    assert result[0]["experiencer"] == "other person"


def test_mother():
    result = detect_experiencer(
        "My mother experienced nausea."
    )

    assert result[0]["experiencer"] == "other person"


def test_empty_text():
    result = detect_experiencer("")

    assert result == []


def test_non_string_input():
    result = detect_experiencer(None)

    assert result == []
