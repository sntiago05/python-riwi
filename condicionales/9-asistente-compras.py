price = float(input("Enter the product price: "))
message = "recommendable to buy your product"

has_discount: bool = bool(int(input("Has discount? Type 1 for Yes or 0 for No: ")))

if has_discount:
    discount_percent = int(input("Enter the discount percent: ")) / 100
    final_price = price - (price * discount_percent)
else:
    final_price = price

budget = float(input("Enter your budget: "))

if final_price <= budget:
    print(f"It is {message}. Final price: ${final_price:.2f}")
else:
    print(f"It is not {message}. Final price: ${final_price:.2f}")
