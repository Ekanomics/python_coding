            # Classwork 2


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


word = input("Enter the word: ")
length = len(word)
if length > 10:
    print("THAT'S A LONG WORD")
else:
    print(f"The word has {length} characters")

