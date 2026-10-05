# Connect NLP results with the trained model.
# This keeps unexpected errors from breaking the application.

from nlp.pipeline import analyze_review
from ml.ml_predictor import predict_condition


def analyze_review_with_prediction(text):
    if not isinstance(text, str) or not text.strip():
        return {
            "error": "Review text is empty.",
        }

    try:
        result = analyze_review(text)

        if "error" in result:
            return result

        prediction = predict_condition(text)

        result["prediction"] = prediction

        return result

    except Exception as error:
        return {
            "error": "Analysis failed.",
            "details": str(error),
        }


if __name__ == "__main__":
    review = (
        "Metformin helped my diabetes, "
        "but caused severe nausea."
    )

    result = analyze_review_with_prediction(review)

    if "error" in result:
        print("\nError:")
        print(result["error"])

        if "details" in result:
            print(result["details"])
    else:
        print("\nPredicted condition:")
        print(result["prediction"]["condition"])

        print("\nModel score:")
        print(result["prediction"]["score"])

        print("\nNormalized score:")
        print(result["prediction"]["normalized_score"])

        print("\nTop predictions:")

        for item in result["prediction"]["top_predictions"]:
            print(
                f"{item['condition']}: "
                f"{item['score']:.4f} "
                f"({item['normalized_score']:.4f})"
            )

        print("\nSide effects:")
        print(result["entities"]["side_effects"])
