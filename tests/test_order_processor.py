import pytest
from order_processor import process_order, InvalidOrderError

# 1. Тест успішної обробки з використанням фікстури
def test_process_valid_order(valid_order_payload):
    result = process_order(valid_order_payload)
    
    assert result["status"] == "success"
    assert result["total_price"] == 11.5  # (5.0 * 2) + (1.5 * 1)
    assert result["item_count"] == 2

# 2. Параметризований тест для перевірки різних некоректних сценаріїв
@pytest.mark.parametrize(
    "invalid_payload, expected_error_msg",
    [
        ({}, "Замовлення порожнє або має некоректний формат."),
        ({"items": []}, "Замовлення порожнє або має некоректний формат."),
        ({"items": [{"name": "pizza", "quantity": 1}]}, "Товар 'pizza' відсутній у меню."),
        ({"items": [{"name": "fries", "quantity": -1}]}, "Некоректна кількість для 'fries': -1."),
        (
            {"items": [{"name": "coke", "quantity": 1, "options": ["extra_cheese"]}]},
            "Опція 'extra_cheese' недоступна для 'coke'."
        ),
    ]
)
def test_process_invalid_orders(invalid_payload, expected_error_msg):
    with pytest.raises(InvalidOrderError) as exc_info:
        process_order(invalid_payload)
    
    assert str(exc_info.value) == expected_error_msg
