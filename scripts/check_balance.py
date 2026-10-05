# Step 17: Check how many reviews each condition has.
# This helps us understand the data.

from pathlib import Path
import pandas as pd

DATA_DIR = Path(r"C:\Users\varsh\patient_drug_nlp\data")

TRAIN_FILE = DATA_DIR / "train_split.csv"


def main():
    print("=" * 70)
    print("DRUGSENSE CONDITION BALANCE CHECK")
    print("=" * 70)

    train = pd.read_csv(TRAIN_FILE)

    counts = train["condition"].value_counts()

    print(f"\nTotal conditions: {len(counts):,}")

    print("\n📊 CONDITION COUNTS")

    print(f"Most reviews for one condition : {counts.max():,}")
    print(f"Fewest reviews for one condition: {counts.min():,}")
    print(f"Average reviews per condition   : {counts.mean():.2f}")
    print(f"Median reviews per condition    : {counts.median():.0f}")

    print("\n🔎 NUMBER OF CONDITIONS BY SIZE")

    print(f"1 review     : {(counts == 1).sum():,}")
    print(f"2–5 reviews  : {((counts >= 2) & (counts <= 5)).sum():,}")
    print(f"6–10 reviews : {((counts >= 6) & (counts <= 10)).sum():,}")
    print(f"11–50 reviews: {((counts >= 11) & (counts <= 50)).sum():,}")
    print(f"51+ reviews  : {(counts >= 51).sum():,}")

    print("\n🏆 TOP 15 CONDITIONS")

    print(counts.head(15).to_string())

    print("\n⚠️ BOTTOM 15 CONDITIONS")

    print(counts.tail(15).to_string())

    print("\n" + "=" * 70)
    print("BALANCE CHECK COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()