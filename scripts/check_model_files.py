# Check that all model files are ready.
# This makes sure the Flask app can load them.

from pathlib import Path


MODEL_DIR = Path(r"C:\Users\varsh\patient_drug_nlp\models")


REQUIRED_FILES = [
    "fixed_tfidf_vectorizer.joblib",
    "fixed_svm_model.joblib",
]


def main():
    print("=" * 70)
    print("DRUGSENSE MODEL FILE CHECK")
    print("=" * 70)

    all_ready = True

    print("\n🔍 Checking model files...\n")

    for filename in REQUIRED_FILES:
        file_path = MODEL_DIR / filename

        if file_path.exists():
            size_mb = file_path.stat().st_size / (1024 * 1024)

            print(
                f"✅ {filename:<40} "
                f"{size_mb:.2f} MB"
            )
        else:
            print(
                f"❌ {filename:<40} "
                f"NOT FOUND"
            )

            all_ready = False

    print("\n" + "-" * 70)

    if all_ready:
        print("✅ All model files are ready.")
    else:
        print("❌ Some model files are missing.")

    print("\n" + "=" * 70)
    print("MODEL FILE CHECK COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()