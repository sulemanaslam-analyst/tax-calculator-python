def calculate_tax(income):
    if income <= 600000:
        return 0
    elif income <= 1200000:
        return income * 0.05
    elif income <= 2400000:
        return income * 0.10
    else:
        return income * 0.15

if __name__ == "__main__":
    income = int(input("Enter your income: "))
    tax = calculate_tax(income)
    print(f"Your tax is: {tax}")