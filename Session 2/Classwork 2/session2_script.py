            # Classwork 2



# Comparison Operators

# Operator	Description	               Example (a = 10, b = 3)
# ==	    Equal to	                a == b → False
# !=	    Not equal to	            a != b → True
# >	        Greater than	            a > b → True
# <	        Less than	                a < b → False
# >=	    Greater than or equal to	a >= b → True
# <=	    Less than or equal to	    a <= b → False



# Arithmetic Operators
# Used to perform mathematical operations:

# Operator	Description	         Example (a = 10, b = 3)
# +	        Addition	         a + b → 10 + 3 = 13
# -	        Subtraction	         a - b → 10 - 3 = 7
# *	        Multiplication	     a * b → 10 * 3 = 30
# /	        Division	         a / b → 10 / 3 = 3.333
# //	    Floor Division	     a // b → 10 // 3 = 3
# %	        Modulus (remainder)	 a % b → 10 % 3 = 1
# **	    Exponentiation	     a ** b → 10 ** 3 = 1000



# Membership Operators
# Used to check if a value exists in a sequence:

# Operator	 Description	               Example (lst = [1,2,3])
# in	     Returns True if found	       2 in lst → True
# not in	 Returns True if not found	   5 not in lst → True





#              Numeric Data Type

#  - Binary - always starts with 0b(zero binary) ----> 01010101
#  - Octal - 0o -         ------> 0-7
#  - Hexidecimal - 0x     ------> 16 ----> 0-9 abcdf


# 1)
#  prints 21
# print(0b010101)

# #  convert 21 to binary
# print(bin(21))

# print(oct(21))
# print(hex(21))



# 2) 
# word1 = "Hello"
# "HelloHelloHello"
# # word2 = "World"

# # combined = word1 + word2
# print(word1 * 2)



# 3)
############ Boolean
# Boolean data types True or False
# Usage: if/else conditions

# if 1 == 1:       # if True
#     print("It one")


# print(10 == 5)

# inp = int(input("Please provide a number: "))

# if inp < 10:
#     print("The number is less than 10")
# else:
#     print("The number is bigger than 10")



############### In Python code reads from top to bottom




# Class task 1:
# take the word input (string)
# find the length of the word
# if the length is more than 10
# print("THAT'S A LONG WORD")
# else
# print("the word has {length of the word} characters")


# word = input("Enter the word: ")
# length = len(word)
# if length > 10:
#     print("THAT'S A LONG WORD")
# else:
#     print(f"The word has {length} characters")



# 4)                                #####################      Boolean operators
# not, and, or

#  and | or    -----> combines 2 or more booleans together
# if num < 10 and num > 0 (0-10)

          # 4.1)
# and ----> True and True == True
#     ----> True and False == False
#     ----> False and False == False

# num = -10
# if num < 10 and num > 0:
#     print("Inside of if condition")
# else:
#     print("Inside of else condition")



          # 4.2)
# The "or" operator returns True if at least one of the operands is True. If both operands are False, it returns False.

# Truth Table for or:
# Operand1	Operand2	Result
# True	     True	   True
# True	     False	   True
# False	     True	   True
# False	     False	   False

# print(not True or not False and True and not True or False)




#  5)
# Class task 2
#  Write a program that will do the following
# 1. Takes integer input
# 2. Checks if integer is positive
# 3. Check if the integer is even or odd (odd = 21 / 2 | even = 4 / 2)
# 4. Prints the following: "The number is even/odd"


# number = int(input("Enter the number: "))
# if number >= 0:
#     print("Number is positive")
#     if number % 2 == 0:
#         print("Number is even")
#     else:
#         print("Number is odd")
# else:
#     print("Hey, give me the positive number")




