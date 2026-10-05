from pathlib import Path
import html
import re

import pandas as pd


PROJECT_ROOT = Path(r"C:\Users\varsh\patient_drug_nlp")
DATA_DIR = PROJECT_ROOT / "data"

TRAIN_FILE = DATA_DIR / "drugsComTrain_raw.csv"
TEST_FILE = DATA_DIR / "drugsComTest_raw.csv"

CLEAN_TRAIN_FILE = DATA_DIR / "clean_train.csv"
CLEAN_TEST_FILE = DATA_DIR / "clean_test.csv"


def clean_text(text):
    """Clean review text without destroying medical meaning."""
    if pd.isna(text):
        return ""

    text = str(text)

    # Decode HTML entities such as &#039; and &amp;
    text = html.unescape(text)

    # Normalize line breaks and tabs.
    text = text.replace("\r", " ")
    text = text.replace("\n", " ")
    text = text.replace("\t", " ")

    # Collapse repeated whitespace.
    text = re.sub(r"\s+", " ", text)

    return text.strip()


def clean_condition(condition):
    """Clean condition labels while preserving their meaning."""
    if pd.isna(condition):
        return None

    condition = html.unescape(str(condition))

    condition = condition.replace("\r", " ")
    condition = condition.replace("\n", " ")
    condition = condition.replace("\t", " ")

    condition = re.sub(r"\s+", " ", condition)

    condition = condition.strip()

    if not condition:
        return None

    return condition


def clean_drug_name(drug_name):
    """Clean drug names without changing their identity."""
    if pd.isna(drug_name):
        return ""

    drug_name = html.unescape(str(drug_name))

    drug_name = re.sub(r"\s+", " ", drug_name)

    return drug_name.strip()


def clean_dataframe(df):
    """Apply safe cleaning operations."""
    df = df.copy()

    original_rows = len(df)

    # Remove records without a target condition.
    df = df[df["condition"].notna()].copy()

    removed_missing_condition = original_rows - len(df)

    # Clean text/label fields.
    df["review"] = df["review"].apply(clean_text)
    df["condition"] = df["condition"].apply(clean_condition)
    df["drugName"] = df["drugName"].apply(clean_drug_name)

    # Remove rows where condition became empty.
    before_empty_condition_removal = len(df)

    df = df[
        df["condition"].notna()
        & (df["condition"].str.len() > 0)
    ].copy()

    removed_empty_condition = (
        before_empty_condition_removal - len(df)
    )

    # Remove rows with empty reviews.
    before_empty_review_removal = len(df)

    df = df[df["review"].str.len() > 0].copy()

    removed_empty_reviews = (
        before_empty_review_removal - len(df)
    )

    # Remove exact duplicate rows only.
    before_duplicate_removal = len(df)

    df = df.drop_duplicates().copy()

    removed_duplicate_rows = (
        before_duplicate_removal - len(df)
    )

    # Reset index.
    df = df.reset_index(drop=True)

    statistics = {
        "original_rows": original_rows,
        "removed_missing_condition": removed_missing_condition,
        "removed_empty_condition": removed_empty_condition,
        "removed_empty_reviews": removed_empty_reviews,
        "removed_duplicate_rows": removed_duplicate_rows,
        "final_rows": len(df),
    }

    return df, statistics


def process_file(input_file, output_file):
    print("\n" + "=" * 70)
    print(f"PROCESSING: {input_file.name}")
    print("=" * 70)

    if not input_file.exists():
        raise FileNotFoundError(
            f"Dataset not found: {input_file}"
        )

    df = pd.read_csv(input_file)

    print(f"\nOriginal rows: {len(df):,}")

    cleaned_df, stats = clean_dataframe(df)

    print("\nCleaning results:")
    print(
        f"Removed missing condition : "
        f"{stats['removed_missing_condition']:,}"
    )
    print(
        f"Removed empty condition   : "
        f"{stats['removed_empty_condition']:,}"
    )
    print(
        f"Removed empty reviews     : "
        f"{stats['removed_empty_reviews']:,}"
    )
    print(
        f"Removed exact duplicates  : "
        f"{stats['removed_duplicate_rows']:,}"
    )
    print(
        f"Final rows                : "
        f"{stats['final_rows']:,}"
    )

    cleaned_df.to_csv(
        output_file,
        index=False,
        encoding="utf-8"
    )

    print(f"\nSaved to:")
    print(output_file)

    return cleaned_df


def main():
    print("=" * 70)
    print("DRUGSENSE DATA CLEANING")
    print("=" * 70)

    print("\nRaw files will NOT be modified.")

    train_df = process_file(
        TRAIN_FILE,
        CLEAN_TRAIN_FILE
    )

    test_df = process_file(
        TEST_FILE,
        CLEAN_TEST_FILE
    )

    print("\n" + "=" * 70)
    print("CLEANING COMPLETE")
    print("=" * 70)

    print("\nClean training shape:")
    print(train_df.shape)

    print("\nClean test shape:")
    print(test_df.shape)

    print("\nClean training columns:")
    print(list(train_df.columns))

    print("\nClean test columns:")
    print(list(test_df.columns))


if __name__ == "__main__":
    main()