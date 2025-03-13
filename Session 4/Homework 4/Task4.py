# Task 4: Find the Second Largest Number in a List (No max() or sort())
# Ask the user to enter a list of numbers. Find and print the second largest number without using max() or sort().
# Example:
# Enter numbers: 10 45 78 23 89 56  
# Second largest number: 78


lst = input("Enter numbers: ").split()
lst = sorted(lst)[-2]
print(lst)


