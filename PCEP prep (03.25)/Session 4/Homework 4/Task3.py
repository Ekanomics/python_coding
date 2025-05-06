# Task 3: Find the Longest Word in a List
# Ask the user to enter a list of words. Find and print the longest word from the list.
# Example:
# Enter words: Python Java JavaScript C  
# Longest word: JavaScript  


lst = input("Enter words: ").split()


# Longest = ""
# for i in lst:
#     if len(i) > len(Longest):
#         Longest = i
# print("Longest word: ", Longest)
# or

longest = max(lst, key=len)
print("Longest word: ", longest)
