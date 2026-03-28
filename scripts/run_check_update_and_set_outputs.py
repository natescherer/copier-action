"""Runs 'copier check-update' and sets Action outputs."""

import json
import os
from pathlib import Path

from plumbum import local

COPIER_ABSOLUTE_PATH = Path(os.environ["COPIER_ABSOLUTE_PATH"])
INPUT_ANSWERS_FILE = os.environ["INPUT_ANSWERS_FILE"]
INPUT_PRERELEASES = os.environ["INPUT_PRERELEASES"]
PRERELEASES_CONVERTED = "--prereleases" if INPUT_PRERELEASES == "true" else ""


def main():
    """Runs 'copier check-update' and sets Action outputs."""
    copier = local["copier"]

    copier_output = json.parse(
        copier(
            "check-update",
            COPIER_ABSOLUTE_PATH,
            "--answers-file",
            INPUT_ANSWERS_FILE,
            PRERELEASES_CONVERTED,
        )
    )

    print(copier_output)


if __name__ == "__main__":
    main()
