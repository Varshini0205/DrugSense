# Compare the models using the same validation data.
# This gives us one final results table.

from pathlib import Path
import pandas as pd

DATA_DIR = Path(r"C:\Users\varsh\patient_drug_nlp\data")

results = [
    {
        "Model": "Logistic Regression",
        "Accuracy": 0.6360,
        "Macro F1": 0.0907,
        "Weighted F1": 0.5794,
    },
    {
        "Model": "Original Linear SVM",
        "Accuracy": 0.8129,
        "Macro F1": 0.5610,
        "Weighted F1": 0.8015,
    },
    {
        "Model": "Cleaned Linear SVM",
        "Accuracy": 0.8173,
        "Macro F1": 0.6008,
        "Weighted F1": 0.8083,
    },
]

comparison = pd.DataFrame(results)

print("=" * 70)
print("DRUGSENSE FINAL MODEL COMPARISON")
print("=" * 70)

print("\n📊 RESULTS\n")
print(
    comparison.to_string(
        index=False
    )
)

comparison.to_csv(
    DATA_DIR / "final_model_comparison.csv",
    index=False
)

print("\n💾 Saved: data\\final_model_comparison.csv")

print("\n" + "=" * 70)
print("MODEL COMPARISON COMPLETE")
print("=" * 70)