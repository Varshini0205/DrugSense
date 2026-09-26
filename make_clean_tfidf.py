# Step 21: Make the text numbers again using the clean data.
# This keeps the model training fair.

from pathlib import Path
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

DATA_DIR = Path(r"C:\Users\varsh\patient_drug_nlp\data")
MODEL_DIR = Path(r"C:\Users\varsh\patient_drug_nlp\models")

TRAIN_FILE = DATA_DIR / "clean_train_split.csv"
VALIDATION_FILE = DATA_DIR / "clean_validation_split.csv"

VECTOR_FILE = MODEL_DIR / "clean_tfidf_vectorizer.joblib"


def main():
    print("=" * 70)
    print("DRUGSENSE CLEAN TF-IDF")
    print("=" * 70)

    MODEL_DIR.mkdir(exist_ok=True)

    train = pd.read_csv(TRAIN_FILE)
    validation = pd.read_csv(VALIDATION_FILE)

    print(f"\nTraining rows  : {len(train):,}")
    print(f"Validation rows: {len(validation):,}")

    print("\n🔢 Turning text into numbers...")

    vectorizer = TfidfVectorizer(
        ngram_range=(1, 2),
        min_df=2,
        max_df=0.95,
        sublinear_tf=True,
    )

    train_text = vectorizer.fit_transform(
        train["review"]
    )

    validation_text = vectorizer.transform(
        validation["review"]
    )

    print("\n📊 RESULTS")
    print(f"Training shape  : {train_text.shape}")
    print(f"Validation shape: {validation_text.shape}")
    print(
        f"Number of features: "
        f"{len(vectorizer.vocabulary_):,}"
    )

    joblib.dump(
        vectorizer,
        VECTOR_FILE,
    )

    print("\n💾 SAVED")
    print(VECTOR_FILE)

    print("\n" + "=" * 70)
    print("CLEAN TF-IDF COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()