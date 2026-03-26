import csv


def save_csv(inventory: list[dict], path: str, include_header=True):
    if not inventory:
        print("Empty inventory")
        return
    with open(path, mode="w") as file:
        header = ["id", "name", "price", "quantity", "total_line"]
        writer = csv.DictWriter(file, fieldnames=header)
        if include_header:
            writer.writeheader()
        writer.writerows(inventory)
        print(f"Inventory saved in path: {path}")


def load_csv(path: str):
    try:
        with open(path) as file:
            reader = csv.DictReader(file)
            header = reader.fieldnames
            inventory = [item for item in reader if len(item.keys()) == 5]
            return inventory

    except FileNotFoundError:
        print("File not found")
