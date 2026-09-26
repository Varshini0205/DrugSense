import os
import joblib
import numpy as np


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

VECTOR_PATH = os.path.join(
    BASE_DIR,
    "models",
    "final_tfidf_vectorizer.joblib"
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "final_svm_model.joblib"
)


_vectorizer = None
_model = None


def load_model():
    global _vectorizer
    global _model

    if _vectorizer is None:
        _vectorizer = joblib.load(VECTOR_PATH)

    if _model is None:
        _model = joblib.load(MODEL_PATH)

    return _vectorizer, _model


def is_valid_condition_label(label):
    if not isinstance(label, str):
        return False

    label = label.strip()

    if len(label) < 3:
        return False

    # Reject obvious corrupted dataset labels.
    if any(char in label for char in ["<", ">", "/", "(", ")", "[", "]"]):
        return False

    if label.lower() in {
        "n",
        "pe",
        "eve",
        "ge",
        "me",
        "gas",
    }:
        return False

    return True


def normalize_scores(scores):
    """
    Convert raw SVM decision scores into relative
    normalized scores that sum to 1.

    These values are NOT medical probabilities.
    """

    if scores is None:
        return []

    try:
        values = np.asarray(
            scores,
            dtype=float
        )

        if values.size == 0:
            return []

        shifted = values - np.max(values)

        exp_values = np.exp(shifted)

        total = np.sum(exp_values)

        if total == 0 or not np.isfinite(total):
            return []

        normalized = exp_values / total

        return normalized.tolist()

    except (TypeError, ValueError):
        return []


def predict_condition(review):
    """
    Predict the medical-condition label associated
    with the review text.

    The prediction is a dataset classification result,
    not a medical diagnosis.
    """

    if not isinstance(review, str):
        return {
            "condition": None,
            "score": None,
            "normalized_score": None,
            "top_predictions": [],
            "error": "Review must be text.",
        }

    review = review.strip()

    if not review:
        return {
            "condition": None,
            "score": None,
            "normalized_score": None,
            "top_predictions": [],
            "error": "Review text is empty.",
        }

    try:
        vectorizer, model = load_model()

        features = vectorizer.transform(
            [review]
        )

        decision_scores = model.decision_function(
            features
        )

        scores = np.asarray(
            decision_scores,
            dtype=float
        ).reshape(-1)

        classes = np.asarray(
            model.classes_
        )

        predicted_index = int(
            np.argmax(scores)
        )

        predicted_condition = str(
            classes[predicted_index]
        )

        predicted_score = float(
            scores[predicted_index]
        )

        normalized_scores = normalize_scores(
            scores
        )

        normalized_score = float(
            normalized_scores[predicted_index]
        )

        # Rank all classes, then keep only valid labels.
        ranked_indices = np.argsort(
            scores
        )[::-1]

        top_predictions = []

        for index in ranked_indices:
            index = int(index)

            condition = str(
                classes[index]
            ).strip()

            if not is_valid_condition_label(
                condition
            ):
                continue

            top_predictions.append(
                {
                    "condition": condition,
                    "score": float(
                        scores[index]
                    ),
                    "normalized_score": float(
                        normalized_scores[index]
                    ),
                }
            )

            if len(top_predictions) == 5:
                break

        return {
            "condition": predicted_condition,
            "score": predicted_score,
            "normalized_score": normalized_score,
            "top_predictions": top_predictions,
            "error": None,
        }

    except Exception as error:
        return {
            "condition": None,
            "score": None,
            "normalized_score": None,
            "top_predictions": [],
            "error": str(error),
        }


def get_model_info():
    try:
        vectorizer, model = load_model()

        return {
            "model": "Linear Support Vector Machine",
            "algorithm": "LinearSVC",
            "features": len(
                vectorizer.vocabulary_
            ),
            "classes": len(
                model.classes_
            ),
            "error": None,
        }

    except Exception as error:
        return {
            "model": None,
            "algorithm": None,
            "features": None,
            "classes": None,
            "error": str(error),
        }


if __name__ == "__main__":

    result = predict_condition(
        "Metformin helped my diabetes."
    )

    print(result)
