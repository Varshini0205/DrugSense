# Fix only labels that are clearly cut off.
# This avoids changing valid condition names.

from pathlib import Path
import pandas as pd

DATA_DIR = Path(r"C:\Users\varsh\patient_drug_nlp\data")

TRAIN_FILE = DATA_DIR / "clean_train_split.csv"
VALIDATION_FILE = DATA_DIR / "clean_validation_split.csv"

LABEL_MAP = {
    "Bipolar Disorde": "Bipolar Disorder",
    "Major Depressive Disorde": "Major Depressive Disorder",
    "Generalized Anxiety Disorde": "Generalized Anxiety Disorder",
    "Post Traumatic Stress Disorde": "Post Traumatic Stress Disorder",
    "Panic Disorde": "Panic Disorder",
    "Obsessive Compulsive Disorde": "Obsessive Compulsive Disorder",
    "Borderline Personality Disorde": "Borderline Personality Disorder",
    "Social Anxiety Disorde": "Social Anxiety Disorder",
    "Schizoaffective Disorde": "Schizoaffective Disorder",
    "Seasonal Affective Disorde": "Seasonal Affective Disorder",
    "Shift Work Sleep Disorde": "Shift Work Sleep Disorder",
    "Persistent Depressive Disorde": "Persistent Depressive Disorder",
    "Premenstrual Dysphoric Disorde": "Premenstrual Dysphoric Disorder",
    "Herpes Zoste": "Herpes Zoster",
    "Breast Cance": "Breast Cancer",
    "Endometrial Cance": "Endometrial Cancer",
    "Gastric Cance": "Gastric Cancer",
    "Ovarian Cance": "Ovarian Cancer",
    "Pancreatic Cance": "Pancreatic Cancer",
    "Prostate Cance": "Prostate Cancer",
    "Skin Cance": "Skin Cancer",
    "Stomach Cance": "Stomach Cancer",
    "Thyroid Cance": "Thyroid Cancer",
    "Typhoid Feve": "Typhoid Fever",
    "amilial Mediterranean Feve": "Familial Mediterranean Fever",
    "amilial Cold Autoinflammatory Syndrome": "Familial Cold Autoinflammatory Syndrome",
    "ibromyalgia": "Fibromyalgia",
    "cal Segmental Glomerulosclerosis": "Focal Segmental Glomerulosclerosis",
    "unctional Gastric Disorde": "Functional Gastric Disorder",
    "m Pain Disorde": "Pain Disorder",
}


def fix_file(input_file, output_file):
    data = pd.read_csv(input_file)

    data["condition"] = (
        data["condition"]
        .replace(LABEL_MAP)
    )

    data.to_csv(
        output_file,
        index=False
    )


def main():
    print("=" * 70)
    print("DRUGSENSE LABEL CLEANUP")
    print("=" * 70)

    fix_file(
        TRAIN_FILE,
        DATA_DIR / "fixed_train_split.csv"
    )

    fix_file(
        VALIDATION_FILE,
        DATA_DIR / "fixed_validation_split.csv"
    )

    print("\n✅ Label replacements completed.")

    print("\n💾 Saved:")
    print("data\\fixed_train_split.csv")
    print("data\\fixed_validation_split.csv")

    print("\n" + "=" * 70)
    print("LABEL CLEANUP COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()