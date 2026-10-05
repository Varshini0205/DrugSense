# Run all project tests.
# This checks the complete DrugSense project.

import subprocess
import sys


def main():
    command = [
        sys.executable,
        "-m",
        "pytest",
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
