# Step 19: Find messy condition names.
# We will inspect them before removing anything.

from pathlib import Path
import pandas as pd

DATA_DIR = Path(r"C:\Users\varsh\patient_drug_nlp\data")

TRAIN_FILE = DATA_DIR / "train_split.csv"


def main():
    print("=" * 70)
    print("DRUGSENSE CONDITION NAME CHECK")
    print("=" * 70)

    data = pd.read_csv(TRAIN_FILE)

    conditions = sorted(
        data["condition"]
        .dropna()
        .unique()
    )

    print(f"\nTotal condition names: {len(conditions):,}")

    print("\n🔎 POSSIBLY MESSY NAMES")

    suspicious = []

    for condition in conditions:
        text = str(condition)

        if (
            "</span>" in text
            or "<span" in text
            or "users found this comment" in text
            or text.startswith("ge ")
            or text.startswith("min ")
            or len(text.strip()) < 4
        ):
            suspicious.append(condition)

    print(f"Found: {len(suspicious):,}")

    for condition in suspicious:
        count = (
            data["condition"] == condition
        ).sum()

        print(f"{count:5,}  {condition}")

    print("\n" + "=" * 70)
    print("CONDITION NAME CHECK COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()