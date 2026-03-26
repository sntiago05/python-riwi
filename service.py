from typing import Optional


def add_product(inventory: list[dict], name: str, price: float, quantity: int) -> None:
    last_id = inventory[-1]["id"] if inventory else 0
    inventory.append(
        {
            "id": last_id + 1,
            "name": name,
            "price": price,
            "quantity": quantity,
            "total_line": quantity * price,
        }
    )


def show_inventory(inventory: list[dict]) -> None:
    if not inventory:
        print("Empty inventory")
        return

    for item in inventory:
        print_product(item)


def print_product(item: dict):
    print(" | ".join(f"{k.replace('_',' ')} -> {v}" for k, v in item.items()))


def search_product_by_id(inventory: list[dict], id: int):
    return next((item for item in inventory if item["id"] == id), None)


def update_product(inventory: list[dict], id: int, updates: dict) -> bool:
    product = search_product_by_id(inventory, id)
    if product is None:
        return False

    for key, value in updates.items():
        if value is not None:
            product[key] = value

    product["total_line"] = product["price"] * product["quantity"]
    return True


def delete_product(inventory: list[dict], id: int) -> bool:
    for i, dic in enumerate(inventory):
        if dic["id"] == id:
            inventory.pop(i)
            return True
    else:
        return False


def statics(inventory: list[dict]):
    if not inventory:
        return ("empty inventory",)

    total_units = f"Total units in the inventory: {len(inventory)}"
    total_value = (
        f"Total value of the inventory: {sum(p["total_line"] for p in inventory)}"
    )
    most_expensive = max(inventory, key=lambda p: p["price"])
    msg_expensive = f"Product most expensive: {most_expensive['name']} - price: {most_expensive['price']}"
    most_stock = max(inventory, key=lambda p: p["quantity"])
    msg_stock = (
        f"Product with most stock: {most_stock['name']} Price: {most_stock['quantity']}"
    )
    return total_units, total_value, msg_expensive, msg_stock
