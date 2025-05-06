# Task 2: Remove Duplicates from a List
# Ask the user to enter multiple words separated by spaces. Store them in a list and remove duplicate words while maintaining the original order.
# Example:
# Enter words: apple banana apple cherry banana apple  
# Filtered List: ['apple', 'banana', 'cherry']


lst = input("Enter words: ").split()

filtered_list = []

for i in lst:
    if i not in filtered_list:
        filtered_list.append(i)
print("Filtered list: ", filtered_list)
