# Task 3: Simple Calculator
# Create a calculator that takes two numbers and an operator (+, -, *, /, //, %, **) as input and performs the appropriate calculation.

print("Welcome dear user, please try my calculator")

num1 = int(input("Number 1 = "))
operator = input("Operator (+, -, *, /, //, %, **): ")
num2 = int(input("Number 2 = "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
elif operator == "//":
    result = num1 // num2
elif operator == "%":
    result = num1 % num2
elif operator == "**":
    result = num1 ** num2
else:
    result = "Invalid operator, please try again"

print(f"Result = {result}")

