# Copier Action

> A GitHub Action for [Copier](https://copier.readthedocs.io/)

---

## Overview

**Copier Action** wraps [Copier](https://copier.readthedocs.io/) and its dependencies,
making it easy to automate template management tasks directly in your CI/CD workflows.

Currently supports the `check-update` subcommand to detect when a newer version of your
template is available.

This action is tested and supported on `macos-latest`, `ubuntu-latest`, and
`windows-latest` GitHub-hosted runners, and should work on any self-hosted runners that
can install [uv](https://docs.astral.sh/uv/).

---

## Usage

```yaml
- uses: natescherer/copier-action@v0
  id: copier
  with:
    subcommand: check-update
```

---

## Inputs

| Input | Description | Required | Default |
| --- | --- | --- | --- |
| `subcommand` | The Copier subcommand to run. Currently only `check-update` is supported. | **Yes** | — |
| `path` | Base path for running the action. Relative paths are resolved from the root of your repo. | No | Your repo's root via `${{ github.workspace }}` |
| `answers-file` | Path to the Copier answers file. | No | `.copier-answers.yml` |
| `prereleases` | Set to `true` to include pre-release template VCS tags when checking for updates. | No | `false` |

---

## Outputs

All outputs are namespaced by the subcommand that produced them.

### `check-update` outputs

| Output | Description |
| --- | --- |
| `check-update_current_version` | The template version currently used by your repo. |
| `check-update_latest_version` | The latest template version available upstream. |
| `check-update_update_available` | `true` if an update is available, `false` otherwise. |

---

## Examples

### Alerting when a repo's template has been updated

By design, this action only executes copier. If you are checking for updates, you will
need to *do* something with the fact that an update is available.

An example workflow is provided below that uses
[apprise](https://github.com/caronc/apprise), a Python library that has the ability to
send notification messages to many different applications and services. Also included is
the action
[liskin/gh-workflow-keepalive](https://github.com/liskin/gh-workflow-keepalive), which
works around the issue of GitHub automatically disabling scheduled workflow executions
on repos that haven't had activity in 60 days.

```yaml
name: Weekly Copier Template Update Check

on:
  schedule:
    - cron: "0 8 * * 0" # Runs every Sunday at 08:00 UTC
  workflow_dispatch: # Allows manual runs

jobs:
  copier-check-update:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0 # Ensures tags are checked out
      - name: Check for Copier Template Updates
        id: copier
        uses: natescherer/copier-action@v0
        with:
          subcommand: check-update
      - name: Notify if Update is Available
        if: steps.copier.outputs.update_available == 'true'
        uses: cstuder/apprise-ga@v3.1.0
        with:
          title: ${{ github.repository }} Template Update Available
          message: >
            Repository ${{ github.repository }} has a new template update available. Current version is ${{ steps.copier.outputs.current_version }}, latest version is ${{ steps.copier.outputs.latest_version }}.
        env:
          APPRISE_URL: ${{ secrets.APPRISE_URL }}
  workflow-keepalive:
    if: github.event_name == 'schedule'
    runs-on: ubuntu-latest
    permissions:
      actions: write
    steps:
      - uses: liskin/gh-workflow-keepalive@v1
```

---

## Contributing

Contributions and bug reports are welcome! See [CONTRIBUTING.md](./CONTRIBUTING.md).

---

## License

See [LICENSE](./LICENSE) for details.
