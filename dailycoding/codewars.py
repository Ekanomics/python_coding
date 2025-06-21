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

def function(arg, value1, value2):
  if arg == '+':
    return value1 + value2
  elif arg == '-':
    return value1 - value2
  elif arg == '*':
    return value1 * value2
  elif arg == '/':
    return value1 / value2
  else:
    raise ValueError("Invalid argument operation")
  
print(function('+', 2, 3))
print(function('-', 2, 3))
print(function('*', 2, 3))
print(function('/', 2, 3))



