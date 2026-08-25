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
**Architecture 
 order_processor.py — The heart of the project. Loads the menu configuration, validates the order payload (availability of items, permitted options, quantity $>0$), calculates the total price and sends an HTTP POST request to an external POS system. 
 
 menu.yaml — Data configuration. Stores a list of dishes, their prices and lists of permitted modifiers (available_options).
 
 conftest.py — Pytest configuration centre. Contains fixtures: `valid_order_payload` (an example of a valid order) and `mock_load_menu` with the `autouse=True` flag, which replaces file reading with mock data, making the tests fully ізольованими.
 
 tests/test_order_processor.py — Modular tests. These test the calculation of the total amount, API calls via @patch("requests.post") and the handling of InvalidOrderError exceptions using @pytest.mark.parametrize.
 
 pyproject.toml — Poetry configuration. 
 Locks in versions of Python, core libraries (requests, pyyaml) and dev dependencies (pytest). 
 
 .github/workflows/tests.yml — GitHub Actions CI/CD pipeline. 
 Script for the GitHub server: start up Ubuntu, install Python 3.12 and Poetry, resolve dependencies, and run `poetry run pytest -v` on every push.
