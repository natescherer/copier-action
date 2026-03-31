"""Runs 'copier check-update' and sets Action outputs."""

import json
import os
import sys
from pathlib import Path

from plumbum import local

COPIER_ABSOLUTE_PATH = Path(os.environ["COPIER_ABSOLUTE_PATH"])
INPUT_ANSWERS_FILE = os.environ["INPUT_ANSWERS_FILE"]
INPUT_PRERELEASES = os.environ["INPUT_PRERELEASES"]
PRERELEASES_CONVERTED = "--prereleases" if INPUT_PRERELEASES == "true" else None


def main():
    """Runs 'copier check-update' and sets Action outputs."""
    copier = local["copier"]

    print("Running copier...")
    copier_output = copier(
        "check-update",
        COPIER_ABSOLUTE_PATH,
        "--output-format",
        "json",
        "--answers-file",
        INPUT_ANSWERS_FILE,
        PRERELEASES_CONVERTED,
    )

    try:
        update_data = json.loads(copier_output)
    except (json.JSONDecodeError, TypeError) as e:
        print(
            f"Output from copier was not the expected JSON, exiting: {e}",
            file=sys.stderr,
        )
        sys.exit(1)
    print(f"Copier output was: {update_data}")

    with Path(os.environ["GITHUB_OUTPUT"]).open("a") as f:
        print(f"Setting Output: current-version={update_data['current_version']}")
        f.write(f"current-version={update_data['current_version']}\n")
        print(f"Setting Output: latest-version={update_data['latest_version']}")
        f.write(f"latest-version={update_data['latest_version']}\n")
        print(
            f"Setting Output: update-available={'true' if update_data['update_available'] else 'false'}"
        )
        f.write(
            f"update-available={'true' if update_data['update_available'] else 'false'}\n"
        )


if __name__ == "__main__":
    main()
