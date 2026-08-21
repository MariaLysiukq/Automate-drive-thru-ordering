from unittest.mock import patch, MagicMock
import pytest
from order_processor import process_order, InvalidOrderError
import requests

@patch("requests.post")
def test_process_valid_order_success(mock_post, valid_order_payload):
    mock_response = MagicMock()
    mock_response.status_code = 201
    mock_post.return_value = mock_response

    result = process_order(valid_order_payload)

    assert result["status"] == "success"
    assert result["total_price"] == 11.5
    mock_post.assert_called_once()

@patch("requests.post")
def test_process_order_pos_failure(mock_post, valid_order_payload):
    mock_response = MagicMock()
    mock_response.status_code = 500
    mock_post.return_value = mock_response

    with pytest.raises(RuntimeError, match="POS System integration failed."):
        process_order(valid_order_payload)

@patch("requests.post")
@pytest.mark.parametrize(
    "invalid_payload, expected_error_msg",
    [
        ({}, "Order payload is empty or malformed."),
        ({"items": []}, "Order payload is empty or malformed."),
        ({"items": [{"name": "pizza", "quantity": 1}]}, "Item 'pizza' is not in the menu."),
        ({"items": [{"name": "fries", "quantity": -1}]}, "Invalid quantity for 'fries': -1."),
        (
            {"items": [{"name": "coke", "quantity": 1, "options": ["extra_cheese"]}]},
            "Option 'extra_cheese' is invalid for 'coke'."
        ),
    ]
)
def test_process_invalid_orders(mock_post, invalid_payload, expected_error_msg):
    with pytest.raises(InvalidOrderError) as exc_info:
        process_order(invalid_payload)
    
    assert str(exc_info.value) == expected_error_msg
