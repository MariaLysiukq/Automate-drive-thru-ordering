# Drive-Thru Order Validator Engine
A Python-based validation module for quick-service restaurant drive-thru AI systems. The engine validates incoming JSON order payloads against the active menu, verifies optional item modifiers, and calculates the total bill.

## Tech Stack
    Python 3.10+
    Poetry (Dependency Management)
    Pytest (Automated Testing)

## Project Structure
```text
drive_thru_validator/
├── order_processor.py        # Core validation logic & menu data
├── pyproject.toml            # Dependencies and project config
├── README.md                 # Project documentation
└── tests/
    ├── conftest.py           # Shared pytest fixtures
    └── test_order_processor.py # Unit test suite

Quick Start

    1. Install Dependencies:
        poetry install

    2. Run Test Suite:
        poetry run pytest -v
