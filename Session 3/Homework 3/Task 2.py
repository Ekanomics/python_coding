# Task 2: Reverse a Word using for loop (please don’t reverse a string using word[::-1])
# Input:
# Enter a word: Python
# Output:
# Reversed Word: nohtyP

# word = input("Please enter the word: ")
# reversed_word = ""
# for i in range(len(word) -1, -1, -1):
#     reversed_word += word[i]
# print("Reversed word: ", reversed_word)




inp = input("Input: ")
reversed_word = ""

for i in range(len(inp), 0, -1):
    reversed_word += inp[i-1]
print(reversed_word)

