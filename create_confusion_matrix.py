# Confusion matrix for the model
# This shows which conditions are confused most often.

from pathlib import Path
import pandas as pd
import joblib
import matplotlib.pyplot as plt

from sklearn.metrics import confusion_matrix

DATA_DIR = Path(r"C:\Users\varsh\patient_drug_nlp\data")
MODEL_DIR = Path(r"C:\Users\varsh\patient_drug_nlp\models")

VALIDATION_FILE = DATA_DIR / "clean_validation_split.csv"
VECTOR_FILE = MODEL_DIR / "clean_tfidf_vectorizer.joblib"
MODEL_FILE = MODEL_DIR / "clean_svm_model.joblib"


def main():
    print("=" * 70)
    print("DRUGSENSE CONFUSION MATRIX")
    print("=" * 70)

    validation = pd.read_csv(VALIDATION_FILE)

    vectorizer = joblib.load(VECTOR_FILE)
    model = joblib.load(MODEL_FILE)

    print("\n🔍 Creating predictions...")

    X_validation = vectorizer.transform(
        validation["review"]
    )

    predictions = model.predict(X_validation)

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
        DATA_DIR / "confusion_matrix.csv"
    )

    print("\n💾 Saved: data\\confusion_matrix.csv")

    print("\n📊 Creating image...")

    plt.figure(figsize=(18, 16))
    plt.imshow(matrix)
    plt.xlabel("Predicted Condition")
    plt.ylabel("Actual Condition")
    plt.title("DrugSense Confusion Matrix")
    plt.tight_layout()

    plt.savefig(
        DATA_DIR / "confusion_matrix.png",
        dpi=200
    )

    plt.close()

    print("💾 Saved: data\\confusion_matrix.png")

    print("\n" + "=" * 70)
    print("CONFUSION MATRIX COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()