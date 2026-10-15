# Drive-Thru Order Validator

[![Run Pytest Suite](https://github.com/MariaLysiukq/Automate-drive-thru-ordering/actions/workflows/tests.yml/badge.svg)](https://github.com/MariaLysiukq/Automate-drive-thru-ordering/actions/workflows/tests.yml)

A small Python project that validates drive-thru order data against a YAML menu, calculates the order total, and demonstrates sending a summary to a POS endpoint.

## Features

- Loads menu items, prices, and allowed options from `menu.yml`
- Checks that orders contain valid items, quantities, and options
- Calculates item subtotals and the order total
- Includes Pytest tests for valid orders, invalid input, and POS request failures

## Requirements

- Python 3.10+
- Poetry

## Setup

```bash
git clone https://github.com/MariaLysiukq/Automate-drive-thru-ordering.git
cd Automate-drive-thru-ordering
poetry install
```

## Run the tests

```bash
poetry run pytest -v
```

The tests mock the HTTP request, so they do not send orders to an external POS service.

## Menu configuration

The menu is stored in `menu.yml`. Each item has a price and a list of allowed options. For example:

```yaml
cheeseburger:
  price: 5.0
  available_options:
    - no_onion
    - extra_cheese
```

## POS integration status

The current code sends a summary to a fixed example URL: `https://api.pos-system.com/v1/orders`. This is a placeholder, not a configured or verified POS integration. Do not use it for real orders without replacing the URL and adding the required configuration and error handling.

## Project structure

```text
.
├── order_processor.py
├── menu.yml
├── tests/
│   ├── conftest.py
│   └── test_order_processor.py
└── pyproject.toml
```
