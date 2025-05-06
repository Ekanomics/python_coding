##### Task 6: Age Group Classifier
# Ask the user for their age and classify them into a group: (Age range is from 0 - 120)
# 0 - 12 → "Child"
# 13 - 19 → "Teenager"
# 20 - 59 → "Adult"
# 60 and above → "Senior Citizen"


age = int(input("Please share your age: "))
if age >= 0 and age <= 12:
    print("Child")
elif age >= 13 and age <= 19:
    print("Teenager")
elif age >= 20 and age <= 59:
    print("Adult")
else:
    print("Senior citizen")