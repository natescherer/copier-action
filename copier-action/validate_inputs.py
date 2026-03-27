"""Provides validation for Action inputs."""

import os
import sys

valid_subcommands = ["check-update"]

if not os.environ["SUBCOMMAND"]:
    print(
        "::error title=Copier Action Error::Input 'subcommand' "
        "is required but was not provided"
    )
    sys.exit(1)

if os.environ["SUBCOMMAND"] not in valid_subcommands:
    print(
        "::error title=Copier Action Error::Value "
        f"'{os.environ['SUBCOMMAND']}' for input 'subcommand' is not one "
        f"of these valid values: {valid_subcommands}"
    )
    sys.exit(1)
