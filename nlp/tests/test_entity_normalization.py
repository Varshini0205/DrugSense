# Test the entity normalization code.
# These checks make sure common variations are normalized.

from nlp.entity_normalization import (
    normalize_entity,
    normalize_entities,
)


def test_headaches():
    assert normalize_entity("headaches") == "headache"


def test_head_pain():
    assert normalize_entity("head pain") == "headache"


def test_depressed():
    assert normalize_entity("depressed") == "depression"


def test_dizzy():
    assert normalize_entity("dizzy") == "dizziness"


def test_unknown_term():
    assert normalize_entity("migraine") == "migraine"


def test_entity_list():
    result = normalize_entities(
        ["headaches", "head pain", "depressed"]
    )

    assert result == [
        "headache",
        "depression",
    ]


def test_empty_list():
    assert normalize_entities([]) == []


def test_non_string():
    assert normalize_entity(None) is None
