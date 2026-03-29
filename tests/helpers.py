"""Provides helpers used for testing."""

import textwrap
from collections.abc import Mapping
from pathlib import Path

from plumbum.cmd import git as _git
from plumbum.machines import LocalCommand

StrOrPath = str | Path


def build_file_tree(
    spec: Mapping[StrOrPath, str | bytes | Path],
    dedent: bool = True,
    encoding: str = "utf-8",
) -> None:
    """Builds a file tree based on the received spec.

    Params:
        spec:
            A mapping from filesystem paths to file contents. If the content is
            a Path object a symlink to the path will be created instead.

        dedent: Dedent file contents.
    """
    for path, contents in spec.items():
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        if isinstance(contents, Path):
            path.symlink_to(contents)
        else:
            binary = isinstance(contents, bytes)
            if not binary and dedent:
                assert isinstance(contents, str)
                contents = textwrap.dedent(contents)
            mode = "wb" if binary else "w"
            enc = None if binary else encoding
            with Path(path).open(mode, encoding=enc) as fd:
                fd.write(contents)


git: LocalCommand = _git.with_env(
    GIT_AUTHOR_NAME="Test Author",
    GIT_AUTHOR_EMAIL="test@fake.com",
    GIT_COMMITTER_NAME="Test Committer",
    GIT_COMMITTER_EMAIL="test@fake.com",
)
