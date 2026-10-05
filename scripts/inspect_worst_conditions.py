# Step 29: Check the hardest conditions.
# This shows what the model predicts instead.

from pathlib import Path
import pandas as pd

DATA_DIR = Path(r"C:\Users\varsh\patient_drug_nlp\data")

ERROR_RATE_FILE = DATA_DIR / "condition_error_rates.csv"
ERROR_FILE = DATA_DIR / "model_errors.csv"


def main():
    print("=" * 70)
    print("DRUGSENSE HARDEST CONDITIONS")
    print("=" * 70)

    rates = pd.read_csv(ERROR_RATE_FILE)
    errors = pd.read_csv(ERROR_FILE)

    rates = rates[
        rates["total_reviews"] >= 20
    ].head(10)

    print("\n🔍 TOP 10 HARD CONDITIONS")

    for _, row in rates.iterrows():
        condition = row["condition"]

        condition_errors = errors[
            errors["condition"] == condition
        ]

        predictions = (
            condition_errors["prediction"]
            .value_counts()
            .head(3)
        )

        print(f"\nActual condition: {condition}")
        print(
            f"Reviews: {row['total_reviews']} | "
            f"Error rate: {row['error_rate']:.2%}"
        )

        print("Common wrong predictions:")

        for prediction, count in predictions.items():
            print(f"  → {prediction}: {count}")

    print("\n" + "=" * 70)
    print("HARD CONDITION CHECK COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()