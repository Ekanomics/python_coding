##### Task 4: Password Strength Checker
# Ask the user for a password input. Check and print:
# "Strong password" if the length is at least 8 characters and contains both letters and numbers.
# "Weak password" otherwise.

pswd = input("Please enter the passwrd: ")
if len(pswd) >= 8 and pswd.isdigit and pswd.isalpha:
    print("Strong password")
else:
    print("Weak password")

    