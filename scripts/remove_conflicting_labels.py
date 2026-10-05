# Step 8: Remove training reviews that have multiple condition labels.
# This prevents contradictory labels from being used during model training.

from pathlib import Path
import pandas as pd

DATA_DIR = Path(r"C:\Users\varsh\patient_drug_nlp\data")

TRAIN_FILE = DATA_DIR / "final_train.csv"
TEST_FILE = DATA_DIR / "final_test.csv"

OUTPUT_TRAIN_FILE = DATA_DIR / "model_train.csv"
OUTPUT_TEST_FILE = DATA_DIR / "model_test.csv"


def main():
    print("=" * 70)
    print("DRUGSENSE CONFLICTING LABEL REMOVAL")
    print("=" * 70)

    train = pd.read_csv(TRAIN_FILE)
    test = pd.read_csv(TEST_FILE)

    print(f"\nOriginal train rows: {len(train):,}")
    print(f"Original test rows : {len(test):,}")

    # Find review texts with more than one condition in training data.
    review_condition_counts = (
        train.groupby("review")["condition"]
        .nunique()
    )

    conflicting_reviews = set(
        review_condition_counts[
            review_condition_counts > 1
        ].index
    )

    print(
        f"\nConflicting review texts in training: "
        f"{len(conflicting_reviews):,}"
    )

    # Remove all rows belonging to conflicting review texts.
    train_clean = train[
        ~train["review"].isin(conflicting_reviews)
    ].copy()

    train_clean = train_clean.reset_index(drop=True)
    test_clean = test.reset_index(drop=True)

    removed_rows = len(train) - len(train_clean)

    print(f"Training rows removed: {removed_rows:,}")

    print("\n📊 FINAL MODEL DATASETS")
    print(f"Model train rows: {len(train_clean):,}")
    print(f"Model test rows : {len(test_clean):,}")

    train_clean.to_csv(
        OUTPUT_TRAIN_FILE,
        index=False,
        encoding="utf-8",
    )

    test_clean.to_csv(
        OUTPUT_TEST_FILE,
        index=False,
        encoding="utf-8",
    )

    print("\n💾 SAVED FILES")
    print(OUTPUT_TRAIN_FILE)
    print(OUTPUT_TEST_FILE)

    print("\n" + "=" * 70)
    print("CONFLICT REMOVAL COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()