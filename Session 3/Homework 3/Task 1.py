# Task 1: Count Down from input number to 1
# Input: 10
# Output:
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1

num = int(input("Please enter the number: "))
for num in range(10, 0, -1):
    print(num)
