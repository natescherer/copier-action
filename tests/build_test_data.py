"""Builds test data for use by CI workflows."""

import os
from pathlib import Path

from helpers import build_file_tree, git
from plumbum import local

COPIER_TEST_BASEPATH = Path(os.environ["COPIER_TEST_BASEPATH"])
COPIER_TEST_SRC_STANDARD = Path(os.environ["COPIER_TEST_SRC_STANDARD"])
COPIER_TEST_DST_100 = Path(os.environ["COPIER_TEST_DST_100"])
COPIER_TEST_DST_100_ANSWERS_MOVED = Path(
    os.environ["COPIER_TEST_DST_100_ANSWERS_MOVED"]
)
COPIER_TEST_DST_200 = Path(os.environ["COPIER_TEST_DST_200"])


def build_standard_src() -> None:
    """Build a standard src repo used for testing."""

    build_file_tree(
        {
            COPIER_TEST_SRC_STANDARD / "{{ _copier_conf.answers_file }}.jinja": (
                """\
                # Changes here will be overwritten by Copier
                {{ _copier_answers|to_nice_yaml }}
                """
            ),
            COPIER_TEST_SRC_STANDARD / "README.md.jinja": "# Version 1.0.0\n",
        }
    )

    with local.cwd(COPIER_TEST_SRC_STANDARD):
        git("init")
        git("add", ".")
        git("commit", "-m", "v1.0.0")
        git("tag", "v1.0.0")

    # Create template v2.0.0
    build_file_tree(
        {
            COPIER_TEST_SRC_STANDARD / "README.md.jinja": "# Version 2.0.0\n",
        }
    )
    with local.cwd(COPIER_TEST_SRC_STANDARD):
        git("add", ".")
        git("commit", "-m", "v2.0.0")
        git("tag", "v2.0.0")

    # Create template v3.0.0-alpha
    build_file_tree(
        {
            COPIER_TEST_SRC_STANDARD / "README.md.jinja": "# Version 3.0.0-alpha\n",
        }
    )
    with local.cwd(COPIER_TEST_SRC_STANDARD):
        git("add", ".")
        git("commit", "-m", "v3.0.0-alpha")
        git("tag", "v3.0.0-alpha")


def main():
    COPIER_TEST_BASEPATH.mkdir()
    COPIER_TEST_SRC_STANDARD.mkdir()
    COPIER_TEST_DST_100.mkdir()
    COPIER_TEST_DST_100_ANSWERS_MOVED.mkdir()
    COPIER_TEST_DST_200.mkdir()

    build_standard_src()

    copier = local["copier"]

    copier(
        "copy",
        COPIER_TEST_SRC_STANDARD,
        COPIER_TEST_DST_100,
        "--quiet",
        "--overwrite",
        "--vcs-ref=v1.0.0",
    )
    copier(
        "copy",
        COPIER_TEST_SRC_STANDARD,
        COPIER_TEST_DST_100_ANSWERS_MOVED,
        "--quiet",
        "--overwrite",
        "--vcs-ref=v1.0.0",
        "-a",
        ".config/copier-answers.yml",
    )
    copier(
        "copy",
        COPIER_TEST_SRC_STANDARD,
        COPIER_TEST_DST_200,
        "--quiet",
        "--overwrite",
        "--vcs-ref=v2.0.0",
    )


if __name__ == "__main__":
    main()
