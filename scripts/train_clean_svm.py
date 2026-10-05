# Step 23: Train the SVM again with clean labels.
# This gives us a fairer result.

from pathlib import Path
import pandas as pd
import joblib

from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score, f1_score

DATA_DIR = Path(r"C:\Users\varsh\patient_drug_nlp\data")
MODEL_DIR = Path(r"C:\Users\varsh\patient_drug_nlp\models")

TRAIN_FILE = DATA_DIR / "clean_train_split.csv"
VALIDATION_FILE = DATA_DIR / "clean_validation_split.csv"

VECTOR_FILE = MODEL_DIR / "clean_tfidf_vectorizer.joblib"
MODEL_FILE = MODEL_DIR / "clean_svm_model.joblib"


def main():
    print("=" * 70)
    print("DRUGSENSE CLEAN SVM MODEL")
    print("=" * 70)

    train = pd.read_csv(TRAIN_FILE)
    validation = pd.read_csv(VALIDATION_FILE)

    vectorizer = joblib.load(VECTOR_FILE)

    print("\n🔢 Preparing text...")

    X_train = vectorizer.transform(train["review"])
    X_validation = vectorizer.transform(validation["review"])

    y_train = train["condition"]
    y_validation = validation["condition"]

    print(f"Training shape  : {X_train.shape}")
    print(f"Validation shape: {X_validation.shape}")

    print("\n🤖 Training model...")

    model = LinearSVC(
        C=1.0,
        max_iter=1000,
    )

    model.fit(X_train, y_train)

    print("\n🔍 Checking model...")

    predictions = model.predict(X_validation)

    accuracy = accuracy_score(
        y_validation,
        predictions,
    )

    macro_f1 = f1_score(
        y_validation,
        predictions,
        average="macro",
        zero_division=0,
    )

    weighted_f1 = f1_score(
        y_validation,
        predictions,
        average="weighted",
        zero_division=0,
    )

    print("\n📊 RESULTS")
    print(f"Accuracy   : {accuracy:.4f}")
    print(f"Macro F1   : {macro_f1:.4f}")
    print(f"Weighted F1: {weighted_f1:.4f}")

    joblib.dump(
        model,
        MODEL_FILE,
    )

    print("\n💾 SAVED")
    print(MODEL_FILE)

    print("\n" + "=" * 70)
    print("CLEAN SVM COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()