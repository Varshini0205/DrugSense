# Step 12: Make a training set and a checking set.
# Very rare conditions are kept in the training set.

from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split

DATA_DIR = Path(r"C:\Users\varsh\patient_drug_nlp\data")

TRAIN_FILE = DATA_DIR / "text_train.csv"

OUTPUT_TRAIN = DATA_DIR / "train_split.csv"
OUTPUT_VALIDATION = DATA_DIR / "validation_split.csv"


def main():
    print("=" * 70)
    print("DRUGSENSE TRAINING DATA SPLIT")
    print("=" * 70)

    data = pd.read_csv(TRAIN_FILE)

    print(f"\nOriginal rows: {len(data):,}")

    condition_counts = data["condition"].value_counts()

    # Conditions with only one review cannot be split safely.
    rare_conditions = condition_counts[
        condition_counts < 2
    ].index

    common_data = data[
        ~data["condition"].isin(rare_conditions)
    ].copy()

    rare_data = data[
        data["condition"].isin(rare_conditions)
    ].copy()

    print(f"Rare-condition rows kept in training: {len(rare_data):,}")
    print(f"Rows available for splitting: {len(common_data):,}")

    train_data, validation_data = train_test_split(
        common_data,
        test_size=0.20,
        random_state=42,
        stratify=common_data["condition"],
    )

    # Put very rare conditions back into training.
    train_data = pd.concat(
        [train_data, rare_data],
        ignore_index=True,
    )

    train_data = train_data.sample(
        frac=1,
        random_state=42,
    ).reset_index(drop=True)

    validation_data = validation_data.reset_index(drop=True)

    train_data.to_csv(
        OUTPUT_TRAIN,
        index=False,
        encoding="utf-8",
    )

    validation_data.to_csv(
        OUTPUT_VALIDATION,
        index=False,
        encoding="utf-8",
    )

    print("\n📊 FINAL SPLIT")
    print(f"Training rows  : {len(train_data):,}")
    print(f"Validation rows: {len(validation_data):,}")

    print("\n💾 SAVED")
    print(OUTPUT_TRAIN)
    print(OUTPUT_VALIDATION)

    print("\n" + "=" * 70)
    print("DATA SPLIT COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()