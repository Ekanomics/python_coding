# Task 4: Password Verification (Limited Attempts)
# secret password = Python123
# Input:

# Enter the password: hello
# Wrong password. Try again.

# Enter the password: python
# Wrong password. Try again.

# Enter the password: Python123
# Access Granted!


secret_password = "Python123"
attempts = 3
for attempt in range(attempts):
    user_pswd = input("Enter your password: ")
    if user_pswd == secret_password:
        print("Access Granted!")
        break
    else:
        print("Wrong password. Try again.")
else:
    print("Access denied, you have only 3 attempts")

    