# Task 4
# You are given two dictionaries where the keys represent item names and the values represent their respective counts
# Input: 
# dict1 = {"apple": 3, "banana": 5, "orange": 2}
# dict2 = {"banana": 2, "orange": 4, "grape": 6}

# Output: 
# {
#     "apple": 3,   # Only in dict1
#     "banana": 7,  # 5 (from dict1) + 2 (from dict2)
#     "orange": 6,  # 2 (from dict1) + 4 (from dict2)
#     "grape": 6    # Only in dict2
# }


dict1 = {"apple": 3, "banana": 5, "orange": 2}
dict2 = {"banana": 2, "orange": 4, "grape": 6}

sum_of_dict = {}

for fruit, value in dict1.items():
    sum_of_dict[fruit] = value

for fruit, value in dict2.items():
    if fruit in sum_of_dict:
        sum_of_dict[fruit] += value
    else:
        sum_of_dict[fruit] = value

print(sum_of_dict)