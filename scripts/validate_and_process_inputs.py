"""Provides validation and processing for Action inputs."""

import os
import sys
from pathlib import Path

# NOTE: argparse and plumbum were tested for this validation but it was too
# difficult to capture their errors and convert them into messages useful to the
# action's end user

INPUT_PATH = os.environ["INPUT_PATH"]
INPUT_SUBCOMMAND = os.environ["INPUT_SUBCOMMAND"]
INPUT_ANSWERS_FILE = os.environ["INPUT_ANSWERS_FILE"]
INPUT_PRERELEASES = os.environ["INPUT_PRERELEASES"]


def main() -> None:
    """Provides validation and processing for Action inputs."""
    # Validate 'path' input was provided
    if not INPUT_PATH:
        print("::error title=Copier Action Error::Input 'path' is empty.")
        sys.exit(1)

    # Converts INPUT_PATH to constant COPIER_ABSOLUTE_PATH
    COPIER_ABSOLUTE_PATH = ""
    if Path(INPUT_PATH).is_absolute():
        COPIER_ABSOLUTE_PATH = Path(INPUT_PATH)
    else:
        COPIER_ABSOLUTE_PATH = Path(os.environ["GITHUB_WORKSPACE"]) / INPUT_PATH

    # Sets env var COPIER_ABSOLUTE_PATH for use in future steps
    with Path(os.environ["GITHUB_ENV"]).open("a") as f:
        f.write(f"COPIER_ABSOLUTE_PATH={COPIER_ABSOLUTE_PATH}\n")

    # Validates if COPIER_ABSOLUTE_PATH exists
    if not COPIER_ABSOLUTE_PATH.exists():
        print(
            f"::error title=Copier Action Error::Value '{INPUT_PATH}' "
            "for input 'path' is not a valid path."
        )
        sys.exit(1)

    # Validate 'subcommand' input was provided
    if not INPUT_SUBCOMMAND:
        print(
            "::error title=Copier Action Error::Input 'subcommand' "
            "is required but was not provided."
        )
        sys.exit(1)

    # Validate 'subcommand' input is valid
    VALID_SUBCOMMAND_VALUES = ["check-update"]
    if INPUT_SUBCOMMAND not in VALID_SUBCOMMAND_VALUES:
        print(
            "::error title=Copier Action Error::Value "
            f"'{INPUT_SUBCOMMAND}' for input 'subcommand' is not one "
            f"of these valid values: {VALID_SUBCOMMAND_VALUES}."
        )
        sys.exit(1)

    # Validate 'answers-file' input was provided
    if not INPUT_ANSWERS_FILE:
        print("::error title=Copier Action Error::Input 'answers-file' is empty.")
        sys.exit(1)

    # Validate path provided by 'answers-file' exists
    ANSWERS_PATH = Path(INPUT_PATH) / INPUT_ANSWERS_FILE
    if not ANSWERS_PATH.exists():
        print(
            f"::error title=Copier Action Error::Value '{INPUT_ANSWERS_FILE}' "
            "for input 'answers-file' is not a valid path."
        )
        sys.exit(1)

    # Validate 'prereleases' input was provided
    if not INPUT_PRERELEASES:
        print("::error title=Copier Action Error::Input 'prereleases' is empty.")
        sys.exit(1)

    # Validate 'prereleases' input is valid
    VALID_PRERELEASES_VALUES = ["true", "false"]
    if INPUT_PRERELEASES not in VALID_PRERELEASES_VALUES:
        print(
            "::error title=Copier Action Error::Value "
            f"'{INPUT_PRERELEASES}' for input 'prereleases' is not one "
            f"of these valid values: {VALID_PRERELEASES_VALUES}."
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
