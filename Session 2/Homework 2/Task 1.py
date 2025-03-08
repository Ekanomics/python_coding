##### Task 1: Number Comparison
# Write a program that takes two integer inputs and prints:
# "Both numbers are equal" if they are the same.
# "The first number is greater" if the first number is larger.
# "The second number is greater" if the second number is larger.

num1 = int(input("Please enter number 1: "))
num2 = int(input("Please enter number 2: "))
if num1 == num2:
    print("Both number are equal")
elif num1 > num2:
    print("The first number is greater")
else:
    print("The second number is greater")



