# --------------------1)
# funcs = []
# for i in range(3):
#     funcs.append(lambda: i)

# results = [f() for f in funcs]
# print(results)

# # [2, 2, 2]

# In Python, lambda is a way to define anonymous functions (functions without a name) in a single line.
# It works like a mini version of def, but is commonly used for short, throwaway functions.

# lambda: i             same thing as below ->

# def some_func():
#     return i



# --------------------2)
# def f(key, val, d={}):
#     d[key] = val
#     return d
# f('a', 1)
# f('b', 2)
# print(f('c', 3)['a'])

# 1



# --------------------3)
# import bisect
# sorted_list = [1, 2, 4, 5]
# bisect,insort(sorted_list, 3)
# print(sorted_list)




# --------------------4)
# from functools import reduce
# numbers = [1, 2, 3, 4]
# result = reduce(lambda x, y: x + y, numbers)
# print(result)

# 10

# The reduce() function is part of the functools module. It is used to apply a binary function (a function that takes two arguments) 
# cumulatively to the items of an iterable, from left to right, reducing the iterable to a single value.
# A lambda function is defined, which takes two arguments (x and y) and returns the sum (x + y). 
# This is the function that reduce() will apply cumulatively to the elements in the list.



# --------------------5)
# import heapq
# heap = [3, 1, 4, 5, 2]
# heapq.heapify(heap)
# heapq.heappush(heap, 6)
# print(heap)

# [1, 2, 4, 5, 3, 6]




# --------------------6)
# data = [(1, 3), (3, 1), (2, 2)]                         # list of 3 tuples, each tuple has 2 integers
# sorted_data = sorted(data, key=lambda x: x[1])          
# print(sorted_data)

# lambda x: x[1] means: for each tuple x, use the second element (x[1]) as the sorting key.
# (1, 3) → 3 ; (3, 1) → 1; (2, 2) → 2
# Now, sort based on these values: 1, 2, 3
# So the sorted order becomes:
# [(3, 1), (2, 2), (1, 3)]