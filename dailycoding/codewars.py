# ____________________________________

# 1) Implement a function which convert the given boolean value into its string representation.
# Note: Only valid inputs will be given.

# def boolean_to_string(b):
#     return str(b)

# print(boolean_to_string(True))
# print(boolean_to_string(False))

# Solution: This works because Python’s built-in str() function automatically converts boolean values to the strings "True" or "False".
# ____________________________________

# 2) Summation
# Write a program that finds the summation of every number from 1 to num (both inclusive). 
# The number will always be a positive integer greater than 0. Your function only needs to return the result, 
# what is shown between parentheses in the example below is how you reach that result and it's not part of it, see the sample tests.

# For example (Input -> Output):
# 2 -> 3 (1 + 2)
# 8 -> 36 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8)


# def summation(num):
#     return sum(range(1, num + 1))
# print(summation(8))

# ____________________________________

# 3) 
# def operation(a):
#     return a()
# def function(arg):
#     print (1, 2, 3, 4)
# function()
# print(function)


# def my_function():
#   print("Hello from a function")
# my_function()


# def my_function(fname):
#   print(fname + " Refsnes")
# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")

# Your task is to create a function that does four basic mathematical operations.

# The function should take three arguments - operation(string/char), value1(number), value2(number).
# The function should return result of numbers after applying the chosen operation.

# Examples(Operator, value1, value2) --> output

# def function(arg, value1, value2):
#   if arg == '+':
#     return value1 + value2
#   elif arg == '-':
#     return value1 - value2
#   elif arg == '*':
#     return value1 * value2
#   elif arg == '/':
#     return value1 / value2
#   else:
#     raise ValueError("Invalid argument operation")
  
# print(function('+', 2, 3))
# print(function('-', 2, 3))
# print(function('*', 2, 3))
# print(function('/', 2, 3))


# _____________________________________________
# Task 4):
# Given an array of integers.
# Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.
# If the input is an empty array or is null, return an empty array.
# Example
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].


# Solution:
# def count_positives_sum_negatives(arr):
#     if not arr:                                 # returns empty list [], if not arr, which evaluates to True
#         return []
    
#     positive = sum(1 for x in arr if x > 0)
#     negative = sum(x for x in arr if x < 0)

#     # return [max(arr), min(arr)]
#     return [positive, negative]

# print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))



# _____________________________________________
# Task 5)
# # Write a function which calculates the average of the numbers in a given array.
# Note: Empty arrays should return 0.


# Solution:
# def find_average(numbers):
#     if not numbers:
#         return 0
#     count_numbers = sum(1 for x in numbers)
#     sum_of_numbers = sum(x for x in numbers)
#     avg = sum_of_numbers / count_numbers
#     return avg

# print(find_average([1, 2, 3]))

# More simple code for this task:
# def find_average(numbers)
#     return sum(array) / len(array) if array else 0



# ____________________________________________
# Task 6)
# Rock Paper Scissors
# Let's play! You have to return which player won! In case of a draw return Draw!.

# Examples(Input1, Input2 --> Output):

# "scissors", "paper" --> "Player 1 won!"
# "scissors", "rock" --> "Player 2 won!"
# "paper", "paper" --> "Draw!"


# Solution:
# def rps(p1, p2):
#     if p1 == "scissors" and p2 == "paper":
#         return "Player 1 won!"
#     elif p1 == "scissors" and p2 == "rock":
#         return "Player 2 won!"
#     elif p1 == "paper" and p2 == "rock":
#         return "Player 1 won!"
#     elif p1 == "paper" and p2 == "scissors":
#         return "Player 2 won!"
#     elif p1 == "rock" and p2 == "paper":
#         return "Player 2 won!"
#     elif p1 == "rock" and p2 == "scissors":
#         return "Player 1 won!"
#     else:
#         return "Draw!"
# print(rps("scissors", "rock"))


# Other shorter solution
# def rps(p1, p2):
#     if p1 == p2:
#         return 'Draw!'
#     elif (p1 == 'rock' and p2 == 'scissors') or (p1 == 'scissors' and p2 == 'paper') or (p1 == 'paper' and p2 == 'rock'):
#         return 'Player 1 won!'
#     else:
#         return 'Player 2 won!'



# ______________________________________________
# Task 7)
# Write function bmi that calculates body mass index (bmi = weight / height2).
# if bmi <= 18.5 return "Underweight"
# if bmi <= 25.0 return "Normal"
# if bmi <= 30.0 return "Overweight"
# if bmi > 30 return "Obese"


# Solution:
def bmi(weight, height):
    x = (weight) / (height ** 2)
    if x <= 18.5:
        return "Underweight"
    elif x <= 25.0:
        return "Normal"
    elif x <= 30.0:
        return "Overweight"
    else:
        return "Obese"

print(bmi(77, 1.72))

# test  = (77 / (172*172)) * 10000
# print(test)