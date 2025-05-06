#           SESSION 5   

# Learn List index(), split()
# List comprehensions
# Tuples
# Difference between mutable and inmutable data types
# Intro to dictionaries


# lst = ["hello", 1, 10, True, 10, 10]
# print(lst.index(10))

#       List comprehensions ---> generate a list of elements using a single line

# create me a list of even number until 10
# lst = []
# for num in range(1, 11):
    # if num % 2 ==0:
#         lst.append(num)
# print(lst)
# IT TOOK 4 LINES TO WRITE THIS CODE


# What is the syntax?
# variable = [element | for element in sequence]
# lst_num = [i for i in range(1,21)]
# print(lst_num)
#       Only 2 lines of code

# "aKumoSolutions" ----> ['a', 'K', ... 's']
# lst = [char for char in "aKumoSolutions"]
# lst_of_num = [char for char in range(1, 11) if char % 2 ==0]
# print(lst_of_num)


# Task 1:
# Create a list of square number from 1 - 10
# output should be: [0, 1, 4, 9, 16... 100]

# lst = [i**2 for i in range(1, 11)]     # final value which will be executed is at the beginning of comprehension code = i**2
# print(lst)




#               What is mutable and immutable

# mutable ---> Data type that constantly changes
# list ----> mutable ---> append, sort, remove, pop
# string ---> immutable ---> string cannot be changed



#       Tuple
# Tuple is the immutable version of list

# tpl = [1, 2, True, 10.10, "Hello"]
# print(tpl)
# print(type(tpl))

# print(tpl[::-1])

# tpl = 1,    - so if you see comma at the end, this is tpl type

# tpl = (1, 0, -10, 8, 7)
# answer = sorted(tpl)
# print(tuple(answer))


# a = "Hello"
# print(tuple(a))


# tpl = ((i) for i in range(1, 10))






#                   WHAT IS THE DICTIONARY

# string ---> 1 key and 1 value
# int ---> 1 key and 1 value

# list ---> 1 key and multiple values
# tuple ---> 1 key and multiple values

# dict ---> multiple keys and multiple values


# jan_class = {
    # key: value
    # "beka": [i for i in range(1, 11)],
    # "yana": True,
    # "erkin": "coffee",
    # "kostya": "massage",
    # "aibek": "english teacher",
    # "aigerim": "ten years",
    # "cuneyt": "homeworks",
    # "jyldyz": "uni student",
    # "gulnaz": "roses",
    # 1: 10,
# }

# print(jan_class["beka"])
# print(jan_class["yana"])
# print(jan_class[1])

# print(jan_class.keys())
# print(jan_class.values())
# print(jan_class.items())

# jan_class.update({"beka": "Mercedes"})       ---> updating key
# print(jan_class)

# jan_class["esen"] = "python",                ---> adding new key
# print(jan_class)


#####               Dictionary keys must be unique


#                           Sets
# sets = {-10,0,90,4,5,1}
# print(type(sets))
# print(sets)




# Create a dictionary with each student
# key is random unique userid
# each key hold values like: first name, word, phone number


class_dict = {
    1: {"first_name": "beka", "word": "prius", "phone_num": "224-876-4321"},
    2: {"first_name": "beka", "word": "prius", "phone_num": "224-876-4321"},
}

print(class_dict[1]["phone_num"])