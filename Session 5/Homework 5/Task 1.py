# Task 1
# Given a dictionary of students and their scores, print only the students who scored more than 50.
# Dictionary: students = {"Alice": 45, "Bob": 78, "Charlie": 52, "David": 33}
# Output: Bob : 78, Charlie : 52

students = {"Alice": 45, "Bob": 78, "Charlie": 52, "David": 33}
for name, score in students.items():
    if score > 50:
        print(f"{name}: {score}", end=", ")
print(end='\n')

