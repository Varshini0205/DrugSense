# Run all project tests.
# This checks the complete DrugSense project.

import subprocess
import sys


TEST_PATHS = [
    "nlp/tests",
    "test_ml_predictor.py",
    "test_ml_pipeline.py",
    "test_ml_pipeline_errors.py",
    "test_ml_model_failure.py",
    "test_nlp_failure.py",
    "test_nlp_partial_failure.py",
    "test_nlp_component_errors.py",
    "test_app.py",
    "test_app_validation.py",
    "test_app_errors.py",
]


def main():
    command = [
        sys.executable,
        "-m",
        "pytest",
        *TEST_PATHS,
        "-q",
    ]

    result = subprocess.run(command)

    print()

    if result.returncode == 0:
        print("TEST STATUS: ALL TESTS PASSED")
    else:
        print("TEST STATUS: SOME TESTS FAILED")

    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
