<!-- header:start -->

# ![Icon](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGNsYXNzPSJmZWF0aGVyIGZlYXRoZXItY29weSIgY29sb3I9InllbGxvdyI+PHJlY3QgeD0iOSIgeT0iOSIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiByeD0iMiIgcnk9IjIiPjwvcmVjdD48cGF0aCBkPSJNNSAxNUg0YTIgMiAwIDAgMS0yLTJWNGEyIDIgMCAwIDEgMi0yaDlhMiAyIDAgMCAxIDIgMnYxIj48L3BhdGg+PC9zdmc+) GitHub Action: Copier Action

<div align="center">
  <img src="https://opengraph.githubassets.com/4236dadf667072ba968e65be2818fa5ea6b7c601f079a713200972d86fca1e87/natescherer/copier-action" width="60px" align="center" alt="Copier Action" />
</div>

---

<!-- header:end -->
<!-- badges:start -->

[![Marketplace](https://img.shields.io/badge/Marketplace-copier--action-blue?logo=github-actions)](https://github.com/marketplace/actions/copier-action)
[![Release](https://img.shields.io/github/v/release/natescherer/copier-action)](https://github.com/natescherer/copier-action/releases)
[![License](https://img.shields.io/github/license/natescherer/copier-action)](http://choosealicense.com/licenses/mit/)
[![Stars](https://img.shields.io/github/stars/natescherer/copier-action?style=social)](https://img.shields.io/github/stars/natescherer/copier-action?style=social)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/natescherer/copier-action/blob/main/CONTRIBUTING.md)

<!-- badges:end -->
<!-- overview:start -->

## Overview

A GitHub Action for Copier

<!-- overview:end -->
<!-- usage:start -->

## Usage

```yaml
- uses: natescherer/copier-action@adef85c25402ef1c12db7b8c73dc1d491ae4349d # main
  with:
    # The base path to use when running the action (Defaults to the root of your repo, and relative paths are assumed to be based on the root of your repo)
    # Default: `${{ github.workspace }}`
    path: ${{ github.workspace }}

    # The subcommand to use (Only "check-update" is currently supported)
    # This input is required.
    subcommand: ""

    # The path to the answers file (Defaults to ".copier-answers.yml")
    # Default: `.copier-answers.yml`
    answers-file: .copier-answers.yml

    # If set to "true", will use prereleases to compare template VCS tags
    # Default: `false`
    prereleases: "false"
```

<!-- usage:end -->
<!-- inputs:start -->

## Inputs

| **Input**          | **Description**                                                                                                                                       | **Required** | **Default**               |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | ------------------------- |
| **`path`**         | The base path to use when running the action (Defaults to the root of your repo, and relative paths are assumed to be based on the root of your repo) | **false**    | `${{ github.workspace }}` |
| **`subcommand`**   | The subcommand to use (Only "check-update" is currently supported)                                                                                    | **true**     | -                         |
| **`answers-file`** | The path to the answers file (Defaults to ".copier-answers.yml")                                                                                      | **false**    | `.copier-answers.yml`     |
| **`prereleases`**  | If set to "true", will use prereleases to compare template VCS tags                                                                                   | **false**    | `false`                   |

<!-- inputs:end -->
<!-- secrets:start -->
<!-- secrets:end -->
<!-- outputs:start -->

## Outputs

| **Output**                          | **Description**                                  |
| ----------------------------------- | ------------------------------------------------ |
| **`check-update_current_version`**  | The current template version used by your repo   |
| **`check-update_latest_version`**   | The latest template version available            |
| **`check-update_update_available`** | 'true' if an update is available, 'false' if not |

<!-- outputs:end -->
<!-- examples:start -->
<!-- examples:end -->
<!-- contributing:start -->

## Contributing

Contributions are welcome! Please see the [contributing guidelines](https://github.com/natescherer/copier-action/blob/main/CONTRIBUTING.md) for more details.

<!-- contributing:end -->
<!-- security:start -->
<!-- security:end -->
<!-- license:start -->

## License

This project is licensed under the MIT License.

SPDX-License-Identifier: MIT

Copyright © 2026 natescherer

For more details, see the [license](http://choosealicense.com/licenses/mit/).

<!-- license:end -->
<!-- generated:start -->

---

This documentation was automatically generated by [CI Dokumentor](https://github.com/hoverkraft-tech/ci-dokumentor).

<!-- generated:end -->
