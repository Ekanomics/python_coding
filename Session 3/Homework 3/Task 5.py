# Task 5: Print a Word in a Pyramid Shape
# Input:
# Enter a word: CODE

# Output:
# C
# CO
# COD
# CODE


word = input("Enter the word: ")
for pyramid in range(1, len(word) + 1):  
    print(word[:pyramid])

