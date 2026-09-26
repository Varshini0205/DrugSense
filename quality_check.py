from pathlib import Path
import pandas as pd


DATA_DIR = Path(r"C:\Users\varsh\patient_drug_nlp\data")

TRAIN_FILE = DATA_DIR / "clean_train.csv"
TEST_FILE = DATA_DIR / "clean_test.csv"


def main():
    print("=" * 70)
    print("DRUGSENSE DATASET QUALITY & LEAKAGE CHECK")
    print("=" * 70)

    train = pd.read_csv(TRAIN_FILE)
    test = pd.read_csv(TEST_FILE)

    print("\n📊 DATASET SIZE")
    print(f"Train rows: {len(train):,}")
    print(f"Test rows : {len(test):,}")

    # ---------------------------------------------------------
    # ID OVERLAP
    # ---------------------------------------------------------

    print("\n🔑 UNIQUE ID OVERLAP")

    train_ids = set(train["uniqueID"])
    test_ids = set(test["uniqueID"])

    id_overlap = train_ids.intersection(test_ids)

    print(f"Train unique IDs: {len(train_ids):,}")
    print(f"Test unique IDs : {len(test_ids):,}")
    print(f"Overlapping IDs : {len(id_overlap):,}")

    # ---------------------------------------------------------
    # REVIEW OVERLAP
    # ---------------------------------------------------------

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

    train_review_set = set(train_reviews)
    test_review_set = set(test_reviews)

    review_overlap = train_review_set.intersection(test_review_set)

    print(f"Unique train reviews: {len(train_review_set):,}")
    print(f"Unique test reviews : {len(test_review_set):,}")
    print(f"Overlapping reviews : {len(review_overlap):,}")

    # ---------------------------------------------------------
    # CONDITION OVERLAP
    # ---------------------------------------------------------

    print("\n🏷️ CONDITION LABEL OVERLAP")

    train_conditions = set(train["condition"].dropna().unique())
    test_conditions = set(test["condition"].dropna().unique())

    common_conditions = train_conditions.intersection(
        test_conditions
    )

    train_only = train_conditions - test_conditions
    test_only = test_conditions - train_conditions

    print(f"Train conditions      : {len(train_conditions):,}")
    print(f"Test conditions       : {len(test_conditions):,}")
    print(f"Common conditions     : {len(common_conditions):,}")
    print(f"Train-only conditions : {len(train_only):,}")
    print(f"Test-only conditions  : {len(test_only):,}")

    # ---------------------------------------------------------
    # RARE CONDITIONS
    # ---------------------------------------------------------

    print("\n⚠️ RARE CONDITIONS IN TRAINING DATA")

    condition_counts = train["condition"].value_counts()

    print("\nConditions with fewer than 10 reviews:")
    rare = condition_counts[condition_counts < 10]

    print(f"Number of rare conditions: {len(rare):,}")

    if len(rare) > 0:
        print(rare.head(30).to_string())

    # ---------------------------------------------------------
    # CONDITION DISTRIBUTION
    # ---------------------------------------------------------

    print("\n📈 CONDITION DISTRIBUTION")

    print(f"Most common condition:")
    print(condition_counts.head(10).to_string())

    print("\nLeast common conditions:")
    print(condition_counts.tail(10).to_string())

    # ---------------------------------------------------------
    # DRUG OVERLAP
    # ---------------------------------------------------------

    print("\n💊 DRUG OVERLAP")

    train_drugs = set(train["drugName"].dropna().unique())
    test_drugs = set(test["drugName"].dropna().unique())

    common_drugs = train_drugs.intersection(test_drugs)

    print(f"Train drugs : {len(train_drugs):,}")
    print(f"Test drugs  : {len(test_drugs):,}")
    print(f"Common drugs: {len(common_drugs):,}")

    # ---------------------------------------------------------
    # SAME REVIEW + DIFFERENT CONDITION
    # ---------------------------------------------------------

    print("\n🚨 DUPLICATE REVIEW / LABEL CHECK")

    review_condition_counts = (
        pd.concat(
            [
                train[["review", "condition"]],
                test[["review", "condition"]],
            ],
            ignore_index=True,
        )
        .groupby("review")["condition"]
        .nunique()
    )

    conflicting_reviews = review_condition_counts[
        review_condition_counts > 1
    ]

    print(
        "Reviews associated with multiple conditions: "
        f"{len(conflicting_reviews):,}"
    )

    # ---------------------------------------------------------
    # SUMMARY
    # ---------------------------------------------------------

    print("\n" + "=" * 70)
    print("QUALITY CHECK SUMMARY")
    print("=" * 70)

    if len(id_overlap) == 0:
        print("✅ No uniqueID overlap")
    else:
        print("❌ uniqueID overlap detected")

    if len(review_overlap) == 0:
        print("✅ No train/test review overlap")
    else:
        print(
            f"⚠️ {len(review_overlap):,} identical reviews "
            "appear in both train and test"
        )

    if len(conflicting_reviews) == 0:
        print("✅ No review has multiple condition labels")
    else:
        print(
            f"⚠️ {len(conflicting_reviews):,} reviews "
            "have multiple condition labels"
        )

    print("\nQUALITY CHECK COMPLETE")


if __name__ == "__main__":
    main()