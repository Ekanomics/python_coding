#           PCEP preparation

1.
# list = [False, True, "2", 3, 4, 5]
# b = 0 in list
# print(b)



2.
# my_tuple[1] = my_tuple[1] + my_tuple[0]
#  Tuples are immutable
# That means, that once a tuple is created, it's elements cannot be changed


3.
# x = [0, 1, 2]    # [0, 1, 2]
# x.insert(0, 1)   # [1, 0, 1, 2] adds 1 as index 0
# del x[1]         # deletes index 1, so it becomes [1, 1, 2]
# print(sum(x))    # 4


4.
# list1 = [1, 3]
# list2 = list1
# list1[0] = 4
# print(list2)

# Answer: [4, 3]


5.
# data = ['Peter', 404, 3.03, 'Wellert', 33.3]
# print(data[1:3])

# Answer: [404, 3.03]


6.
# nums = [1, 2, 3]
# vals = nums
# del vals[1:2]

# Answer: B. nums and vals are of the same length
#         D. nums and vals refer to the same list


7.
# dct = {}
# dct['1'] = (1, 2)   # Добавляем в словарь ключ '1' со значением (1, 2)
# dct['2'] = (2, 1)   # Добавляем в словарь ключ '2' со значением (2, 1)

# # dct = {
# #     '1': (1, 2),
# #     '2': (2, 1)
# # }                     # Вот так выглядит пустой словарь после добавления в него новый ключей

# for x in dct.keys():            # Проходим по всем ключам словаря
#     print(dct[x][1], end='')    # Выводим второй элемент кортежа, связанного с ключом x
#                                 # end='' убирает пробелы и символы новой строки между выводами
#                                 # dct[x][1] — это второй элемент кортежа (индексация в Python начинается с 0).

# Answer: 21


8. 
# print(list('hello'))

# Answer: ['h', 'e', 'l', 'l', 'o']
# Here the string 'hello' is passed to to the list() function. So list() converts the string into a list, where each char becomes an individual element of the list.


9. 
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(a[::2])

# Answer: [1, 3, 5, 7, 9]


10.
# d = {}
# d[1] = 1
# d['1'] = 2
# d[1] += 1

# # dictionary now contains: d = {1: 2, '1': 2}, where we have 2 keys: 1 and '1' with values 2 and 2

# sum = 0

# for k in d:
#     sum += d[k]

# print(sum)

# Answer: 4


11.
# dict = {'one': 'two', 'three': 'one', 'two': 'three'}
# v = dict['one']

# for k in range(len(dict)):       # len(dict) возвращает количество элементов в словаре, то есть 3. Цикл выполняется 3 раза (для k = 0, k = 1, k = 2).
#     v = dict[v]

# print(v)

# Answer: two
# 


12. 
# nums = [3, 4, 5, 20, 5, 25, 1, 3]
# nums.pop(1)
# print(nums)

# Answer: [3, 5, 20, 5, 25, 1, 3]
# method pop() removes the element at the specified index. For ex: pop(1), deletes element under the index 1 in the list


13.
# Which of the following sentences is true?
# str1 = 'Peter'
# str2 = str1[:]      # В Python срез [:] создает поверхностную копию объекта. Для строк это означает, что создается новая строка с тем же содержимым.

# print(str1)
# print(str2)

# Answer: A. str1 and str2 are different (but equal) strings


14.
# The fact that tuples belong to sequence types means:

# Answer: D. they can be indexed and sliced like lists
# Tuples are immutable sequence types in Python, meaning they cannot be modified, and don't have methods like .append()


15.
# my_list = [3, 1, -1]
# my_list[-1] = my_list[-2]
# print(my_list)

# Answer: [3, 1, 1]


16. 
# data = ((1, 2),) * 7      ---> data = ((1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2))
# print(len(data[3:8]))     ---> counting elements from index 3 to the end of tuple: ((1, 2), (1, 2), (1, 2), (1, 2)), len calculating the length of the slice - 4 elements

# Answer: 4


17.
# data = {'Peter': 30, 'Paul': 31}
# print(list(data.keys()))              # data.keys() returns a view object of all the keys in the dict. 
                                        # list(data.keys()) converts this view of object into a list

# Answer: ['Peter', 'Paul']


18.
# tup = (1, ) + (1, )         # tup = (1, 1)
# tup = tup + tup             # tup = (1, 1, 1, 1)
# print(len(tup))

# Answer: 4


19.
# data = (1, 2, 4, 8)
# data = data[-2:-1]    # Slicing the tuple, start at index -2, which is 4. Then stop before -1. The result is - 4.
# data = data[-1]
# print(data)

