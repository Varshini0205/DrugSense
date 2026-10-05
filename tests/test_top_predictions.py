# Show the most likely model predictions.
# This helps us understand the model output.

from pathlib import Path
import joblib


MODEL_DIR = Path(r"C:\Users\varsh\patient_drug_nlp\models")

VECTOR_FILE = MODEL_DIR / "fixed_tfidf_vectorizer.joblib"
MODEL_FILE = MODEL_DIR / "fixed_svm_model.joblib"


def main():
    print("=" * 70)
    print("DRUGSENSE TOP PREDICTIONS")
    print("=" * 70)

    vectorizer = joblib.load(VECTOR_FILE)
    model = joblib.load(MODEL_FILE)

    review = (
        "I have been taking this medicine for two months. "
        "It helped with my symptoms but I experienced mild nausea "
        "and a headache during the first week."
    )

    print("\n📝 Review:")
    print(review)

    X = vectorizer.transform([review])

    scores = model.decision_function(X)[0]

    classes = model.classes_

    top_indices = scores.argsort()[-3:][::-1]

    print("\n🔍 TOP 3 PREDICTIONS")

    for index in top_indices:
        print(
            f"{classes[index]:<35} "
            f"Score: {scores[index]:.4f}"
        )

    print("\n" + "=" * 70)
    print("TOP PREDICTION TEST COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()