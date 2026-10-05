# Step 26: Check examples where the model made mistakes.
# This helps us understand what the model gets wrong.

from pathlib import Path
import pandas as pd
import joblib

DATA_DIR = Path(r"C:\Users\varsh\patient_drug_nlp\data")
MODEL_DIR = Path(r"C:\Users\varsh\patient_drug_nlp\models")

VALIDATION_FILE = DATA_DIR / "clean_validation_split.csv"
VECTOR_FILE = MODEL_DIR / "clean_tfidf_vectorizer.joblib"
MODEL_FILE = MODEL_DIR / "clean_svm_model.joblib"


def main():
    print("=" * 70)
    print("DRUGSENSE MODEL ERROR CHECK")
    print("=" * 70)

    validation = pd.read_csv(VALIDATION_FILE)

    vectorizer = joblib.load(VECTOR_FILE)
    model = joblib.load(MODEL_FILE)

    print("\n🔍 Checking validation reviews...")

    X_validation = vectorizer.transform(
        validation["review"]
    )

    predictions = model.predict(X_validation)

    validation["prediction"] = predictions

    errors = validation[
        validation["condition"] != validation["prediction"]
    ].copy()

    print(f"\n📊 Total validation reviews: {len(validation):,}")
    print(f"❌ Incorrect predictions: {len(errors):,}")
    print(
        f"✅ Correct predictions: "
        f"{len(validation) - len(errors):,}"
    )

    print("\n🔎 SAMPLE ERRORS")

    for _, row in errors.head(20).iterrows():
        print("\nReview:")
        print(row["review"][:300])

        print(f"Actual     : {row['condition']}")
        print(f"Predicted  : {row['prediction']}")

    errors.to_csv(
        DATA_DIR / "model_errors.csv",
        index=False
    )

    print("\n💾 Saved: data\\model_errors.csv")

    print("\n" + "=" * 70)
    print("ERROR CHECK COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()