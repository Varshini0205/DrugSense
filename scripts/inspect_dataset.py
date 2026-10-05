from pathlib import Path
import pandas as pd

DATA_DIR = Path(r"C:\Users\varsh\patient_drug_nlp\data")

FILES = [
    "drugsComTrain_raw.csv",
    "drugsComTest_raw.csv",
]


def inspect_file(filename):
    path = DATA_DIR / filename

    print("\n" + "=" * 70)
    print(f"FILE: {filename}")
    print("=" * 70)

    if not path.exists():
        print(f"ERROR: File not found: {path}")
        return

    df = pd.read_csv(path)

    print(f"\nRows    : {df.shape[0]:,}")
    print(f"Columns : {df.shape[1]}")

    print("\nColumn names:")
    for column in df.columns:
        print(f"  - {column}")

    print("\nData types:")
    print(df.dtypes.to_string())

    print("\nMissing values:")
    print(df.isna().sum().to_string())

    print("\nDuplicate rows:")
    print(df.duplicated().sum())

    if "uniqueID" in df.columns:
        print("\nDuplicate uniqueID:")
        print(df["uniqueID"].duplicated().sum())

    if "review" in df.columns:
        reviews = df["review"].fillna("").astype(str)

        print("\nDuplicate reviews:")
        print(reviews.duplicated().sum())

        word_counts = reviews.str.split().str.len()

        print("\nReview length:")
        print(f"  Minimum : {word_counts.min()}")
        print(f"  Maximum : {word_counts.max()}")
        print(f"  Mean    : {word_counts.mean():.2f}")
        print(f"  Median  : {word_counts.median():.2f}")

    if "drugName" in df.columns:
        print("\nUnique drugs:")
        print(df["drugName"].nunique())

    if "condition" in df.columns:
        print("\nUnique conditions:")
        print(df["condition"].nunique())

        print("\nTop 20 conditions:")
        print(df["condition"].value_counts().head(20).to_string())

    if "rating" in df.columns:
        print("\nRating:")
        print(f"  Minimum : {df['rating'].min()}")
        print(f"  Maximum : {df['rating'].max()}")
        print(f"  Mean    : {df['rating'].mean():.2f}")

    print("\nFirst 5 rows:")
    print(df.head().to_string())


def main():
    print("=" * 70)
    print("DRUGSENSE DATASET INSPECTION")
    print("=" * 70)

    print(f"\nData directory:")
    print(DATA_DIR)

    for filename in FILES:
        inspect_file(filename)

    print("\n" + "=" * 70)
    print("INSPECTION COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()