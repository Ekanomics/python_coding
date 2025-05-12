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
import bisect
sorted_list = [1, 2, 4, 5]
bisect,insort(sorted_list, 3)
print(sorted_list)
