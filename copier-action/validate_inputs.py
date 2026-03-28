"""Provides validation for Action inputs."""

import os
import sys
from pathlib import Path

# NOTE: argparse and plumbum were tested for this validation but it was too
# difficult to capture their errors and convert them into messages useful to the
# action's end user

# Inputs
INPUT_SUBCOMMAND = os.environ["INPUT_SUBCOMMAND"]
INPUT_ANSWERS_FILE = os.environ["INPUT_ANSWERS_FILE"]
INPUT_PRERELEASES = os.environ["INPUT_PRERELEASES"]

# Validate 'subcommand' input was provided
if not INPUT_SUBCOMMAND:
    print(
        "::error title=Copier Action Error::Input 'subcommand' "
        "is required but was not provided."
    )
    sys.exit(1)

# Validate 'INPUT_SUBCOMMAND' input is valid
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
ANSWERS_PATH = Path(os.environ["GITHUB_WORKSPACE"]) / INPUT_ANSWERS_FILE
if not ANSWERS_PATH.exists():
    print(
        f"::error title=Copier Action Error::Value '{INPUT_ANSWERS_FILE}'"
        "for input 'answers-file' is not a valid path."
    )
    sys.exit(1)

# Validate 'prereleases' input was provided
if not INPUT_PRERELEASES:
    print("::error title=Copier Action Error::Input 'answers-file' is empty.")
    sys.exit(1)

# Validate 'prereleases' input is valid
VALID_PRERELEASES_VALUES = ["true", "false"]
if INPUT_PRERELEASES not in VALID_PRERELEASES_VALUES:
    print(
        "::error title=Copier Action Error::Value "
        f"'{INPUT_PRERELEASES}' for input 'subcommand' is not one "
        f"of these valid values: {VALID_PRERELEASES_VALUES}."
    )
    sys.exit(1)
