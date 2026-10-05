# Step 7: Inspect reviews that have multiple condition labels.
# This script only analyzes the data; it does NOT modify any dataset files.

from pathlib import Path
import pandas as pd

DATA_DIR = Path(r"C:\Users\varsh\patient_drug_nlp\data")

TRAIN_FILE = DATA_DIR / "final_train.csv"
TEST_FILE = DATA_DIR / "final_test.csv"


def main():
    print("=" * 70)
    print("DRUGSENSE CONFLICTING REVIEW LABEL INSPECTION")
    print("=" * 70)

    train = pd.read_csv(TRAIN_FILE)
    test = pd.read_csv(TEST_FILE)

    # Combine train and test only for inspection.
    combined = pd.concat(
        [
            train[["uniqueID", "review", "condition", "drugName"]],
            test[["uniqueID", "review", "condition", "drugName"]],
        ],
        ignore_index=True,
    )

    # Find reviews associated with more than one condition.
    condition_counts = (
        combined.groupby("review")["condition"]
        .nunique()
    )

    conflicting_reviews = condition_counts[
        condition_counts > 1
    ].index

    conflicts = combined[
        combined["review"].isin(conflicting_reviews)
    ].copy()

    print(f"\nTotal conflicting reviews: {len(conflicting_reviews):,}")

    print("\n📋 FIRST 20 CONFLICTING REVIEWS")
    print("=" * 70)

    for i, review in enumerate(conflicting_reviews[:20], start=1):
        rows = conflicts[conflicts["review"] == review]

        print(f"\n{'-' * 70}")
        print(f"Conflict #{i}")
        print(f"Review: {review[:500]}")

        print("\nAssociated records:")
        print(
            rows[
                ["uniqueID", "condition", "drugName"]
            ].to_string(index=False)
        )

    print("\n" + "=" * 70)
    print("CONFLICT INSPECTION COMPLETE")
    print("=" * 70)

    print("\n⚠️ No files were modified.")


if __name__ == "__main__":
    main()