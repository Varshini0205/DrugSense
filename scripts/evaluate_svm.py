# Step 18: Check the SVM results in more detail.
# This shows how well the model handles each condition.

from pathlib import Path
import pandas as pd
import joblib

from sklearn.metrics import classification_report

DATA_DIR = Path(r"C:\Users\varsh\patient_drug_nlp\data")
MODEL_DIR = Path(r"C:\Users\varsh\patient_drug_nlp\models")

VALIDATION_FILE = DATA_DIR / "validation_split.csv"

VECTOR_FILE = MODEL_DIR / "tfidf_vectorizer.joblib"
MODEL_FILE = MODEL_DIR / "svm_model.joblib"

OUTPUT_FILE = Path(
    r"C:\Users\varsh\patient_drug_nlp\svm_condition_report.csv"
)


def main():
    print("=" * 70)
    print("DRUGSENSE SVM DETAILED EVALUATION")
    print("=" * 70)

    validation = pd.read_csv(VALIDATION_FILE)

    vectorizer = joblib.load(VECTOR_FILE)
    model = joblib.load(MODEL_FILE)

    print("\n🔍 Checking validation data...")

    X_validation = vectorizer.transform(
        validation["review"]
    )

    y_validation = validation["condition"]

    predictions = model.predict(X_validation)

    print("\n📊 Creating condition report...")

    report = classification_report(
        y_validation,
        predictions,
        output_dict=True,
        zero_division=0,
    )

    report_df = pd.DataFrame(report).transpose()

    report_df.to_csv(
        OUTPUT_FILE,
        encoding="utf-8",
    )

    print("\n💾 Saved:")
    print(OUTPUT_FILE)

    print("\n🏆 BEST 15 CONDITIONS BY F1")

    condition_report = report_df.loc[
        ~report_df.index.isin(
            ["accuracy", "macro avg", "weighted avg"]
        )
    ].copy()

    print(
        condition_report
        .sort_values("f1-score", ascending=False)
        .head(15)
        .to_string()
    )

    print("\n⚠️ LOWEST 15 CONDITIONS BY F1")

    print(
        condition_report
        .sort_values("f1-score", ascending=True)
        .head(15)
        .to_string()
    )

    print("\n" + "=" * 70)
    print("SVM EVALUATION COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()