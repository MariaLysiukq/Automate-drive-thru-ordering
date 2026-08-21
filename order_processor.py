from pathlib import Path
from typing import Any
import yaml
import requests

class InvalidOrderError(Exception):
    pass

def load_menu(config_path: str = "menu.yaml") -> dict[str, Any]:
    """Динамічно завантажує конфігурацію меню з YAML-файлу."""
    path = Path(config_path)
    if not path.exists():
        raise FileNotFoundError(f"Config file '{config_path}' not found.")
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def send_to_pos_api(order_summary: dict[str, Any]) -> bool:
    """Імітація відправки даних на зовнішній сервіс касового терміналу."""
    response = requests.post("https://api.pos-system.com/v1/orders", json=order_summary, timeout=5)
    return response.status_code == 201

def process_order(order: dict[str, Any], config_path: str = "menu.yaml") -> dict[str, Any]:
    menu = load_menu(config_path)

    if not isinstance(order, dict) or "items" not in order or not order["items"]:
        raise InvalidOrderError("Order payload is empty or malformed.")

    total_price = 0.0
    processed_items = []

    for item in order["items"]:
        name = item.get("name")
        quantity = item.get("quantity", 1)
        options = item.get("options", [])

        if name not in menu:
            raise InvalidOrderError(f"Item '{name}' is not in the menu.")

        if not isinstance(quantity, int) or quantity <= 0:
            raise InvalidOrderError(f"Invalid quantity for '{name}': {quantity}.")

        for option in options:
            if option not in menu[name]["available_options"]:
                raise InvalidOrderError(f"Option '{option}' is invalid for '{name}'.")

        item_subtotal = menu[name]["price"] * quantity
        total_price += item_subtotal
        processed_items.append({"name": name, "quantity": quantity, "subtotal": item_subtotal})

    summary = {
        "status": "success",
        "total_price": total_price,
        "item_count": len(processed_items)
    }

    # Виклик зовнішнього API
    if not send_to_pos_api(summary):
        raise RuntimeError("POS System integration failed.")

    return summary
