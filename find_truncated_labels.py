# Find condition names that look cut off.
# This avoids changing valid medical labels.

from pathlib import Path
import pandas as pd

DATA_DIR = Path(r"C:\Users\varsh\patient_drug_nlp\data")

TRAIN_FILE = DATA_DIR / "clean_train_split.csv"
VALIDATION_FILE = DATA_DIR / "clean_validation_split.csv"


def main():
    print("=" * 70)
    print("DRUGSENSE TRUNCATED LABEL CHECK")
    print("=" * 70)

    train = pd.read_csv(TRAIN_FILE)
    validation = pd.read_csv(VALIDATION_FILE)

    conditions = sorted(
        set(train["condition"]) |
        set(validation["condition"])
    )

    suspicious_endings = [
        "Disorde",
        "Feve",
        "Cance",
        "Zoste",
        "Ulce",
        "Carcinom",
        "Glomerulosclerosis",
        "ibromyalgia",
        "amilial",
        "cal Segmental",
        "unctional",
    ]

    found = []

    for condition in conditions:
        if any(
            condition.endswith(word)
            or condition.startswith(word)
            or word.lower() in condition.lower()
            for word in suspicious_endings
        ):
            found.append(condition)

    print("\n🔍 POSSIBLE TRUNCATED LABELS")

    for condition in found:
        train_count = (
            train["condition"] == condition
        ).sum()

        validation_count = (
            validation["condition"] == condition
        ).sum()

        print(
            f"{condition:<45} "
            f"Train: {train_count:>5}   "
            f"Validation: {validation_count:>5}"
        )

    print(f"\n📊 Possible truncated labels: {len(found)}")

    print("\n" + "=" * 70)
    print("TRUNCATED LABEL CHECK COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()