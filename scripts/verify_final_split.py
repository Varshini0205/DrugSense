from pathlib import Path
import pandas as pd

DATA_DIR = Path(r"C:\Users\varsh\patient_drug_nlp\data")

TRAIN_FILE = DATA_DIR / "final_train.csv"
TEST_FILE = DATA_DIR / "final_test.csv"


def main():
    print("=" * 70)
    print("DRUGSENSE FINAL SPLIT VERIFICATION")
    print("=" * 70)

    train = pd.read_csv(TRAIN_FILE)
    test = pd.read_csv(TEST_FILE)

    print("\n📊 DATASET SIZE")
    print(f"Train rows: {len(train):,}")
    print(f"Test rows : {len(test):,}")

    print("\n🔑 UNIQUE ID OVERLAP")

    train_ids = set(train["uniqueID"])
    test_ids = set(test["uniqueID"])
    id_overlap = train_ids.intersection(test_ids)

    print(f"Overlapping IDs: {len(id_overlap):,}")

    print("\n📝 REVIEW TEXT OVERLAP")

    train_reviews = (
        train["review"]
        .fillna("")
        .astype(str)
        .str.strip()
    )

    test_reviews = (
        test["review"]
        .fillna("")
        .astype(str)
        .str.strip()
    )

    review_overlap = set(train_reviews).intersection(set(test_reviews))

    print(f"Overlapping reviews: {len(review_overlap):,}")

    print("\n🏷️ CONDITION LABELS")

    train_conditions = set(train["condition"].dropna().unique())
    test_conditions = set(test["condition"].dropna().unique())

    common_conditions = train_conditions.intersection(test_conditions)
    test_only_conditions = test_conditions - train_conditions

    print(f"Train conditions: {len(train_conditions):,}")
    print(f"Test conditions : {len(test_conditions):,}")
    print(f"Common conditions: {len(common_conditions):,}")
    print(f"Test-only conditions: {len(test_only_conditions):,}")

    print("\n🚨 FINAL STATUS")

    if len(id_overlap) == 0:
        print("✅ No uniqueID leakage")
    else:
        print("❌ uniqueID leakage detected")

    if len(review_overlap) == 0:
        print("✅ No review-text leakage")
    else:
        print("❌ Review-text leakage detected")

    print("\n" + "=" * 70)
    print("VERIFICATION COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()