# Test the model using a real review from the dataset.
# This lets us compare the prediction with the actual label.

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
    print("DRUGSENSE REAL REVIEW TEST")
    print("=" * 70)

    validation = pd.read_csv(
        VALIDATION_FILE
    )

    vectorizer = joblib.load(
        VECTOR_FILE
    )

    model = joblib.load(
        MODEL_FILE
    )

    row = validation.iloc[0]

    review = row["review"]
    actual = row["condition"]

    X = vectorizer.transform(
        [review]
    )

    prediction = model.predict(
        X
    )[0]

    print("\n📝 Review:")
    print(review)

    print("\n🎯 Actual condition:")
    print(actual)

    print("\n🔍 Predicted condition:")
    print(prediction)

    if actual == prediction:
        print("\n✅ Prediction is correct.")
    else:
        print("\n❌ Prediction is incorrect.")

    print("\n" + "=" * 70)
    print("REAL REVIEW TEST COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()