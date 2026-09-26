# Step 28: Calculate mistakes for each condition.
# This shows which conditions are harder to classify.

from pathlib import Path
import pandas as pd

DATA_DIR = Path(r"C:\Users\varsh\patient_drug_nlp\data")

VALIDATION_FILE = DATA_DIR / "clean_validation_split.csv"
ERROR_FILE = DATA_DIR / "model_errors.csv"


def main():
    print("=" * 70)
    print("DRUGSENSE CONDITION ERROR RATES")
    print("=" * 70)

    validation = pd.read_csv(VALIDATION_FILE)
    errors = pd.read_csv(ERROR_FILE)

    total = (
        validation
        .groupby("condition")
        .size()
        .reset_index(name="total_reviews")
    )

    wrong = (
        errors
        .groupby("condition")
        .size()
        .reset_index(name="wrong_predictions")
    )

    result = total.merge(
        wrong,
        on="condition",
        how="left"
    )

    result["wrong_predictions"] = (
        result["wrong_predictions"]
        .fillna(0)
        .astype(int)
    )

    result["error_rate"] = (
        result["wrong_predictions"]
        / result["total_reviews"]
    )

    result = result.sort_values(
        ["error_rate", "total_reviews"],
        ascending=[False, False]
    )

    print("\n🔍 CONDITIONS WITH AT LEAST 20 REVIEWS")

    filtered = result[
        result["total_reviews"] >= 20
    ]

    for _, row in filtered.head(20).iterrows():
        print(
            f"{row['condition']:<35} "
            f"Reviews: {row['total_reviews']:>5}   "
            f"Errors: {row['wrong_predictions']:>5}   "
            f"Error Rate: {row['error_rate']:.2%}"
        )

    result.to_csv(
        DATA_DIR / "condition_error_rates.csv",
        index=False
    )

    print("\n💾 Saved: data\\condition_error_rates.csv")

    print("\n" + "=" * 70)
    print("ERROR RATE ANALYSIS COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()