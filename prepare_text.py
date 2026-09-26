# Step 10: Clean the review text for the model.
# This makes the reviews easier for the model to learn from.

from pathlib import Path
import re
import pandas as pd

DATA_DIR = Path(r"C:\Users\varsh\patient_drug_nlp\data")

TRAIN_FILE = DATA_DIR / "model_train.csv"
TEST_FILE = DATA_DIR / "model_test.csv"

OUTPUT_TRAIN_FILE = DATA_DIR / "text_train.csv"
OUTPUT_TEST_FILE = DATA_DIR / "text_test.csv"


def clean_text(text):
    text = str(text)

    # Remove HTML tags.
    text = re.sub(r"<[^>]+>", " ", text)

    # Make everything lowercase.
    text = text.lower()

    # Replace links with a space.
    text = re.sub(r"http\S+|www\S+", " ", text)

    # Keep letters and numbers.
    text = re.sub(r"[^a-z0-9\s]", " ", text)

    # Remove extra spaces.
    text = re.sub(r"\s+", " ", text)

    return text.strip()


def main():
    print("=" * 70)
    print("DRUGSENSE TEXT PREPARATION")
    print("=" * 70)

    train = pd.read_csv(TRAIN_FILE)
    test = pd.read_csv(TEST_FILE)

    print(f"\nTrain rows: {len(train):,}")
    print(f"Test rows : {len(test):,}")

    print("\n🧹 Cleaning review text...")

    train["review"] = train["review"].apply(clean_text)
    test["review"] = test["review"].apply(clean_text)

    # Remove rows that became empty.
    train = train[train["review"].str.len() > 0].copy()
    test = test[test["review"].str.len() > 0].copy()

    train.reset_index(drop=True, inplace=True)
    test.reset_index(drop=True, inplace=True)

    train.to_csv(
        OUTPUT_TRAIN_FILE,
        index=False,
        encoding="utf-8",
    )

    test.to_csv(
        OUTPUT_TEST_FILE,
        index=False,
        encoding="utf-8",
    )

    print("\n📊 FINAL TEXT DATA")
    print(f"Train rows: {len(train):,}")
    print(f"Test rows : {len(test):,}")

    print("\n📝 EXAMPLE")
    print("\nOriginal/cleaned review:")
    print(train["review"].iloc[0][:500])

    print("\n💾 SAVED")
    print(OUTPUT_TRAIN_FILE)
    print(OUTPUT_TEST_FILE)

    print("\n" + "=" * 70)
    print("TEXT PREPARATION COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()