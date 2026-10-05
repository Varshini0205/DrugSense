# Step 27: Find the most common mistakes.
# This shows which conditions are confused most often.

from pathlib import Path
import pandas as pd

DATA_DIR = Path(r"C:\Users\varsh\patient_drug_nlp\data")

ERROR_FILE = DATA_DIR / "model_errors.csv"


def main():
    print("=" * 70)
    print("DRUGSENSE COMMON MODEL ERRORS")
    print("=" * 70)

    errors = pd.read_csv(ERROR_FILE)

    pairs = (
        errors
        .groupby(["condition", "prediction"])
        .size()
        .reset_index(name="count")
        .sort_values("count", ascending=False)
    )

    print("\n🔍 TOP 20 CONFUSION PAIRS")

    for _, row in pairs.head(20).iterrows():
        print(
            f"{row['condition']:<35} "
            f"→ {row['prediction']:<35} "
            f"{row['count']:>4}"
        )

    pairs.to_csv(
        DATA_DIR / "error_pairs.csv",
        index=False
    )

    print("\n💾 Saved: data\\error_pairs.csv")

    print("\n" + "=" * 70)
    print("ERROR ANALYSIS COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()