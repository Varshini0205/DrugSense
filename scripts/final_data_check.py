# Step 9: Check the final data before training the model.
# This makes sure everything is ready.

from pathlib import Path
import pandas as pd

DATA_DIR = Path(r"C:\Users\varsh\patient_drug_nlp\data")

TRAIN_FILE = DATA_DIR / "model_train.csv"
TEST_FILE = DATA_DIR / "model_test.csv"


def main():
    print("=" * 70)
    print("DRUGSENSE FINAL DATA CHECK")
    print("=" * 70)

    train = pd.read_csv(TRAIN_FILE)
    test = pd.read_csv(TEST_FILE)

    print("\n📊 DATA SIZE")
    print(f"Train rows: {len(train):,}")
    print(f"Test rows : {len(test):,}")

    print("\n📋 COLUMNS")
    print("Train:", list(train.columns))
    print("Test :", list(test.columns))

    print("\n❓ MISSING VALUES IN TRAIN")
    print(train.isna().sum())

    print("\n❓ MISSING VALUES IN TEST")
    print(test.isna().sum())

    print("\n🏷️ CONDITIONS")
    print(f"Train conditions: {train['condition'].nunique():,}")
    print(f"Test conditions : {test['condition'].nunique():,}")

    print("\n⭐ TOP 10 CONDITIONS")
    print(
        train["condition"]
        .value_counts()
        .head(10)
        .to_string()
    )

    print("\n📝 REVIEW LENGTH")
    train_lengths = train["review"].astype(str).str.len()

    print(f"Shortest review: {train_lengths.min()}")
    print(f"Longest review : {train_lengths.max()}")
    print(f"Average length : {train_lengths.mean():.2f}")

    print("\n" + "=" * 70)
    print("FINAL DATA CHECK COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()