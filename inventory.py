from exceptions import NegativeNumberException
import os


# show menu option and return selected option
def get_menu_option():
    try:
        return int(input("Select an option: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return None


# ask the user for the product name
def get_product_name():
    name = input("Enter the product name: ").strip()
    if name:
        return name
    else:
        print("Product name cannot be empty.")


# ask the user for the product price and handle exceptions
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


# ask the user for the product quantity and handle exceptions
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


# create and return a product dictionary
def create_product():
    name = None
    while name is None:
        name = get_product_name()

    price = None
    while price is None:
        price = get_price()

    quantity = None
    while quantity is None:
        quantity = get_quantity()

    return {
        "name": name,
        "price": price,
        "quantity": quantity,
        "total_line": price * quantity,
    }


# receive a list of products, calculate the total cost and print product information
def print_products(products):
    if empty_inventory(products):
        return

    print(f"\n{'='*60}")
    print("INVENTORY LIST")
    print(f"{'='*60}")

    for product in products:
        print(
            f"Product: {product['name']} | "
            f"Unit Price: ${product['price']:.2f} | "
            f"Quantity: {product['quantity']} | "
            f"Total: ${product['total_line']:.2f}"
        )

    print(f"{'='*60}\n")


def show_statics_options():
    print(
        "\nStatistics Menu:\n"
        "1. Total inventory value\n"
        "2. Total number of products\n"
        "3. Return to main menu"
    )


def empty_inventory(products):
    total = len(products)
    if total <= 0:
        print("Inventory is empty.")
        return True
    return False


def total_inventory(products):
    if empty_inventory(products):
        return None
    return len(products)


def total_price_products(products):
    if empty_inventory(products):
        return None
    return sum(p["total_line"] for p in products)


def print_total_price_products(products):
    total = total_price_products(products)
    if total is not None:
        print(f"Total inventory value: ${total:.2f}")


def print_total_inventory(products):
    total = total_inventory(products)
    if total is not None:
        print(f"Total number of products: {total}")


# handle the flow program invoking all required functions
def main():
    products = []
    continue_ = True

    while continue_:
        print(
            "\nMain Menu:\n"
            "1. Add a product\n"
            "2. Show inventory\n"
            "3. Show statistics\n"
            "4. Exit"
        )
        option = get_menu_option()

        match option:
            case 1:
                product = create_product()
                products.append(product)
                print("Product added successfully.")

            case 2:
                print_products(products)

            case 3:
                continue_statics = True
                while continue_statics:
                    show_statics_options()
                    statics_options = get_menu_option()

                    match statics_options:
                        case 1:
                            print_total_price_products(products)
                        case 2:
                            print_total_inventory(products)
                        case 3:
                            continue_statics = False
                        case _:
                            print("Invalid option. Please try again.")

            case 4:
                continue_ = False

            case _:
                print("Invalid option. Please try again.")

    print("\nFinal Inventory:")
    print_products(products)


if __name__ == "__main__":
    main()
