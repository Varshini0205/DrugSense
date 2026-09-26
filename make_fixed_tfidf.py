# Rebuild TF-IDF using the cleaned labels.
# This keeps the model data consistent.

from pathlib import Path
import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer

DATA_DIR = Path(r"C:\Users\varsh\patient_drug_nlp\data")
MODEL_DIR = Path(r"C:\Users\varsh\patient_drug_nlp\models")

TRAIN_FILE = DATA_DIR / "fixed_train_split.csv"
VALIDATION_FILE = DATA_DIR / "fixed_validation_split.csv"

VECTOR_FILE = MODEL_DIR / "fixed_tfidf_vectorizer.joblib"


def main():
    print("=" * 70)
    print("DRUGSENSE FIXED TF-IDF")
    print("=" * 70)

    train = pd.read_csv(TRAIN_FILE)
    validation = pd.read_csv(VALIDATION_FILE)

    vectorizer = TfidfVectorizer(
        ngram_range=(1, 2),
        min_df=2,
        max_df=0.95,
        sublinear_tf=True
    )

    print("\n🔍 Fitting TF-IDF on training reviews...")

    X_train = vectorizer.fit_transform(
        train["review"]
    )

    X_validation = vectorizer.transform(
        validation["review"]
    )

    print(
        f"\nTrain shape: {X_train.shape}"
    )

    print(
        f"Validation shape: {X_validation.shape}"
    )

    joblib.dump(
        vectorizer,
        VECTOR_FILE
    )

    print(
        f"\n💾 Saved: {VECTOR_FILE}"
    )

    print("\n" + "=" * 70)
    print("FIXED TF-IDF COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()