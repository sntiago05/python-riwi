import json

PATH = "./manejo-archivos/json/inventory.json"
inventorry = [
    {"id": 1, "name": "mouse", "price": 12, "quantity": 2},
    {"id": 2, "name": "keyboard", "price": 20, "quantity": 4},
    {"id": 3, "name": "monitor", "price": 70, "quantity": 5},
]

with open(PATH, mode="w", encoding="utf-8", newline="") as file:
    json.dump(inventorry, file, indent=4)

with open(PATH, encoding="utf-8") as file:
    data = json.load(file)

print("\n".join(f"{p["id"]} - {p["name"]}" for p in data))