# Answer: 4


20.
# my_list = [1, 2]

# for v in range(2):                          # Loop runs 2 times 
#     my_list.insert(-1, my_list[v])          # insert method inserts my_list[v] into the second to last posistion (-1 index)
#                                             # первая итерация (v=0), my_list[v] = my_list[0] = 1; insert(-1; 1) inserts the value 1 just before the last element)
#                                             # the list becomes: [1, 1, 2], second iteration (v=1) - becomes [1, 1, 1, 2]
# print(my_list)


21.
# data = [1, 2, 3, None, (), [], ]            # () - empty tuple, [] empty list
# print(len(data))

# Answer: 6 elements


22.
# A data structure described as LIFO is actually a:

# A: Stack
# Last in, first out - which is characteristic of a stack data structure. In a stack, the last element added is the first one to be removed

# LIFO - stack
# FIFO - queue

# stack = []  # Создаем пустой стек

# # Добавляем элементы в стек
# stack.append(1)  # [1]
# stack.append(2)  # [1, 2]
# stack.append(3)  # [1, 2, 3]

# # Удаляем элементы из стека
# print(stack.pop())  # Удалится 3 (последний добавленный)
# print(stack.pop())  # Удалится 2
# print(stack.pop())  # Удалится 1

# # Стек пуст



23.
# d = {'A': 1, 'B': 2, 'C': 3}
# print(d)
# d.clear()
# print(d)

# Answer: is d.clear(), is the only valid method for dict


24.
# data = {'one': 'two', 'two': 'three', 'three': 'one'}
# res = data['three']

# for i in range(len(data)):
#     res = data[res]

# print(res)

# Answer: one


25.
# data = {'name': 'Peter', 'age': 30}
# person = data.copy()
# print(id(data) == id(person))

# id() — это встроенная функция Python, которая возвращает уникальный идентификатор объекта. Этот идентификатор представляет собой адрес объекта в памяти.
# Метод .copy() создает новый объект словаря. Это означает, что data и person — это два разных объекта в памяти, даже если они содержат одинаковые данные.

# Answer: False


26.
# list = [4, 1, 7, 2, 'A']

# list.reverse()

# print(list)

# Answer: C. list.reverse()   ---> .reverse() method reverses the list in place, modifying the original list



27.
# data1 = '1', '2'    ---> tuple. becomes data1 = ('1', '2')
# data2 = ('3', '4')

# print(data1 + data2)

# Answer: ('1', '2', '3', '4')



28.
# data = (1, 2, 4, 8)
# data = data[1:-1]           # (2, 4)
# data = data[0]              # (2)
# print(data)



29.
# my_list = [3, 1, -2]
# print(my_list[my_list[-1]])

# Answer: 1



30.
# An alternative name for a data structure called a stack is:
#     LIFO



31.
# w = [7, 3, 23, 42]
# x = w[1:]             # x = [3, 23, 42]
# y = w[1:]             # y = [3, 23, 42]
# z = w                 # Here z assigned the ref to w, so any changes to z will directly modify w
# y[0] = 10             # y = [10, 23, 42]
# z[1] = 20             # z = [7, 20, 23, 42]
# print(w)

# Answer: [7, 20, 23, 42]



32.
# nums = []
# vals = nums
# vals.append(1)

# Answer: nums and vals are the same length. They both are two names for the same object



33.
# data = {'a': 1, 'b': 2, 'c': 3}
# print(data['a', 'b'])                     # в словаре такого кортеж ключа ['a', 'b'] не существует, есть отдельно ['a'] and ['b']

# Answer: error



34.
# L = [i for i in range(-1, -2)]      # In this case range starts at -1 and stops before -2, the range produces no numbers. As a result it produces an empty list
# print(L)

# Answer: D. zero



35.
# What is the output of the following snippet?
# my_list = [0, 1, 2, 3]
# x = 1
# for elem in my_list:
#     x *= elem
# print(x)

# Answer: 0



36.
# nums = [1, 2, 3]
# data = ('Peter',) * (len(nums) - nums[::-1][0])
# print(data)

# Answer: ()        ---> In Python, multiplying a tuple by 0 results in an empty tuple. ('Peter',) * 0 = 0



37.
# t1 = (1, 4, 9)
# t2 = ('A', 'D', 'Z')
# t3 = (True, False, None)
# t4 = (5.0, 7.5, 9.9)

# t1, t3 = t2, t4
# print(t1)

# Answer: C. ('A', 'D', 'Z')



38.
# data = ()
# print(data.__len__())             # __len__() = len()

