# Task 3
# Take an input of list of numbers, find and print the unique numbers.
# Input: [1, 2, 2, 3, 4, 4, 5]
# Output: 1, 3, 5


list_of_num = input("Input: ").split()

Output = []

for i in list_of_num:
    if i not in Output:
        Output.append(i)

output_str = ", ".join(Output)          #.join  -  превращает список, кортеж and etc. в одну строку

print("Output: ", Output)



