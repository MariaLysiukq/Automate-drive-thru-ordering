from typing import Any

# Умовна база даних меню ресторану
MENU = {
    "cheeseburger": {"price": 5.0, "available_options": ["no_onion", "extra_cheese"]},
    "fries": {"price": 2.5, "available_options": ["large", "medium"]},
    "coke": {"price": 1.5, "available_options": ["no_ice"]}
}

class InvalidOrderError(Exception):
    """Кастомний виняток для некоректних замовлень."""
    pass

def process_order(order: dict[str, Any]) -> dict[str, Any]:
    """
    Перевіряє замовлення та розраховує підсумкову ціну.
    """
    if not isinstance(order, dict) or "items" not in order or not order["items"]:
        raise InvalidOrderError("Замовлення порожнє або має некоректний формат.")

    total_price = 0.0
    processed_items = []

    for item in order["items"]:
        name = item.get("name")
        quantity = item.get("quantity", 1)
        options = item.get("options", [])

        # Валідація наявності товару в меню
        if name not in MENU:
            raise InvalidOrderError(f"Товар '{name}' відсутній у меню.")

        # Валідація кількості
        if not isinstance(quantity, int) or quantity <= 0:
            raise InvalidOrderError(f"Некоректна кількість для '{name}': {quantity}.")

        # Валідація опцій/модифікаторів
        for option in options:
            if option not in MENU[name]["available_options"]:
                raise InvalidOrderError(f"Опція '{option}' недоступна для '{name}'.")

        item_total = MENU[name]["price"] * quantity
        total_price += item_total

        processed_items.append({
            "name": name,
            "quantity": quantity,
            "subtotal": item_total
        })

    return {
        "status": "success",
        "total_price": total_price,
        "item_count": len(processed_items)
    }
