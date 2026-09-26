# Run all NLP checks together.
# One failed check should not stop the whole review.

from nlp.text_preprocessing import clean_text
from nlp.sentence_analysis import analyze_sentences
from nlp.entity_extraction import extract_entities
from nlp.negation_detection import detect_negations
from nlp.uncertainty_detection import detect_uncertainty
from nlp.temporal_information import extract_temporal_information
from nlp.medication_details import extract_medication_details
from nlp.severity_detection import detect_severity
from nlp.relation_extraction import extract_relations
from nlp.causality import extract_causality
from nlp.side_effects import extract_side_effects
from nlp.coreference import resolve_coreference
from nlp.experiencer import detect_experiencer
from nlp.discourse import classify_sentence_roles
from nlp.sentiment_analysis import analyze_sentiment
from nlp.aspect_sentiment import extract_aspect_sentiment
from nlp.treatment_response import detect_treatment_response
from nlp.comparative import extract_comparative_changes
from nlp.events import extract_events
from nlp.timeline import build_timeline
from nlp.entity_normalization import normalize_entities
from nlp.semantic import compare_texts


def safe_call(function, text, default):
    try:
        return function(text)
    except Exception as error:
        return {
            "error": str(error),
            "value": default,
        }


def analyze_review(text):
    if not isinstance(text, str) or not text.strip():
        return {
            "review": text if isinstance(text, str) else "",
            "error": "Review text is empty.",
        }

    cleaned_text = clean_text(text)

    entities_result = safe_call(
        extract_entities,
        cleaned_text,
        {
            "drugs": [],
            "conditions": [],
            "symptoms": [],
        },
    )

    entities = entities_result

    normalized_result = {
        "drugs": normalize_entities(
            entities.get("drugs", [])
        ),
        "conditions": normalize_entities(
            entities.get("conditions", [])
        ),
        "symptoms": normalize_entities(
            entities.get("symptoms", [])
        ),
    }

    side_effects = safe_call(
        extract_side_effects,
        cleaned_text,
        [],
    )

    try:
        semantic_features = compare_texts(
            cleaned_text,
            normalized_result["conditions"],
        )
    except Exception as error:
        semantic_features = {
            "error": str(error),
            "value": {},
        }

    result = {
        "review": text,
        "cleaned_review": cleaned_text,

        "sentences": safe_call(
            analyze_sentences,
            cleaned_text,
            [],
        ),

        "entities": {
            "drugs": entities.get("drugs", []),
            "conditions": entities.get("conditions", []),
            "symptoms": entities.get("symptoms", []),
            "normalized": normalized_result,
            "side_effects": side_effects,
        },

        "negation": safe_call(
            detect_negations,
            cleaned_text,
            [],
        ),

        "uncertainty": safe_call(
            detect_uncertainty,
            cleaned_text,
            [],
        ),

        "temporal_information": safe_call(
            extract_temporal_information,
            cleaned_text,
            [],
        ),

        "medication_details": safe_call(
            extract_medication_details,
            cleaned_text,
            {},
        ),

        "severity": safe_call(
            detect_severity,
            cleaned_text,
            [],
        ),

        "relations": safe_call(
            extract_relations,
            cleaned_text,
            [],
        ),

        "causal_relations": safe_call(
            extract_causality,
            cleaned_text,
            [],
        ),

        "coreference": safe_call(
            resolve_coreference,
            cleaned_text,
            [],
        ),

        "experiencer": safe_call(
            detect_experiencer,
            cleaned_text,
            [],
        ),

        "sentence_roles": safe_call(
            classify_sentence_roles,
            cleaned_text,
            [],
        ),

        "sentiment": safe_call(
            analyze_sentiment,
            cleaned_text,
            {},
        ),

        "aspect_sentiment": safe_call(
            extract_aspect_sentiment,
            cleaned_text,
            [],
        ),

        "treatment_response": safe_call(
            detect_treatment_response,
            cleaned_text,
            [],
        ),

        "comparative_changes": safe_call(
            extract_comparative_changes,
            cleaned_text,
            [],
        ),

        "events": safe_call(
            extract_events,
            cleaned_text,
            [],
        ),

        "timeline": safe_call(
            build_timeline,
            cleaned_text,
            [],
        ),

        "semantic_features": semantic_features,
    }

    return result


if __name__ == "__main__":
    review = (
        "Metformin helped my diabetes, "
        "but caused severe nausea."
    )

    result = analyze_review(review)

    print("\nPredicted NLP result:")
    print(result)
