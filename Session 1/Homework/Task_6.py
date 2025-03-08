# Task 6: Palindrome Checker
# Ask the user to enter a word and check whether it reads the same forward and backward (e.g., "madam" is a palindrome).

# The answer should return True or False


while True:
    word = input("Please enter the word: ")
    reversed_word = word[::-1]
    if reversed_word == word:
        print("Yay, it's a palindrome word, congrats you found one")
        break
    else:
        print("It's not a palindrome, enter he word again")


