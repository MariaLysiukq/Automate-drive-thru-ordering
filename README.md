# Drive-Thru Order Validator

[![Run Pytest Suite](https://github.com/MariaLysiukq/Automate-drive-thru-ordering/actions/workflows/tests.yml/badge.svg)](https://github.com/MariaLysiukq/Automate-drive-thru-ordering/actions/workflows/tests.yml)

A Python validation engine for AI-driven drive-thru ordering systems. It verifies incoming order payloads against menu items, prices, and available options.

## Features

* Dynamic menu configuration using YAML (`menu.yaml`).
* Validation of item availability, option selection, and order quantities.
* Integration handling for POS system submission.
* Automated CI testing via GitHub Actions.

## Setup & Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/MariaLysiukq/Automate-drive-thru-ordering.git](https://github.com/MariaLysiukq/Automate-drive-thru-ordering.git)
   cd Automate-drive-thru-ordering
   
2. Install dependencies with Poetry:
    poetry install

Running Tests

Run the full test suite with Pytest:
poetry run pytest -v


---
**Commands to Commit the Changes**

```bash
git add README.md
git commit -m "docs: update README with setup guide and CI badge"
git push
