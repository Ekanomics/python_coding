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
# def bmi(weight, height):
#     x = weight / (height ** 2)
#     if x <= 18.5:
#         return "Underweight"
#     elif x <= 25.0:
#         return "Normal"
#     elif x <= 30.0:
#         return "Overweight"
#     else:
#         return "Obese"

# weight = float(input("Your weight in kg: "))
# height = float(input("You height in meters: "))

# print(bmi(weight, height))

# test  = (77 / (172*172)) * 10000
# print(test)



# _____________________________________
# Task 8)
# A hero is on his way to the castle to complete his mission. However, he's been told that the castle is 
# surrounded with a couple of powerful dragons! each dragon takes 2 bullets to be defeated, our hero has no idea how many 
# bullets he should carry.. Assuming he's gonna grab a specific given number of bullets and move forward to fight another 
# specific given number of dragons, will he survive?

# Return true if yes, false otherwise :)


# Solution:
# def hero(bullets, dragons):
#     if bullets % dragons >= 0 and bullets >= dragons * 2 and dragons != 0:
#         return True  #"Castle is yours"
#     else:
#         return False #"You shall not pass"
    
# print(hero(61, 30))




# _________________________________________
# Task 9)
# Build a function that returns an array of integers from n to 1 where n>0.

# Example : n=5 --> [5,4,3,2,1]


# Solution:
# def reverse_seq(n):
#     if n > 1:
#         return list(range(n, 0, -1))

# print(reverse_seq(7))

# REMEMBER: range(start, stop, step)
# stop is exclusive, means stops before this value




# ________________________________________
# Task 10)
# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!

# The function takes a name as its only argument, and returns one of the following strings:

# name + " plays banjo" 
# name + " does not play banjo"

# Names given are always valid strings.


# Solution:
# 1)
# def are_you_playing_banjo(name):
#     if isinstance(name, str) and name.startswith(('R', 'r')):
#         return name + " plays banjo"
#     else:
#         return name + " does not play banjo"

# print(are_you_playing_banjo("Robocop"))

# 2)
# def are_you_playing_banjo(name):
#     if name[0].lower() == 'r':
#         return name + ' plays banjo'
#     else:
#         return name + ' does not play banjo'
    
# print(are_you_playing_banjo("amazon"))




# _______________________________________________
# Task 11)
# Create a function with two arguments that will return an array of the first n multiples of x.

# Assume both the given number and the number of times to count will be positive numbers greater than 0.

# Return the results as an array or list ( depending on language ).

# Examples
# x = 1, n = 10 --> [1,2,3,4,5,6,7,8,9,10]
# x = 2, n = 5  --> [2,4,6,8,10]


# Solution(1):
# def count_by(x, n):
#     if x > 0 and n > 0:
#         return list(range(x, (x*n)+x, x))
#     else:
#         return "Number is not positive"
    
# print(count_by(-1, 10))

# Solution(2):
# def count_by(x, n):
#     return [i * x for i in range(1, n + 1)]

# print(count_by(1, 10))




# ____________________________________________________
# # Task 12)
# Deoxyribonucleic acid, DNA is the primary information storage molecule in biological systems. 
# It is composed of four nucleic acid bases Guanine ('G'), Cytosine ('C'), Adenine ('A'), and Thymine ('T').

# Ribonucleic acid, RNA, is the primary messenger molecule in cells. RNA differs slightly from DNA its chemical 
# structure and contains no Thymine. In RNA Thymine is replaced by another nucleic acid Uracil ('U').

# Create a function which translates a given DNA string into RNA.

# For example:
# "GCAT"  =>  "GCAU"
# The input string can be of arbitrary length - in particular, it may be empty. All input is guaranteed to be valid, i.e. 
# each input string will only ever consist of 'G', 'C', 'A' and/or 'T'.

# arbitrary - произвольный


# Solution:
# def dna_to_rna(dna):
#     if isinstance(dna, list):             # isinstance() - checks type of dna; and if dna is a list then it's TRUE
#         dna = ''.join(dna)                # This line is executed if dna is a list. ''.join(dna) - takes a list and joins them into a single string
#     if not dna:                           # Here we check if dna is empty. empty "" or [] == FALSE, so not dna = TRUE
#         return "GCAU"
#     return dna.replace('T', 'U')

# print(dna_to_rna([]))



# OLD   # if dna == ['G', 'C', 'A'] or dna == ['G', 'C', 'A', 'T'] or dna == []:
        #     return dna.replace('T', 'U') or ["GCA"] or ["GCAU"]


