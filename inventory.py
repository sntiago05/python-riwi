from execeptions import NegativeNumberExeception


# show menu option and return selected option
def get_menu_option():
    try:
        return int(input("Enter an option: "))
    except ValueError:
        print("Choose a valid option")
        return None


# ask the user for the product name
def get_product_name():
    name = input("Enter the product name: ").strip()
    if name:
        return name
    else:
        print("Name cannot be empty")


# ask the user for the product price and handle execeptions
def get_price():
    try:
        price = float(input("Enter the product price: "))
        if price <= 0:
            raise NegativeNumberExeception("Enter values greater than zero")
        return price
    except ValueError:
        print("Please, enter a numeric value.")
    except NegativeNumberExeception as e:
        print(e)

    return None


# ask the user for the product quantity and handle execeptions
def get_quantity():
    try:
        quantity = int(input("Enter the quantity: "))
        if quantity <= 0:
            raise NegativeNumberExeception("Enter values greater than zero")
        return quantity
    except ValueError:
        print("Please, enter a numeric value.")
    except NegativeNumberExeception as e:
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
    if len(products) <= 0:
        return
    total = sum(p["total_line"] for p in products)

    print(f"{'='*60}\n")

    for product in products:
        print(
            f"Product: {product['name']} | "
            f"Unitary price: {product['price']} | "
            f"Quantity: {product['quantity']} | "
            f"Total line: {product['total_line']}"
        )

    print(f"Total: {total}")
    print(f"{'='*60}\n")


# handle the flow program invoking all required functions
def main():
    products = []
    continue_ = True

    while continue_:
        print("1. Enter a product\n2. Exit")

        option = get_menu_option()

        if option == 2:
            continue_ = False
            continue

        if option == 1:
            product = create_product()
            products.append(product)

    print_products(products)


if __name__ == "__main__":
    main()
