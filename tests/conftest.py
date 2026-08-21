import pytest

@pytest.fixture
def valid_order_payload():
    """Фікстура коректного замовлення."""
    return {
        "order_id": 101,
        "items": [
            {"name": "cheeseburger", "quantity": 2, "options": ["no_onion"]},
            {"name": "coke", "quantity": 1, "options": ["no_ice"]}
        ]
    }
