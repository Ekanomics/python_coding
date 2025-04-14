# from datetime import datetime

# def show_date() -> None:
#     print('This is the current time: ')
#     print(datetime.now())

# show_date()




# def greet(name):
#     print(f'Hello, {name}!')

# greet('Askar')
# greet('Amy')



# def add(a, b):
#     return a + b

# print(add(10, 13))




# class car:
#     def __init__(self, brand, power):
#         self.brand = brand
#         self.horsepower = power

#     def drive(self):
#         print(f'{self.brand} is driving')

#     def get_info(self):
#         print(f'{self.brand} with {self.horsepower} horsepower')

# Toyota: car = car('Toyota', 250)
# Toyota.drive()
# Toyota.get_info()


# bmw: car = car('BMW', 300)
# bmw.drive()
# bmw.get_info()





# x = 9
# y = 12
# result = x // 2 * 2 / 2 + y % 2 ** 3
# print(result)



# x = 1
# x = x == x
# Answer: True


# a = 10
# b = 20
# c = a>b
# print(not(c))
# Answer: True



# x = 1 + 1 // 2 + 1 / 2 + 2
# print(x)
# A: 3.5


# z = 3
# y = 7
# x = y == z and y > z or z > y and z != y
# print(x)
# A: False



# print(1/1)



# list1 = [3, 7, 23, 42]
# list2 = [3, 7, 23, 42]
# print(list1 is list2)
# print(list1 == list2)
# # A: False, True

# print(id(list1))
# print(id(list2))


# print(3*'abc'+'xyz')



# nums = [3, 7, 23, 42]
# alphas = ['p', 'p', 'm', 'j']

# print(nums is alphas)
# print(nums == alphas)

# nums = alphas

# print(nums is alphas)
# print(nums == alphas)

# print(nums)
# print(alphas)

# A:False, FAlse, True, True, ['p', 'p', 'm', 'j']



# x = 'Peter'
# y = 'Peter'
# res = x is y
# print(res)

# y = ''.join(['P', 'e', 't', 'e', 'r'])
# print(y)



# x, y, z = 3, 2, 1
# z, y, x = x, y, z
# print(x, y, z)



# x = 1
# print(++++x)



# x = 23 + 42
# y = '23' + '42'
# z = '23' * 7
# print(type(x))
# print(type(y))
# print(type(z))



# x = 2
# y = 6
# x += 2 ** 3
# x //= y //2 // 3
# print(x)



# res = str(bool(1) + float(12) / float(2))
# print(res)
# A: str(1 + 6.0) = '7.0'


# print('Mikeii' > 'Mikey')


# x = 2 ^ 3
# print(x)


# // - performs integer division


# y = 2 + 3 * 5.
# print(y)
# A: 17.0


# equal - '=='



# a = 1
# b = 0
# a = a ^ b
# b = a ^ b
# b = a ^ b
# print(a, b)
# 1, 0



# a = 1
# b = 0
# c = a & b     # True and False = False = 0
# d = a | b     # | - or = True or False = True = 1
# e = a ^ b     # 1 - True (Бит равен 1, если только один бит равен 1)
# print(c + d + e)
# A: 2




# x = float('23.42')
# print(x)
# print(bool(x) + True)



# print('Mike' > 'MIke')      #True
# Lowercase letters (a–z) have higher ASCII values than uppercase letters (A–Z)
# Therefore, 'm' > 'M', 'z' > 'Z', 'a' > 'A', etc.



# print(2 ** 3 ** 2 ** 1)         # 2 ** 9 = 512, from right to the left



# print('t' in 'Peter')
# print('is' in 'This IS Python code.')


# z = 2
# y = 1
# x = y < z or z > y and y > z or z < y
# print(x)
# A: True


# ** - exponentiation


# x = 0
# y = 1
# x = x ^ y
# y = x ^ y
# y = x ^ y
# print(x, y)
# A: 1 1



# x = True
# y = False
# z = False

# if x or y and z:
#     print('TRUE')
# else:
#     print('FALSE')

# Оператор and выполняется раньше, чем or!






# Basics:

#! - tell a Unix OS how to execute the contens of a Python file

# 4 fundamental elements that make a language - Alphabet, lexis, syntax and semantics

# x = '\''              backslash \ doesn't count - it's an escape character
# print(len(x))
# A: 1



# 'True' , 'and' , 'in' - are illegal variable names
# But 'TRUE' and 'true' are ok


# CPython - is a default, reference implementation of the Python language, written in C


# utf-8 - default value of encoding in the string function encode()


# machine code - a low level programming language consisting of binary digits/bit that the computer reads and understands


# pyc file - contains compiled Python bytecode


# True: (such keywords like: False, True. def, or, and, pass, return and etc.)
# You cannot use keywords as variable names in Python
# You cannot use keywords as function names in Python


