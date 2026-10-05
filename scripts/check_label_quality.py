# Check condition names for possible problems.
# This helps us find broken or inconsistent labels.

from pathlib import Path
import pandas as pd

DATA_DIR = Path(r"C:\Users\varsh\patient_drug_nlp\data")

TRAIN_FILE = DATA_DIR / "clean_train_split.csv"
VALIDATION_FILE = DATA_DIR / "clean_validation_split.csv"


def main():
    print("=" * 70)
    print("DRUGSENSE CONDITION LABEL QUALITY CHECK")
    print("=" * 70)

    train = pd.read_csv(TRAIN_FILE)
    validation = pd.read_csv(VALIDATION_FILE)

    all_conditions = sorted(
        set(train["condition"]) |
        set(validation["condition"])
    )

    suspicious_words = [
        "Disorde",
        "ibromyalgia",
        "Othe",
        "min /",
        "mis",
        "eve",
        "ge (",
        "me",
        "Pe",
        "Gas",
    ]

    print("\n🔍 POSSIBLE LABEL PROBLEMS")

    found = []

    for condition in all_conditions:
        for word in suspicious_words:
            if word.lower() in condition.lower():
                found.append(condition)
                break

    for condition in found:
        train_count = (
            train["condition"] == condition
        ).sum()

        validation_count = (
            validation["condition"] == condition
        ).sum()

        print(
            f"{condition:<40} "
            f"Train: {train_count:>5}   "
            f"Validation: {validation_count:>5}"
        )

    print(f"\n📊 Possible problem labels: {len(found)}")

    print("\n" + "=" * 70)
    print("LABEL QUALITY CHECK COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()