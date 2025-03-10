# Task 3: Factorial of a Number (use for loop)
# Input:
# Enter a number: 5

# Output:
# Factorial of 5 is 120

# Example of factorial:
# 4! = 1*2*3*4 = 24

num = int(input("Enter the number: "))
fact = 1
for f in range(1, num + 1):
    fact *= f
print(f"Factorial of {num} is {fact}")

