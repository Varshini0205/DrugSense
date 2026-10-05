# Organize old project files safely.
# Nothing is permanently deleted.
# Important files stay where they are.

from pathlib import Path
import shutil


PROJECT = Path(__file__).resolve().parent.parent

ARCHIVE_MODELS = PROJECT / "archive" / "models"
ARCHIVE_ANALYSIS = PROJECT / "archive" / "analysis"

ARCHIVE_MODELS.mkdir(parents=True, exist_ok=True)
ARCHIVE_ANALYSIS.mkdir(parents=True, exist_ok=True)


old_models = [
    "tfidf_vectorizer.joblib",
    "logistic_model.joblib",
    "svm_model.joblib",
    "clean_tfidf_vectorizer.joblib",
    "clean_svm_model.joblib",
]


old_analysis = [
    "model_comparison.csv",
    "clean_svm_report.csv",
    "model_errors.csv",
    "error_pairs.csv",
    "condition_error_rates.csv",
    "condition_error_confidence.csv",
    "confusion_matrix.csv",
    "top_confusion_pairs.csv",
    "final_condition_report.csv",
    "final_confusion_matrix.csv",
    "confusion_matrix.png",
]


def move_file(source, destination):
    if not source.exists():
        print(f"SKIP  : {source.name}")
        return

    target = destination / source.name

    if target.exists():
        print(f"EXISTS: {target}")
        return

    shutil.move(str(source), str(target))
    print(f"MOVED : {source} -> {target}")


print("=" * 60)
print("DRUGSENSE PROJECT CLEANUP")
print("=" * 60)

print("\nMoving old model files...")

for filename in old_models:
    source = PROJECT / "models" / filename
    move_file(source, ARCHIVE_MODELS)


print("\nMoving old analysis files...")

for filename in old_analysis:
    source = PROJECT / "data" / filename
    move_file(source, ARCHIVE_ANALYSIS)


print("\nChecking important model files...")

important_models = [
    PROJECT / "models" / "fixed_tfidf_vectorizer.joblib",
    PROJECT / "models" / "fixed_svm_model.joblib",
]

for model in important_models:
    if model.exists():
        print(f"KEEP  : {model.name}")
    else:
        print(f"WARNING: Missing {model.name}")


print("\nChecking virtual environment...")

venv = PROJECT / "venv"

if venv.exists():
    print("KEEP  : venv")
else:
    print("WARNING: venv folder not found")


print("\n" + "=" * 60)
print("CLEANUP FINISHED")
print("=" * 60)
print("\nNothing was permanently deleted.")
print("Old files were moved into archive.")
