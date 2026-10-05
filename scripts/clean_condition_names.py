# Step 20: Remove clearly broken condition names.
# We keep real condition names unchanged.

from pathlib import Path
import re
import pandas as pd

DATA_DIR = Path(r"C:\Users\varsh\patient_drug_nlp\data")

TRAIN_FILE = DATA_DIR / "train_split.csv"
VALIDATION_FILE = DATA_DIR / "validation_split.csv"

OUTPUT_TRAIN = DATA_DIR / "clean_train_split.csv"
OUTPUT_VALIDATION = DATA_DIR / "clean_validation_split.csv"


def is_bad_condition(condition):
    text = str(condition).strip()

    # Remove broken HTML/comment text.
    if "</span>" in text:
        return True

    if "users found this comment" in text.lower():
        return True

    # Remove very short broken names.
    if text in {"Gas", "Pe", "eve", "ge", "me", "mis"}:
        return True

    # Remove known broken starts from damaged names.
    if text.startswith("ge "):
        return True

    if text.startswith("min "):
        return True

    return False


def clean_file(input_file, output_file):
    data = pd.read_csv(input_file)

    before = len(data)

    bad_rows = data["condition"].apply(is_bad_condition)

    removed = bad_rows.sum()

    data = data[~bad_rows].copy()
    data = data.reset_index(drop=True)

    data.to_csv(
        output_file,
        index=False,
        encoding="utf-8",
    )

    print(f"\nFile: {input_file.name}")
    print(f"Rows before: {before:,}")
    print(f"Rows removed: {removed:,}")
    print(f"Rows after : {len(data):,}")

    return data


def main():
    print("=" * 70)
    print("DRUGSENSE CONDITION NAME CLEANING")
    print("=" * 70)

    train = clean_file(
        TRAIN_FILE,
        OUTPUT_TRAIN,
    )

    validation = clean_file(
        VALIDATION_FILE,
        OUTPUT_VALIDATION,
    )

    print("\n📊 CONDITIONS LEFT")
    print(f"Train: {train['condition'].nunique():,}")
    print(f"Validation: {validation['condition'].nunique():,}")

    print("\n💾 SAVED")
    print(OUTPUT_TRAIN)
    print(OUTPUT_VALIDATION)

    print("\n" + "=" * 70)
    print("CONDITION CLEANING COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()