# Answer: 0           


39.
# fruits1 = ['Apple', 'Pear', 'Banana']
# fruits2 = fruits1
# fruits3 = fruits1[:]

# fruits2[0] = 'Cherry'
# fruits3[1] = 'Orange'

# res = 0

# for i in (fruits1, fruits2, fruits3):
#     if i[0] == 'Cherry':
#         res += 1
#     if i[1] == 'Orange':
#         res += 10

# print(res)

# Answer: 12



40.
# data = (1,) * 3           # creates a tuple: (1, 1, 1)
# data[0] = 2               # tuples are immutable, elements cannot be modified
# print(data)

# Answer: Error 



41.
# list = [2, 7, 1, 4]
# list.sort()
# print(list)

# Answer: list.sort() ---> [1, 2, 4, 7]



42.
# nums = [1, 2, 3]
# vals = nums

# Answer: CD. nums and vals are different names of the same list, and have the same length



43.
# vals = [0, 1, 2]
# vals[0], vals[1] = vals[1], vals[2]

# Answer: doesn't change the list's length


44.
# data = ['abc', 'def', 'abcde', 'efg']
# print(max(data))

# Answer: efg               # ---> max() function in Python returns the largest item in an iterable or the largest. In our case it returns lixicographically e > d.



45.
# list.reverse() - this function does in-place reversal of objects in a list


46.
# my_list1 = [1, 2, 3]
# my_list2 = []
# for v in my_list1:
#     my_list2.insert(0, v)         #---> Метод insert(0, v) добавляет каждый новый элемент в начало списка my_list2, что приводит к обратному порядку элементов.
                                    #---> Если бы мы использовали append(v) вместо insert(0, v), то элементы добавлялись бы в конец списка, и результат был бы [1, 2, 3]. 
                                    # Но в данном случае используется insert(0, v), поэтому порядок обратный.
# print(my_list2)

# Answer: [3, 2, 1]


47.
# data = [10, 2, 1, 7, 5, 6, 4, 3, 9, 8]

# def find_high_low(nums):
#     nums.sort()                                                 # Список сортируется по возрастанию с помощью метода sort().
#     return nums[-1], nums[0]                                    # (nums[-1]) — это наибольшее число, (nums[0]) — это наименьшее число.

# high, low = find_high_low(data)                       # Функция find_high_low вызывается с аргументом data, Результат (кортеж из двух чисел) распаковывается в var high и low.

# print(
#     ('The highest number is {} ' +
#     'and the lowest number is {}').format(high, low)
# )



48.
# my_list = ['Mary', 'had', 'a', 'little', 'lamb']

# def my_list(my_list):
#     del my_list[3]
#     my_list[3] = 'ram'

# print(my_list(my_list))

# Answer: Error, TypeError
# Beacuse the name of the list is the same as the name of the function
# And 'function' object does not support item deletion



49.
# data = ['Peter', 'Mary', 'Paul']
# print(data[int(-1 / 2)])

# Answer: Peter



50.
# data = (1, 2, 3, 4)
# data = data[-2:-1]                    # Срез [-2:-1] извлекает элементы от -2 (включительно) до -1 (не включая).
# data = data[-1]
# print(data)

# Answer: 3



51.
# data = {1: 0, 2: 1, 3: 2, 0: 1}
# x = 0

# for _ in range(len(data)):
#     x = data[x]

# print(x)


# Answer: 0



52.
# list = ['Peter', 'Paul', 'Mary']

# def list(data):
#     del data[1]
#     data[1] = 'Jane'
#     return data

# print(list(list))


# Answer: Error 



53.
# data = {}
# data['2'] = [1, 2]
# data['1'] = [3, 4]
#                                     # После этого словарь выглядит вот так: {'2': [1, 2], '1': [3, 4]}
# for i in data.keys():
#     print(data[i][1], end=' ')      # end=' ', означает, что следующий вывод будет на той же строке через пробел.
#                                     # data['2'][1] возвращает второй элемент списка [1, 2], то есть 2.
#                                     # data['1'][1] возвращает второй элемент списка [3, 4], то есть 4.

# Answer: 2 4



54.
# data1 = (1, 2)
# data2 = (3, 4)
# [print(sum(x)) for x in [data1 + data2]]          # == print(sum((1, 2, 3, 4))) - here the sum function calculates the sum of the elements in the tuple

# Answer: 10



55.
# vals = [0, 1, 2]
# vals.insert(0, 1)           # after this operation value becomes = [1, 1, 2]
# del vals[1]

# print(vals)

# Answer: 4



56.
