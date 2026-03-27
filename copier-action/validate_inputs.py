"""Provides validation for Action inputs."""

import os
import sys

# NOTE: argparse and plumbum were tested for this validation but it was too
# difficult to capture their errors and convert them into messages useful to the
# action's end user

subcommand = os.environ["COPIER_SUBCOMMAND"]

# Validate 'subcommand' input was provided
if not subcommand:
    print(
        "::error title=Copier Action Error::Input 'subcommand' "
        "is required but was not provided"
    )
    sys.exit(1)

# Validate 'subcommand' input is valid
valid_subcommands = ["check-update"]
if subcommand not in valid_subcommands:
    print(
        "::error title=Copier Action Error::Value "
        f"'{subcommand}' for input 'subcommand' is not one "
        f"of these valid values: {valid_subcommands}"
    )
    sys.exit(1)
