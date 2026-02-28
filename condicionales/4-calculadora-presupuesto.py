class NegativeZeroInputExeception(Exception):
    pass


def get_monthly_income_expenses():
    try:
        income = float(input("What is your monthly income?: "))
        expenses = float(input("What are your total monthly expenses?: "))
        if income <= 0 or expenses <= 0:
            raise NegativeZeroInputExeception("Value must be greater than zero")
        return income, expenses
    except ValueError:
        print("Please only enter numeric values")
    except NegativeZeroInputExeception as e:
        print(e)


def calculate_savings(income, expenses):
    if income is not None and expenses is not None:
        if expenses <= income * 0.5:
            savings = income - expenses
            savings_percent = savings / income * 100
            return savings, savings_percent
        else:
            return None, None


def main():
    montly_data = get_monthly_income_expenses()
    if montly_data:
        savings, percent = calculate_savings(*montly_data)
        if savings is not None and percent is not None:
            print(
                f"Recommended savings: ${savings:.2f} ({percent:.2f}% of your income)"
            )
        else:
            print("Need to reduce your expenses")


if __name__ == "__main__":
    main()
