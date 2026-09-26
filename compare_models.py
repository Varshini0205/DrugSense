# Step 16: Compare the models we trained.
# This shows their results side by side.

import pandas as pd


def main():
    print("=" * 70)
    print("DRUGSENSE MODEL COMPARISON")
    print("=" * 70)

    results = pd.DataFrame(
        [
            {
                "Model": "Logistic Regression",
                "Accuracy": 0.6360,
                "Macro F1": 0.0907,
                "Weighted F1": 0.5794,
            },
            {
                "Model": "Linear SVM",
                "Accuracy": 0.8129,
                "Macro F1": 0.5610,
                "Weighted F1": 0.8015,
            },
        ]
    )

    print("\n📊 RESULTS")
    print(results.to_string(index=False))

    results.to_csv(
        "model_comparison.csv",
        index=False,
    )

    print("\n💾 Saved:")
    print("model_comparison.csv")

    print("\n" + "=" * 70)
    print("MODEL COMPARISON COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()