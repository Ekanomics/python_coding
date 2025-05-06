#           Agenda:
# While loop
# List
# Break, continue, pass

# while takes only boolean data type, which mean it will run until the condition is False

# for loops ---> it has a start and end point "Hello"
#           ---> it has a start and end point "range(10) {0, 1, -9}"
#           ...> iterator

# Syntax
# while num1 < num2
# while <condition>:
#   <code>



# secret_password = "Python123"
# inp = input("Enter: ")
# while secret_password != inp:
#     inp = input("Wrong pswd, please try again: ")


# secret_password = "Python123"
# inp = input("Enter: ")
# max_attempts = 3
# attempts = 0

# while attempts < max_attempts:
#     if secret_password != inp:
#         attempts = attempts + 1
#         inp = input("Wrong pswd, please try again: ")
#     else:
#         print("Access granted")
#         break




# max_attempts = 3
# attempts = 0

# while attempts < max_attempts: ## Runs infinetly until it turns to False
#     print(attempts)
#     attempts = attempts + 1



#           Continue & break

# break ----> It's a keyword that stops the loop

# for loop and you want to break at some point or when conditions are met
# for i in range(10):
#     if i == 5:
#         break
#     else:
#         print(i)


# continue ---->
# for has iterators -----> range(3) ----> 0, 1, 2

# for i in range(10):
#     if i % 2 != 0:
#         continue
#     else:
#         print(i)



# pass ---> it can be used with if conditions, for/while loops, functions ---> filter ---> it does nothing

# for i in range(10):
#     pass

# print("Hello")



#           Data Types, that can handle multiple values
#  - Lists
#  - Sets
#  - Tuples
#  - Dictionaries

# # ----> Lists

# lst = []
# print(type(lst))

# test_list = ["hello", 12, 1.04, True, False, 0b1]
# print(test_list)


# Class task
# ask for input of character, print names that contains this characater (note: the program should be case insensitive)
# Input: r
# Output: 
# Erkin
# Aigerim

# lst_names = [
#     "Esen",
#     "Beka",
#     "Iana",
#     "Erkin",
#     "Aigerim",
#     "Kostya",
#     "Jyldyzx",
#     "Cuneyt",
#     "Gulnaz",
#     "Aibek",
# ]

# char = input("Please enter the character: ")
# for name in lst_names:
#     if char.lower() in name.lower():
#         print(name)
#     else:
#         print(f"No student has this char in name - {char}")
#         break




#                   List functions
# Append() ----> adds to the end of the list
# insert()
# pop() ----> remove the value from the end

# fruits = ["banana", "apple", "pineapple"]
# fruits.append("cherry")
# print(fruits)

# fruits = ["banana", "apple", "pineapple"]
# fruits.insert(1, "cherry"),  # add "cherry" as an index 1 (*remember the list and everything starts with 0)
# print(fruits)

# fruits = ["banana", "apple", "pineapple"]
# fruits.pop()
# print(fruits)

# numbers = [1, 4, 0, -1, -10, 56, 5]
# numbers.sort()
# print(numbers)


# Class task 2
# With the list filter to have only string data types
lst = ["banana", True, False, "apple", 10, "pineapple", "cherry", "apple", 1, 10.3, True]
# print(isinstance(lst, str))

filtered_lst = []

for fruits in lst:
    if isinstance(fruits, str):
        filtered_lst.append(fruits)
print(filtered_lst)