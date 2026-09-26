# Create the final confusion matrix.
# This uses the cleaned model and cleaned labels.

from pathlib import Path
import pandas as pd
import joblib

from sklearn.metrics import confusion_matrix


DATA_DIR = Path(r"C:\Users\varsh\patient_drug_nlp\data")
MODEL_DIR = Path(r"C:\Users\varsh\patient_drug_nlp\models")

VALIDATION_FILE = DATA_DIR / "fixed_validation_split.csv"
VECTOR_FILE = MODEL_DIR / "fixed_tfidf_vectorizer.joblib"
MODEL_FILE = MODEL_DIR / "fixed_svm_model.joblib"


def main():
    print("=" * 70)
    print("DRUGSENSE FINAL CONFUSION MATRIX")
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

    print("\n🔍 Creating predictions...")

    X_validation = vectorizer.transform(
        validation["review"]
    )

    predictions = model.predict(
        X_validation
    )

    labels = sorted(
        validation["condition"].unique()
    )

    matrix = confusion_matrix(
        validation["condition"],
        predictions,
        labels=labels
    )

    matrix_df = pd.DataFrame(
        matrix,
        index=labels,
        columns=labels
    )

    matrix_df.to_csv(
        DATA_DIR / "final_confusion_matrix.csv"
    )

    print("\n💾 Saved:")
    print("data\\final_confusion_matrix.csv")

    print("\n" + "=" * 70)
    print("FINAL CONFUSION MATRIX COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()