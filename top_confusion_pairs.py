# Find the most common model mistakes.
# This makes the confusion matrix easier to understand.

from pathlib import Path
import pandas as pd

DATA_DIR = Path(r"C:\Users\varsh\patient_drug_nlp\data")

MATRIX_FILE = DATA_DIR / "confusion_matrix.csv"


def main():
    print("=" * 70)
    print("DRUGSENSE TOP CONFUSION PAIRS")
    print("=" * 70)

    matrix = pd.read_csv(
        MATRIX_FILE,
        index_col=0
    )

    pairs = []

    for actual in matrix.index:
        for predicted in matrix.columns:

            if actual == predicted:
                continue

            count = matrix.loc[actual, predicted]

            if count > 0:
                pairs.append(
                    {
                        "actual": actual,
                        "predicted": predicted,
                        "count": int(count),
                    }
                )

    result = pd.DataFrame(pairs)

    result = result.sort_values(
        "count",
        ascending=False
    )

    print("\n🔍 TOP 30 CONFUSION PAIRS")

    for _, row in result.head(30).iterrows():
        print(
            f"{row['actual']:<35} "
            f"→ {row['predicted']:<35} "
            f"{row['count']:>4}"
        )

    result.to_csv(
        DATA_DIR / "top_confusion_pairs.csv",
        index=False
    )

    print("\n💾 Saved: data\\top_confusion_pairs.csv")

    print("\n" + "=" * 70)
    print("CONFUSION PAIR ANALYSIS COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()