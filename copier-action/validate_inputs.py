"""Provides validation for Action inputs."""

import argparse


def main() -> None:
    """Validates Action inputs via argparse."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--subcommand", type=str, required=True, choices=["check-update"]
    )


if __name__ == "__main__":
    main()
