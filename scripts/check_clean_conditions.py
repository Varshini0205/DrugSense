# Step 22: Check the cleaned condition names.
# This makes sure the bad names are gone.

from pathlib import Path
import pandas as pd

DATA_DIR = Path(r"C:\Users\varsh\patient_drug_nlp\data")

TRAIN_FILE = DATA_DIR / "clean_train_split.csv"
VALIDATION_FILE = DATA_DIR / "clean_validation_split.csv"


def main():
    print("=" * 70)
    print("DRUGSENSE CLEAN CONDITION CHECK")
    print("=" * 70)

    train = pd.read_csv(TRAIN_FILE)
    validation = pd.read_csv(VALIDATION_FILE)

    print("\n📊 DATA SIZE")
    print(f"Train rows      : {len(train):,}")
    print(f"Validation rows : {len(validation):,}")

    print("\n🏷️ CONDITIONS")
    print(f"Train conditions      : {train['condition'].nunique():,}")
    print(f"Validation conditions : {validation['condition'].nunique():,}")

    print("\n🔎 BAD LABEL CHECK")

    bad = train[
        train["condition"]
        .astype(str)
        .str.contains(
            r"</span>|users found this comment|^ge |^min ",
            case=False,
            regex=True,
        )
    ]

    print(f"Bad condition names left: {len(bad):,}")

    print("\n🏆 TOP 10 CONDITIONS")

    print(
        train["condition"]
        .value_counts()
        .head(10)
        .to_string()
    )

    print("\n" + "=" * 70)
    print("CLEAN CONDITION CHECK COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()