from exceptions import NegativeNumberException
import service
import handle_files


def get_menu_option():
    try:
        return int(input("Select an option: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return None


def get_name(type_: str):
    name = input(f"Enter the {type_} name: ").strip()
    if name:
        return name
    print(f"{type_.capitalize()} name cannot be empty.")


def get_id():
    try:
        id = int(input("Enter the id to search: "))
        if id <= 0:
            raise NegativeNumberException("Id must be greater than zero")
        return id
    except ValueError:
        print("Id must be an int value")
    except NegativeNumberException as e:
        print(e)


def validate_id():
    id = None
    while id is None:
        id = get_id()
    return id


def get_price():
    try:
        price = float(input("Enter the product price: "))
        if price <= 0:
            raise NegativeNumberException("Price must be greater than zero.")
        return price
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
    except NegativeNumberException as e:
        print(e)
    return None


def get_quantity():
    try:
        quantity = int(input("Enter the quantity: "))
        if quantity <= 0:
            raise NegativeNumberException("Quantity must be greater than zero.")
        return quantity
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
    except NegativeNumberException as e:
        print(e)
    return None


def validate_quantity():
    quantity = None
    while quantity is None:
        quantity = get_quantity()
    return quantity


def validate_price():
    price = None
    while price is None:
        price = get_price()
    return price


def validate_name(type_: str):
    name = None
    while name is None:
        name = get_name(type_)
    return name


def hanlde_create_product(products: list):
    name = validate_name("product")
    price = validate_price()
    quantity = validate_quantity()
    service.add_product(products, name, price, quantity)


def change_attribute(name_change: str):
    change = ""
    while change not in ("y", "n"):
        change = input(f"Want to change the {name_change}? (y/n): ").strip().lower()
    return change == "y"


def include_header():
    include = None
    while include not in ("y", "n"):
        include = input("Want to include headers? y/n").lower()
    return include == "y"


def update_flow(products):
    id = validate_id()

    fields = {
        "name": validate_name,
        "price": validate_price,
        "quantity": validate_quantity,
    }

    updates = {
        field: validator()
        for field, validator in fields.items()
        if change_attribute(field)
    }

    if not updates:
        print("No changes made.")
        return

    ok = service.update_product(products, id, updates)

    if ok:
        print("Product updated successfully")
    else:
        print("Product not found")


def handle_delete(products):
    id = validate_id()
    ok = service.delete_product(products, id)
    if ok:
        print("product deleted sucessfully")
    else:
        print("Operation failed")


def handle_save_csv(products):
    header = include_header()
    path = validate_name("path")
    handle_files.save_csv(products, path, header)


def show_main_menu():
    print(
        "\nMain Menu:\n"
        "1. Add a product\n"
        "2. Show inventory\n"
        "3. Show statistics\n"
        "4. Search product by id\n"
        "5. Update product\n"
        "6. Delete product\n"
        "7. Save inventory\n"
        "8. Exit"
    )


def handle_statistics(products):
    print("\n".join(service.statics(products)))


def handle_search(products):
    id = validate_id()
    product = service.search_product_by_id(products, id)

    if product:
        service.print_product(product)
    else:
        print("Product not found")

def handle_load_csv():
    pass
def main():
    products = []
    continue_ = True
    while continue_:
        show_main_menu()
        option = get_menu_option()

        match option:
            case 1:
                hanlde_create_product(products)
                print("Product added successfully.")

            case 2:
                service.show_inventory(products)

            case 3:
                handle_statistics(products)

            case 4:
                handle_search(products)

            case 5:
                update_flow(products)

            case 6:
                handle_delete(products)

            case 7:
                handle_save_csv(products)

            case 8:

            case 9:
                continue_ = False

            case _:
                print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
