# Task 2: Number Swapper
# Write a Python program that takes two numbers as input from the user and swaps their values.


num1 = int(input("Input number 1 = "))
num2 = int(input("Input number 2 = "))
print(f"Original values: number1 = {num1}, number2 = {num2}")

num1, num2 = num2, num1
print(f"Swapped result: number1 = {num1}, number2 = {num2}")

