# Test the relation extraction code.
# These checks make sure the relationships are correct.

from nlp.relation_extraction import extract_relations


def test_caused_relation():
    text = "Metformin caused nausea."

    result = extract_relations(text)

    assert result == [
        {
            "subject": "metformin",
            "relation": "caused",
            "object": "nausea",
        }
    ]


def test_helped_relation():
    text = "Metformin helped my diabetes."

    result = extract_relations(text)

    assert result == [
        {
            "subject": "metformin",
            "relation": "helped",
            "object": "diabetes",
        }
    ]


def test_two_relations():
    text = "Metformin helped my diabetes but caused nausea."

    result = extract_relations(text)

    assert {
        "subject": "metformin",
        "relation": "helped",
        "object": "diabetes",
    } in result

    assert {
        "subject": "metformin",
        "relation": "caused",
        "object": "nausea",
    } in result


def test_no_relation():
    text = "Metformin is a medicine."

    result = extract_relations(text)

    assert result == []


def test_non_string_input():
    result = extract_relations(None)

    assert result == []