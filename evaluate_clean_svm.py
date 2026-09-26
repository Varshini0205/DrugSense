# Step 24: Check the clean SVM by condition.
# This shows which conditions are easy or difficult.

from pathlib import Path
import pandas as pd
import joblib

from sklearn.metrics import classification_report

DATA_DIR = Path(r"C:\Users\varsh\patient_drug_nlp\data")
MODEL_DIR = Path(r"C:\Users\varsh\patient_drug_nlp\models")

VALIDATION_FILE = DATA_DIR / "clean_validation_split.csv"

VECTOR_FILE = MODEL_DIR / "clean_tfidf_vectorizer.joblib"
MODEL_FILE = MODEL_DIR / "clean_svm_model.joblib"

OUTPUT_FILE = Path(
    r"C:\Users\varsh\patient_drug_nlp\clean_svm_report.csv"
)


def main():
    print("=" * 70)
    print("DRUGSENSE CLEAN SVM EVALUATION")
    print("=" * 70)

    validation = pd.read_csv(VALIDATION_FILE)

    vectorizer = joblib.load(VECTOR_FILE)
    model = joblib.load(MODEL_FILE)

    print("\n🔍 Checking validation data...")

    X_validation = vectorizer.transform(
        validation["review"]
    )

    predictions = model.predict(X_validation)

    report = classification_report(
        validation["condition"],
        predictions,
        output_dict=True,
        zero_division=0,
    )

    report_df = pd.DataFrame(report).transpose()

    report_df.to_csv(
        OUTPUT_FILE,
        encoding="utf-8",
    )

    condition_report = report_df.loc[
        ~report_df.index.isin(
            ["accuracy", "macro avg", "weighted avg"]
        )
    ].copy()

    print("\n🏆 BEST 10 CONDITIONS")

    print(
        condition_report
        .sort_values("f1-score", ascending=False)
        .head(10)
        .to_string()
    )

    print("\n⚠️ LOWEST 10 CONDITIONS")

    print(
        condition_report
        .sort_values("f1-score", ascending=True)
        .head(10)
        .to_string()
    )

    print("\n💾 Saved:")
    print(OUTPUT_FILE)

    print("\n" + "=" * 70)
    print("CLEAN SVM EVALUATION COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()