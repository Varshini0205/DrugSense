# Step 11: Check the cleaned review text.
# This makes sure the text looks correct.

from pathlib import Path
import pandas as pd

DATA_DIR = Path(r"C:\Users\varsh\patient_drug_nlp\data")

TRAIN_FILE = DATA_DIR / "text_train.csv"
TEST_FILE = DATA_DIR / "text_test.csv"


def main():
    print("=" * 70)
    print("DRUGSENSE CLEAN TEXT CHECK")
    print("=" * 70)

    train = pd.read_csv(TRAIN_FILE)
    test = pd.read_csv(TEST_FILE)

    print("\n📊 DATA SIZE")
    print(f"Train rows: {len(train):,}")
    print(f"Test rows : {len(test):,}")

    print("\n❓ EMPTY REVIEWS")
    print(f"Train: {(train['review'].str.strip() == '').sum():,}")
    print(f"Test : {(test['review'].str.strip() == '').sum():,}")

    print("\n📝 SAMPLE REVIEWS")

    for i in range(5):
        print(f"\nReview {i + 1}:")
        print(train["review"].iloc[i][:300])

    print("\n📏 REVIEW LENGTH")

    lengths = train["review"].str.len()

    print(f"Shortest: {lengths.min()}")
    print(f"Longest : {lengths.max()}")
    print(f"Average : {lengths.mean():.2f}")

    print("\n" + "=" * 70)
    print("TEXT CHECK COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()