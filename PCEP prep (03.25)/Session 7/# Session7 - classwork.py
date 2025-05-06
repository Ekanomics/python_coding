# Session7 - classwork

#   -   for else and while else
#   -   Functions
#   -   Recursive functions
#   -   Exceptions / error handling
#   -   Exception classes



# for char in "hello":
#     print(char)
#     if char == "l":
#         break
# else:
#     print("End")


# while <condition>:
    # code
# else:
#   post execution code


# ---------------


# functions
# --> starts with keyword def nameOfFunction(argument1, argument1)
# --> repetitive code

# def numberChecker(lst, number):
#     if number in lst:
#         return True
#     else:
#         return False
    
# print(numberChecker([1, 2, 3, 4], 5))


# def numberChecker(number = 2, lst=[1, 2, 3, 4]):
#     if number in lst:
#         return True
#     else:
#         return False
    
# print(numberChecker(5))


# ----------------------

# Recursive function

    # Рекурсивная функция — это функция, которая вызывает саму себя в своем теле для решения подзадачи. Основной принцип рекурсии — разбить задачу 
    # на более мелкие подзадачи, пока не будет достигнуто базовое условие, которое остановит рекурсию.

    # Пример рекурсивной функции (факториал числа):


# def factorial(n):
#     if n == 1:                    # breaking point
#         return 1                  
#     return n * factorial(n-1)     # call yourself once again

# print(factorial(5))               # Factorial of 5 = Output: 120



# Fibonacci sequence
# Последовательность Фибоначчи — это числовая последовательность, в которой каждое число равно сумме двух предыдущих. Первые два числа обычно принимаются равными 0 и 1:
# F(n)=F(n−1)+F(n−2)

# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(10))        # Output: 55



# sum(5)
# 1 + 2 + 3 + 4 + 5 == 15

# def findsum(num):
#     if num == 1:
#         return 1
#     return num + findsum(num - 1)

# print(findsum(5))


# Important use if condition broken
# else: keep adding

# not with recursion
# sum = 0
# for i in range(1, num + 1):
#     sum = sum + i





# -----------------------------

# Exceptions / Error handling

# lst = [1, 2, 3, 4, 5]
# for i in range(1, len(lst) + 1):
#     print(lst[i])

# exception are the way to handle different errors in python and provide logic to handle them
# syntax:
# try:
#   code...
# except:
# code.. | error handling

# try:
#     lst = [1, 2, 3, 4, 5]       # lst[5]
#     for i in range(1, len(lst) + 1):
#         print(lst[i])
# except:
#     print("The list is out of range")


# try:
#     print(2 / 0)
# except ZeroDivisionError:
#     # for loop
#     print("you cannot divide number by 0")



#       Class task
# Take an input of a Name
# Output the score of the student

# use try-except block to handle if student does not exists
# Output: theestudent does not exists

# Input: Alice
# Output: 95

# Input: Alex
# Output: the student does not exist

# students_data = {"Alice": 95, "Bob": 88, "Charlie": 92, "Ethan": 90, "Diana": 80}
# name = input("Enter the name: ")

# try:
#     print(students_data[name])
# except:
#     print("The student does not exist")

# for student, score in students_data.items():
#     if student == name:
        # print(f{student}: {score})

# print(students_data['Alice'])


#   Class task 2
# try:
#     data = int(input("Please enter data: "))
#     print("Nice")
# except Exception:
#     print("Invalid input! Please enter an integer")


# Class task 3
# students = ["Alice", "Bob", "Charlie"]

# try:
#     index = int(input("Please enter an index: "))
#     print(students[index])
# except ValueError:
#     print("Invalid input! Index must be an integer")
# except LookupError:
#     print("Index is out of range!")