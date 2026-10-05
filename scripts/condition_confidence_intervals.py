# Confidence intervals for condition errors
# This shows the uncertainty around each error rate.

from pathlib import Path
import pandas as pd
from statsmodels.stats.proportion import proportion_confint

DATA_DIR = Path(r"C:\Users\varsh\patient_drug_nlp\data")

ERROR_RATE_FILE = DATA_DIR / "condition_error_rates.csv"


def main():
    print("=" * 70)
    print("DRUGSENSE ERROR RATE CONFIDENCE INTERVALS")
    print("=" * 70)

    data = pd.read_csv(ERROR_RATE_FILE)

    data = data[
        data["total_reviews"] >= 50
    ].copy()

    intervals = data.apply(
        lambda row: proportion_confint(
            row["wrong_predictions"],
            row["total_reviews"],
            alpha=0.05,
            method="wilson"
        ),
        axis=1
    )

    data["lower_95"] = [
        value[0] for value in intervals
    ]

    data["upper_95"] = [
        value[1] for value in intervals
    ]

    data = data.sort_values(
        "error_rate",
        ascending=False
    )

    print("\n🔎 CONDITIONS WITH 50+ REVIEWS")

    for _, row in data.head(20).iterrows():
        print(
            f"{row['condition']:<35} "
            f"Reviews: {row['total_reviews']:>5}   "
            f"Error: {row['error_rate']:.2%}   "
            f"95% CI: "
            f"{row['lower_95']:.2%} - "
            f"{row['upper_95']:.2%}"
        )

    data.to_csv(
        DATA_DIR / "condition_error_confidence.csv",
        index=False
    )

    print(
        "\n💾 Saved: "
        "data\\condition_error_confidence.csv"
    )

    print("\n" + "=" * 70)
    print("CONFIDENCE INTERVAL ANALYSIS COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()