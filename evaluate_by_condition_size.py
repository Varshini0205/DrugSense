# Step 25: Check results for common and rare conditions.
# This shows how review count affects the model.

from pathlib import Path
import pandas as pd
import joblib

from sklearn.metrics import f1_score


DATA_DIR = Path(r"C:\Users\varsh\patient_drug_nlp\data")
MODEL_DIR = Path(r"C:\Users\varsh\patient_drug_nlp\models")

TRAIN_FILE = DATA_DIR / "clean_train_split.csv"
VALIDATION_FILE = DATA_DIR / "clean_validation_split.csv"

VECTOR_FILE = MODEL_DIR / "clean_tfidf_vectorizer.joblib"
MODEL_FILE = MODEL_DIR / "clean_svm_model.joblib"


def get_group(count):
    if count <= 5:
        return "1-5 reviews"
    elif count <= 10:
        return "6-10 reviews"
    elif count <= 50:
        return "11-50 reviews"
    elif count <= 100:
        return "51-100 reviews"
    else:
        return "101+ reviews"


def main():
    print("=" * 70)
    print("DRUGSENSE PERFORMANCE BY CONDITION SIZE")
    print("=" * 70)

    train = pd.read_csv(TRAIN_FILE)
    validation = pd.read_csv(VALIDATION_FILE)

    vectorizer = joblib.load(VECTOR_FILE)
    model = joblib.load(MODEL_FILE)

    condition_counts = train["condition"].value_counts()

    validation["condition_size"] = (
        validation["condition"]
        .map(condition_counts)
    )

    validation["group"] = (
        validation["condition_size"]
        .apply(get_group)
    )

    print("\n🔍 Checking validation data...")

    X_validation = vectorizer.transform(
        validation["review"]
    )

    predictions = model.predict(X_validation)

    validation["prediction"] = predictions

    print("\n📊 RESULTS")

    groups = [
        "1-5 reviews",
        "6-10 reviews",
        "11-50 reviews",
        "51-100 reviews",
        "101+ reviews",
    ]

    for group in groups:
        subset = validation[
            validation["group"] == group
        ]

        if len(subset) == 0:
            continue

        score = f1_score(
            subset["condition"],
            subset["prediction"],
            average="weighted",
            zero_division=0,
        )

        print(
            f"{group:15} "
            f"Reviews: {len(subset):6,}   "
            f"Weighted F1: {score:.4f}"
        )

    print("\n" + "=" * 70)
    print("PERFORMANCE CHECK COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()