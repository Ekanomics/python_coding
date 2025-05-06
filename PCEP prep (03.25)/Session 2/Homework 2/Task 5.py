##### Task 5: Number Type Identifier
# Take a single integer input and classify it as follows:
# If it’s positive and even, print "Positive Even"
# If it’s positive and odd, print "Positive Odd"
# If it’s negative and even, print "Negative Even"
# If it’s negative and odd, print "Negative Odd"
# If it’s zero, print "The number is zero"

integer = int(input("Please enter a single integer: "))
if integer > 0 and integer % 2 == 0:
    print("Number is positive and even")
elif integer > 0 and integer % 2 != 0:
    print("Number is positive and odd")
elif integer < 0 and integer % 2 == 0:
    print("Number is negative and even")
elif integer < 0 and integer % 2 != 0:
    print("Number is negative and odd")
else:
    print("Number is zero")

