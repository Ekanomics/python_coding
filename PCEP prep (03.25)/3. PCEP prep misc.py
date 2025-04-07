# from datetime import datetime

# def show_date() -> None:
#     print('This is the current time: ')
#     print(datetime.now())

# show_date()




# def greet(name):
#     print(f'Hello, {name}!')

# greet('Askar')
# greet('Amy')



# def add(a, b):
#     return a + b

# print(add(10, 13))




# class car:
#     def __init__(self, brand, power):
#         self.brand = brand
#         self.horsepower = power

#     def drive(self):
#         print(f'{self.brand} is driving')

#     def get_info(self):
#         print(f'{self.brand} with {self.horsepower} horsepower')

# Toyota: car = car('Toyota', 250)
# Toyota.drive()
# Toyota.get_info()


# bmw: car = car('BMW', 300)
# bmw.drive()
# bmw.get_info()





# x = 9
# y = 12
# result = x // 2 * 2 / 2 + y % 2 ** 3
# print(result)



# x = 1
# x = x == x
# Answer: True


# a = 10
# b = 20
# c = a>b
# print(not(c))
# Answer: True



# x = 1 + 1 // 2 + 1 / 2 + 2
# print(x)
# A: 3.5


# z = 3
# y = 7
# x = y == z and y > z or z > y and z != y
# print(x)
# A: False



# print(1/1)



# list1 = [3, 7, 23, 42]
# list2 = [3, 7, 23, 42]
# print(list1 is list2)
# print(list1 == list2)
# # A: False, True

# print(id(list1))
# print(id(list2))


# print(3*'abc'+'xyz')



# nums = [3, 7, 23, 42]
# alphas = ['p', 'p', 'm', 'j']

# print(nums is alphas)
# print(nums == alphas)

# nums = alphas

# print(nums is alphas)
# print(nums == alphas)

# print(nums)
# print(alphas)

# A:False, FAlse, True, True, ['p', 'p', 'm', 'j']



# x = 'Peter'
# y = 'Peter'
# res = x is y
# print(res)

# y = ''.join(['P', 'e', 't', 'e', 'r'])
# print(y)



# x, y, z = 3, 2, 1
# z, y, x = x, y, z
# print(x, y, z)



# x = 1
# print(++++x)



# x = 23 + 42
# y = '23' + '42'
# z = '23' * 7
# print(type(x))
# print(type(y))
# print(type(z))



# x = 2
# y = 6
# x += 2 ** 3
# x //= y //2 // 3
# print(x)



# res = str(bool(1) + float(12) / float(2))
# print(res)
# A: str(1 + 6.0) = '7.0'


# print('Mikeii' > 'Mikey')


# x = 2 ^ 3
# print(x)


# // - performs integer division


# y = 2 + 3 * 5.
# print(y)
# A: 17.0


# equal - '=='



# a = 1
# b = 0
# a = a ^ b
# b = a ^ b
# b = a ^ b
# print(a, b)
# 1, 0



# a = 1
# b = 0
# c = a & b     # True and False = False = 0
# d = a | b     # | - or = True or False = True = 1
# e = a ^ b     # 1 - True (Бит равен 1, если только один бит равен 1)
# print(c + d + e)
# A: 2




# x = float('23.42')
# print(x)
# print(bool(x) + True)



# print('Mike' > 'MIke')      #True
# Lowercase letters (a–z) have higher ASCII values than uppercase letters (A–Z)
# Therefore, 'm' > 'M', 'z' > 'Z', 'a' > 'A', etc.



# print(2 ** 3 ** 2 ** 1)         # 2 ** 9 = 512, from right to the left



# print('t' in 'Peter')
# print('is' in 'This IS Python code.')


# z = 2
# y = 1
# x = y < z or z > y and y > z or z < y
# print(x)
# A: True


# ** - exponentiation


# x = 0
# y = 1
# x = x ^ y
# y = x ^ y
# y = x ^ y
# print(x, y)
# A: 1 1



# x = True
# y = False
# z = False

# if x or y and z:
#     print('TRUE')
# else:
#     print('FALSE')

# Оператор and выполняется раньше, чем or!






# Basics:

#! - tell a Unix OS how to execute the contens of a Python file

# 4 fundamental elements that make a language - Alphabet, lexis, syntax and semantics

x = '\''
print(len(x))
