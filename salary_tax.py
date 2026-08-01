#!/usr/bin/env python3

def calculate_final_income(salary: float) -> tuple[int, float, float]:
    if salary < 0:
        raise ValueError("Salary must be non-negative")
    if salary < 30000:
        rate = 5
    elif salary <= 70000:
        rate = 15
    else:
        rate = 20
    tax = salary * rate / 100
    final = salary - tax
    return rate, tax, final


def main():
    try:
        s = input("Enter your salary: ").strip()
        salary = float(s.replace(',',''))
    except ValueError:
        print("Invalid salary input. Please enter a numeric value.")
        return
    try:
        rate, tax, final = calculate_final_income(salary)
    except ValueError as e:
        print(e)
        return
    print(f"Salary: {salary:,.2f}")
    print(f"Tax rate: {rate}%")
    print(f"Tax amount: {tax:,.2f}")
    print(f"Final income after tax: {final:,.2f}")


if __name__ == "__main__":
    main()
