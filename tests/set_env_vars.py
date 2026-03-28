"""Sets environment variables for use in later action steps"""

# No, you can't just do this directly in action.yml, nor is there a way to
# join paths cross-platform directly in actions.yml without a shell

import os
from pathlib import Path

COPIER_TEST_BASEPATH = Path(os.environ["RUNNER_TEMP"]) / "copier-action-test-data"
COPIER_TEST_SRC_STANDARD = COPIER_TEST_BASEPATH / "src-standard"
COPIER_TEST_DST_100 = COPIER_TEST_BASEPATH / "dst-100"
COPIER_TEST_DST_100_ANSWERS_MOVED = COPIER_TEST_BASEPATH / "dst-100-answers-moved"
COPIER_TEST_DST_200 = COPIER_TEST_BASEPATH / "dst-200"

with Path(os.environ["GITHUB_ENV"]).open("a") as f:
    f.write(f"COPIER_TEST_BASEPATH={COPIER_TEST_BASEPATH}\n")
    f.write(f"COPIER_TEST_SRC_STANDARD={COPIER_TEST_SRC_STANDARD}\n")
    f.write(f"COPIER_TEST_DST_100={COPIER_TEST_DST_100}\n")
    f.write(f"COPIER_TEST_DST_100_ANSWERS_MOVED={COPIER_TEST_DST_100_ANSWERS_MOVED}\n")
    f.write(f"COPIER_TEST_DST_200={COPIER_TEST_DST_200}\n")
