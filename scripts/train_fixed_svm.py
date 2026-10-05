# Train the model using the cleaned labels.
# Then we can compare the new results.

from pathlib import Path
import pandas as pd
import joblib

from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score, f1_score


DATA_DIR = Path(r"C:\Users\varsh\patient_drug_nlp\data")
MODEL_DIR = Path(r"C:\Users\varsh\patient_drug_nlp\models")

TRAIN_FILE = DATA_DIR / "fixed_train_split.csv"
VALIDATION_FILE = DATA_DIR / "fixed_validation_split.csv"

VECTOR_FILE = MODEL_DIR / "fixed_tfidf_vectorizer.joblib"
MODEL_FILE = MODEL_DIR / "fixed_svm_model.joblib"


def main():
    print("=" * 70)
    print("DRUGSENSE FIXED SVM MODEL")
    print("=" * 70)

    train = pd.read_csv(TRAIN_FILE)
    validation = pd.read_csv(VALIDATION_FILE)

    vectorizer = joblib.load(VECTOR_FILE)

    print("\n🔍 Preparing data...")

    X_train = vectorizer.transform(train["review"])
    X_validation = vectorizer.transform(validation["review"])

    y_train = train["condition"]
    y_validation = validation["condition"]

    print("\n🤖 Training SVM...")

    model = LinearSVC(
        C=1.0,
        max_iter=1000
    )

    model.fit(
        X_train,
        y_train
    )

    predictions = model.predict(
        X_validation
    )

    accuracy = accuracy_score(
        y_validation,
        predictions
    )

    macro_f1 = f1_score(
        y_validation,
        predictions,
        average="macro",
        zero_division=0
    )

    weighted_f1 = f1_score(
        y_validation,
        predictions,
        average="weighted",
        zero_division=0
    )

    print("\n📊 RESULTS")

    print(
        f"Accuracy    : {accuracy:.4f}"
    )

    print(
        f"Macro F1    : {macro_f1:.4f}"
    )

    print(
        f"Weighted F1 : {weighted_f1:.4f}"
    )

    joblib.dump(
        model,
        MODEL_FILE
    )

    print(
        f"\n💾 Saved: {MODEL_FILE}"
    )

    print("\n" + "=" * 70)
    print("FIXED SVM TRAINING COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()