"""Provides validation for Action inputs."""

from plumbum import cli


class Validator(cli.Application):
    """Validate action inputs via Plumbum."""

    subcommand = cli.SwitchAttr(["--subcommand"], str, mandatory=True)


if __name__ == "__main__":
    Validator.run()
