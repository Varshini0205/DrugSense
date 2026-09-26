# Test several real reviews.
# This gives us a quick view of model behavior.

from pathlib import Path
import pandas as pd
import joblib


DATA_DIR = Path(r"C:\Users\varsh\patient_drug_nlp\data")
MODEL_DIR = Path(r"C:\Users\varsh\patient_drug_nlp\models")

VALIDATION_FILE = DATA_DIR / "fixed_validation_split.csv"
VECTOR_FILE = MODEL_DIR / "fixed_tfidf_vectorizer.joblib"
MODEL_FILE = MODEL_DIR / "fixed_svm_model.joblib"


def main():
    print("=" * 70)
    print("DRUGSENSE MULTIPLE REVIEW TEST")
    print("=" * 70)

    validation = pd.read_csv(VALIDATION_FILE)

    vectorizer = joblib.load(VECTOR_FILE)
    model = joblib.load(MODEL_FILE)

    sample = validation.sample(
        n=10,
        random_state=42
    )

    X = vectorizer.transform(
        sample["review"]
    )

    predictions = model.predict(X)

    correct = 0

    print("\n🔍 RESULTS\n")

    for number, (_, row) in enumerate(
        sample.iterrows(),
        start=1
    ):
        actual = row["condition"]
        prediction = predictions[number - 1]

        if actual == prediction:
            correct += 1
            status = "✅"
        else:
            status = "❌"

        print(
            f"{number}. {status} "
            f"Actual: {actual} | "
            f"Predicted: {prediction}"
        )

    print(
        f"\n📊 Correct: {correct}/10"
    )

    print(
        f"📊 Sample accuracy: {correct / 10:.2%}"
    )

    print("\n" + "=" * 70)
    print("MULTIPLE REVIEW TEST COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()