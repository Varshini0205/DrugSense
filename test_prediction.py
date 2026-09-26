# Test one new patient review.
# This checks that the saved model can classify new text.

from pathlib import Path
import joblib


MODEL_DIR = Path(r"C:\Users\varsh\patient_drug_nlp\models")

VECTOR_FILE = MODEL_DIR / "fixed_tfidf_vectorizer.joblib"
MODEL_FILE = MODEL_DIR / "fixed_svm_model.joblib"


def main():
    print("=" * 70)
    print("DRUGSENSE NEW REVIEW TEST")
    print("=" * 70)

    vectorizer = joblib.load(
        VECTOR_FILE
    )

    model = joblib.load(
        MODEL_FILE
    )

    review = (
        "I have been taking this medicine for two months. "
        "It helped with my symptoms but I experienced mild nausea "
        "and a headache during the first week."
    )

    print("\n📝 Review:")
    print(review)

    X = vectorizer.transform(
        [review]
    )

    prediction = model.predict(
        X
    )[0]

    print("\n🔍 Predicted condition:")
    print(prediction)

    print("\n" + "=" * 70)
    print("PREDICTION TEST COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()