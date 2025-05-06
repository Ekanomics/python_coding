# Session3 - classwork

# print(bin(10))
# print(bin(15))

# print(15 & 10)


# print(bin(20))
# print(bin(65))
# print(20 & 65)

# print(2<<1)   Left Shift operator
# # = 2*2

# print(3 << 5),  Right Shift Operator
# # (3 * 2 * 2 * 2 * 2 * 2)




#                           LOOPS


# print("Hello") * 10

# For <variable name for loop> in <sequence>
# <instruction>

# for char in "Hello":
#     print(char)

# Definition: A loop allows you to repeat a block of code multiple times without writing it again.
# Why use loops?: Automates repetitive tasks, simplifies code, and enhances efficiency. For example, processing lists of data, counting items, or searching through data.

# for char in "Hello":
#     # set of instructions
#     print(char + "lo")




# variable ----> a = 10
# iteratable ----> the vavlue constantly changes

# num = 10 it's just a number 10, it does not represent the numbers from 1-10

# for test in range(10):
#     print(test)
# # 9 != {0-9}

#       Class task 1
# print numbers from 0-100
# for number in range(101):
#     print(number)


#       Class task 2
# print only even number all the way to 100

# for number in range(100, 9, -2):
#     print(number)
# for num in range(11):
#     # range {0, 1, 2, 3, 4, 5 .. 10}
#     # iteratable num = 0
#     if num % 2 == 0:
#         print(num)



#       Class task 2.0
# Character counter
# Take an input of the word/sentence
# Calculate how many 'a' character are in the word/sentence

# input: akumosolutions -- a
# output: 1

# input: banana
# output: 3

# word = input("Please enter the word: ")
# counter = 0

# for letter in word:
#     if letter == "a":
#         counter = counter + 1

# print(counter)


# Instead of taking 'a', let the user choose the letter
# sentence or character should be case insensitive (hint:use lower() or upper())

# word = input("Please enter the word: ").lower()
# letter_inp1 = input("Please choose any letter 1: ").lower()
# letter_inp2 = input("Please choose any letter 2: ").lower()

# counter1 = 0
# counter2 = 0

# if len(letter_inp1) == 1 and len(letter_inp2) == 1:
#     for letter in word:
#         if letter == letter_inp1:
#             counter1 = counter1 + 1
#         elif letter == letter_inp2:
#             counter2 = counter2 + 1
    
#     print(f"{letter_inp1} = {counter1}")
#     print(f"{letter_inp2} = {counter2}")

# else:
#     print("Character input is more than 1, please do it again")



