# Task 2
# Take an input and count the occurrences of each character.
# Input: programming
# Output: {'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 1, 'n': 1}

word = input("Please enter the word: ")

# print(list(word))

occur = {}                # creating empty dict
for i in word:            # here loop going through each character
    if i in occur:        # checking if we have (i) char in the dict{occur}
        occur[i] += 1     # if it's there we counting them +1
    else:
        occur[i] = 1      # if it's not in dict we just give it number 1

print(occur)

# we using [] in occur[], to get acccess to the value through the key