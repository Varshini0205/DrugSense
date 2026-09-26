# Create the final report for every condition.
# This shows precision, recall, and F1 for each condition.

from pathlib import Path
import pandas as pd
import joblib

from sklearn.metrics import classification_report


DATA_DIR = Path(r"C:\Users\varsh\patient_drug_nlp\data")
MODEL_DIR = Path(r"C:\Users\varsh\patient_drug_nlp\models")

VALIDATION_FILE = DATA_DIR / "fixed_validation_split.csv"
VECTOR_FILE = MODEL_DIR / "fixed_tfidf_vectorizer.joblib"
MODEL_FILE = MODEL_DIR / "fixed_svm_model.joblib"

REPORT_FILE = DATA_DIR / "final_condition_report.csv"


def main():
    print("=" * 70)
    print("DRUGSENSE FINAL CONDITION REPORT")
    print("=" * 70)

    validation = pd.read_csv(
        VALIDATION_FILE
    )

    vectorizer = joblib.load(
        VECTOR_FILE
    )

    model = joblib.load(
        MODEL_FILE
    )

    print("\n🔍 Creating predictions...")

    X_validation = vectorizer.transform(
        validation["review"]
    )

    predictions = model.predict(
        X_validation
    )

    report = classification_report(
        validation["condition"],
        predictions,
        output_dict=True,
        zero_division=0
    )

    report_df = pd.DataFrame(report).transpose()

    report_df.to_csv(
        REPORT_FILE
    )

    print("\n📊 CONDITIONS WITH 20+ REVIEWS")

    condition_report = report_df[
        ~report_df.index.isin(
            ["accuracy", "macro avg", "weighted avg"]
        )
    ].copy()

    condition_report["support"] = (
        condition_report["support"]
        .astype(int)
    )

    condition_report = condition_report[
        condition_report["support"] >= 20
    ]

    condition_report = condition_report.sort_values(
        "f1-score",
        ascending=False
    )

    print(
        condition_report[
            ["precision", "recall", "f1-score", "support"]
        ].head(20).to_string()
    )

    print(
        f"\n📊 Total conditions: "
        f"{len(report_df) - 3:,}"
    )

    print(
        f"📊 Conditions with 20+ reviews: "
        f"{len(condition_report):,}"
    )

    print(
        f"\n💾 Saved: data\\final_condition_report.csv"
    )

    print("\n" + "=" * 70)
    print("FINAL CONDITION REPORT COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()