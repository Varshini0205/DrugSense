# Support-aware error analysis
# This compares error rates using enough reviews.

from pathlib import Path
import pandas as pd

DATA_DIR = Path(r"C:\Users\varsh\patient_drug_nlp\data")

ERROR_RATE_FILE = DATA_DIR / "condition_error_rates.csv"


def main():
    print("=" * 70)
    print("DRUGSENSE SUPPORT-AWARE ERROR ANALYSIS")
    print("=" * 70)

    data = pd.read_csv(ERROR_RATE_FILE)

    groups = [
        ("20+ reviews", 20),
        ("50+ reviews", 50),
        ("100+ reviews", 100),
        ("200+ reviews", 200),
    ]

    for name, minimum in groups:
        subset = data[
            data["total_reviews"] >= minimum
        ].copy()

        subset = subset.sort_values(
            "error_rate",
            ascending=False
        )

        print(f"\n🔎 {name}")

        for _, row in subset.head(10).iterrows():
            print(
                f"{row['condition']:<35} "
                f"Reviews: {row['total_reviews']:>5}   "
                f"Errors: {row['wrong_predictions']:>5}   "
                f"Error Rate: {row['error_rate']:.2%}"
            )

    print("\n" + "=" * 70)
    print("SUPPORT-AWARE ANALYSIS COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()