# escape character owes its name to the fact that it - changes the meaning of the character next to it 


# Console - command-line intepreter which lets you interact with your OS and execute Python commands and scripts


# print('Andy\nBrown')


# print('Andy Brown', end=' ')

# print('Andy Brown')

# Compilation:
# Code converted directly into machine code executable by the Processor 
# It tends to be faster than interpretation


# compiled - pyc


# index.py:
# from sys import argv
# print(argv[1] + argv[2])
# python index.py 42 3
# A: 423        # argv содержит только строки (str)


# print() function can output values of - any number of arguments (including zero)



# x = '\\\'
# print(len(x))
# A: error 


# print() is a built-in function (means no need to import it)


# IDLE - Integrated Development and Learning Environment for Python



# CPython - default implementation of the Python prog language


# A code point is - A number which makes up a character


# x = """
# """
# print(len(x))
# A: 1



# Source file - file containing written in a high-level programming language


# num = 2 + 3 * 5
# print(Num)
# A: error 


# __pycache__ - folder created by Python used to store pyc files






            # FUNCTIONS:

# def func(data):
#     for d in data[::2]:
#         yield d

# for x in func('abcdef'):
#     print(x, end='')          # end - prevents newlines

# A: ace 




# None - default return value for a function thst does not explicitly return any value 


# def func(num):
#     res = '*'
#     for _ in range(num):
#         res += res
#     return res

# for x in func(2):
#     print(x, end='')

# A: ****



# Question #6
# -----




# a = [1, 2, 3]
# a.append([4, 5])
# print(len(a))



# s = {1, 2, 3, 45}
# print(len(s))


# my_dict = {"a": 1, "b": 2}
# print(my_dict.get("c"))
# print(my_dict)

# import math
# print(math.sqrt(16))


# x = 1
# y = 2
# z = 3
# print(x, y, z, end='\n')
# print(5//2)


# secret_number = 4
# guess = int(input("Guess a number: "))
# while guess != secret_number:
#     guess = int(input("Guess a number: "))
# else:
#     print("Congrats, you found it")



# for i in range(12):
#     if i == 2:
#         continue
#     print("i is: ", i)


# def input_number(num = 10):
#     return int(input("Enter the number: ")) * num

# input_number()
# # print(input1)




# def myfunc():
#         print(num + 1, end='')
 
# num = 5
# myfunc()
# print(num+13)



# list1 = [1, 2, 3]
# list2 = list1[-3:-1]
# print(list1)
# print(list2)
# In the end, list1 = [1, 2, 3] and list = [1. 2].
# expression list1[-3:-1] means: start with the third element from the back (inclusive), which is 1. and take all elements until the last element (exclusive!)
# не включает последний элемент -1


# a = 0
# while a <= 5:
#         a += 2
#         print('@')

# @
# @
# @



# def myfun(x):
#         if x == 0:
#                 return 1
#         return x + myfun(x-1)
  
# print(myfun(5))

# # This is a classic recursive function. To find the result, I'll trace through the execution:
# myfun(5) is called
# Since 5 ≠ 0, it returns 5 + myfun(4)
# But we need to calculate myfun(4) first
# myfun(4) is called
# Since 4 ≠ 0, it returns 4 + myfun(3)
# But we need to calculate myfun(3) first
# myfun(3) is called
# Since 3 ≠ 0, it returns 3 + myfun(2)
# But we need to calculate myfun(2) first
# myfun(2) is called
# Since 2 ≠ 0, it returns 2 + myfun(1)
# But we need to calculate myfun(1) first
# myfun(1) is called
# Since 1 ≠ 0, it returns 1 + myfun(0)
# But we need to calculate myfun(0) first
# myfun(0) is called
# Since x == 0, it returns 1 (base case reached)
# Now we can go back up:
# myfun(1) = 1 + myfun(0) = 1 + 1 = 2
# myfun(2) = 2 + myfun(1) = 2 + 2 = 4
# myfun(3) = 3 + myfun(2) = 3 + 4 = 7
# myfun(4) = 4 + myfun(3) = 4 + 7 = 11
# myfun(5) = 5 + myfun(4) = 5 + 11 = 16

# Therefore, print(myfun(5)) outputs 16.




# x = [
#     'a',
#     'b',
#     {
#         'one': 1,
#         'two':
#         {
#             'x' : 10,
#             'y' : 20,
#             'z' : 30
#         },
#         'three': 3
#     },
#     'c',
#     'd'
# ]
# print(30 in x[2])

# False




# tup_a = (0, 1, 2)
# tup_b = (2, 3, 4)
# list_c = []
# for el in tup_a:
#         if el not in tup_b:
#                 list_c.append(el)
# print(list_c)

# [0, 1]



print(1 | 0 ^ 1 & ~0)