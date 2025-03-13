# Task 1: Reverse a List
# Write a program that reverses a list using a for loop.
# Example:
# # Input:
# Enter numbers separated by space: 1 2 3 4 5
# # Output:
# Reversed List: [5, 4, 3, 2, 1]



lst = input("Please enter numbers separated by space: ").split()        #.split() splits the input string into a list of substrings based on spaces
# print(len(lst))
reversed_lst = [],                                                      # Creating an empty list called "reversed_lst"

for i in range(len(lst) -1, -1, -1):                                    # len(lst) gives the number of elements in lst. If lst = ['1', '2', '3', '4', '5'], then len(lst) is 5
    reversed_lst.append(lst[i])
print(reversed_lst)




