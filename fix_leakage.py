from pathlib import Path
import pandas as pd

DATA_DIR = Path(r"C:\Users\varsh\patient_drug_nlp\data")

TRAIN_FILE = DATA_DIR / "clean_train.csv"
TEST_FILE = DATA_DIR / "clean_test.csv"

FINAL_TRAIN_FILE = DATA_DIR / "final_train.csv"
FINAL_TEST_FILE = DATA_DIR / "final_test.csv"


def main():
    print("=" * 70)
    print("DRUGSENSE TRAIN/TEST LEAKAGE FIX")
    print("=" * 70)

    train = pd.read_csv(TRAIN_FILE)
    test = pd.read_csv(TEST_FILE)

    print(f"\nOriginal train rows: {len(train):,}")
    print(f"Original test rows : {len(test):,}")

    # Normalize review text only for comparison.
    train["_review_key"] = (
        train["review"]
        .fillna("")
        .astype(str)
        .str.strip()
    )

    test["_review_key"] = (
        test["review"]
        .fillna("")
        .astype(str)
        .str.strip()
    )

    train_review_keys = set(train["_review_key"])

    # Remove test reviews that already occur in training data.
    test_before = len(test)

    test = test[
        ~test["_review_key"].isin(train_review_keys)
    ].copy()

    removed_from_test = test_before - len(test)

    # Remove helper columns.
    train = train.drop(columns=["_review_key"])
    test = test.drop(columns=["_review_key"])

    train = train.reset_index(drop=True)
    test = test.reset_index(drop=True)

    # Save final datasets.
    train.to_csv(FINAL_TRAIN_FILE, index=False, encoding="utf-8")
    test.to_csv(FINAL_TEST_FILE, index=False, encoding="utf-8")

    print("\n🔧 LEAKAGE REMOVAL")
    print(f"Duplicate reviews removed from test: {removed_from_test:,}")

    print("\n📊 FINAL DATASET SIZE")
    print(f"Final train rows: {len(train):,}")
    print(f"Final test rows : {len(test):,}")

    print("\n💾 SAVED FILES")
    print(FINAL_TRAIN_FILE)
    print(FINAL_TEST_FILE)

    print("\n" + "=" * 70)
    print("LEAKAGE FIX COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()