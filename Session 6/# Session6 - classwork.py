#           Session 6

# students = {
#     "101": {
#         "name": "Alice Johnson",
#         "age": 20,
#         "grade": "A",
#         "courses": ["Math", "Physics", "Computer Science"],
#         "attendance": 95
#     },
#     "102": {
#         "name": "Bob Smith",
#         "age": 21,
#         "grade": "B",
#         "courses": ["History", "Literature", "Political Science"],
#         "attendance": 88
#     },
#     "103": {
#         "name": "Charlie Brown",
#         "age": 19,
#         "grade": "A-",
#         "courses": ["Biology", "Chemistry", "Physics"],
#         "attendance": 92
#     },
#     "104": {
#         "name": "Diana Adams",
#         "age": 22,
#         "grade": "C+",
#         "courses": ["Economics", "Statistics", "Business"],
#         "attendance": 80
#     },
#     "105": {
#         "name": "Ethan Green",
#         "age": 20,
#         "grade": "B+",
#         "courses": ["Computer Science", "Mathematics"],
#         "attendance": 90
#     }
# }


#   Task1: that prints the user id and prints the name of the student in the following format
# 101: Alice Johnson
# 102: Bob Smith
# etc.

# for key, value in students.items():
#     print(f'{key}: {value["name"]}')




#   Task 2: print only students that grades are A (A-, A)

# for key, value in students.items():
#     if "A" in value["grade"]:
#         print(f'{key}: {value["name"]}, {value["grade"]}')




#   Task 3: Ask user for an input of course
# Print the studets that are taking this course
# Input: Computer Science
# Output:
# 101: Alice Johnson
# 105: Ethan Green

# course_name = input("Enter the course name: ")
# for key, value in students.items():
#     if course_name in value["courses"]:
#         print(f'{key}: {value["name"]} - {value["courses"]}')






#                   FUNCTIONS

# Small chunk or repeatable code which you can call multiple times in your program
# DRY (Do Not Repeat Yourself)

# How to create a function
# def

# def <functionName> ():
#   code...

#       Example 1:
# def helloworld():
#     print("Hello World")
#     print("Hello World")
#     print("Hello World")
#     # additional 20-30 lines of code 
     
# helloworld()


#       Example 2:
# def helloworld(inp_arg):
#     for i in range(inp_arg):
#         print("Hello World")
     
# helloworld(5)



#       Class task 1:
# create a function that takes an integer input and prints if it's Odd or Even

# def input(i):
#     if i % 2 == 0:
#         print(" This is even number")
#     else:
#         print("This is odd number")

# input(6)




#               What is the dif between print() and return
# print() ---> to output the values
# return ----> only used in functions | the purpose is ---> return outputs data type back


# print(type(print("Hello")))
# When you using print, youre just printing, nothing is being stored as data type

# when you use return, you output the data type

# def input(i):
#     if i % 2 == 0:
#         return "This is even number"
#     else:
#         return "This is odd number"

# print(input(6))
# print(type(input(6)))



#       Class task 2
# Create a function that takes list of integers
# return the list of even numbers

# def func(lst):
#     even_list = []
#     for i in lst:
#         if i % 2 == 0:
#             even_list.append(i)

#     return even_list

# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list2 = [46, 12, 97, 56, 43, 1, 37]
# list3 = [5, 64, 89, 54, 22, 13, 78]

# print(func(list))
# print(func(list2))
# print(func(list3))




#       Class task 2

# Take an input of word and character and return an index of this character
# if no char is available return "No such character"

def func(word, char):
    if char in word:
        return word.index(char)
    else:
        return "No such character"

print(func('akumosolutions', 'o'))
print(func('akumosolutions', 'z'))

