from unittest.mock import patch
import pytest

@pytest.fixture
def valid_order_payload():
    return {
        "order_id": 101,
        "items": [
            {"name": "cheeseburger", "quantity": 2, "options": ["no_onion"]},
            {"name": "coke", "quantity": 1, "options": ["no_ice"]},
        ],
    }

@pytest.fixture(autouse=True)
def mock_load_menu():
    mocked_menu = {
        "cheeseburger": {"price": 5.0, "available_options": ["no_onion"]},
        "coke": {"price": 1.5, "available_options": ["no_ice"]},
        "fries": {"price": 2.0, "available_options": []},
    }
    with patch("order_processor.load_menu", return_value=mocked_menu):
        yield
