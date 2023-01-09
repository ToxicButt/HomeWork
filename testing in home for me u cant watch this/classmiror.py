# бинарный поиск
# numbers = list(range(1,100))

# def benary_search(objs, target):
#     start = 0
#     end = len(objs)
#     i = (end+start) // 2
#     while objs[i] != target:
#         if objs[i] > target:
#             end = i
#         elif objs[i] > target:
#             start = i
#         i = (end + start) //2
#         return i
# print(benary_search(numbers, 100))

# def decimal_to_binary(decimal):
#     binary = ""
#     while decimal >0:
#         binary = f'{decimal % 2}' + binary
#         decimal //= 2
#     binary = f'{decimal}' + binary
#     return binary
#
#
# def binary_to_decimal(binary):
#     decimal = 0
#     for i in binary:
#         decimal *= 2
#         decimal += int(i)
#     return  decimal
#---- Задача Пайтон
# def shift_list(objs, shift):
#     if abs(shift) in range(len(objs)+1):
#         objs = objs[-shift: ] + objs[:-shift]
#     return objs
# print(shift_list([1,2,3,4,5,6,7,], 3))
# задание на убрать текст

# elemnets = [1,2,3, 'fdgh', 'wege', 34, 'gewrg']
# # elemnets = list(filter(lambda x: isinstance(x, str), elemnets))
# # print(elemnets)
# def string_filter(objs):
#     for i in range(len(objs) -1, -1, -1,):
#         if not isinstance(objs[i], str):
#             del [objs[i]]
#     return objs
# print(string_filter(elemnets))


# def reverse(objs):
#     for i in range(len(objs) // 2):
#         objs[i], objs[~i] = objs[~1], objs[i]
#     return objs
#
# print(reverse([1,2,3,4,5,6,7,8,9]))
#
# import random
# def fsort(x):
#     return x%2
# text = [random.randint(1, 10) for i in range(10)]
# text_1 = list(sorted(text, key=fsort))
# print(text_1)
#-------- сумма соседей
# def some_of_neighbors(numbers):
#     result = []
#     for i in range(len(numbers)):
#         if i < len(numbers) -1:
#             result.append(numbers[i -1]+ numbers[i+1])
#         else:
#             result.append(numbers[i - 1] + numbers[0])
#     return result
# print(some_of_neighbors([1,2,3,4,5]))
#


# на вход функции поступает простейшая химическая формула, напримнр C2H50H
# вернуть словарь где ключами выступают название элементов а значения колличество моллекул
# данного вещества ({"C":2, "H": 6, "O": 1})


#
# # -------- Задача на формулу
# def elements_count(formula:str):
#     formula += "1" if formula[-1].isalpha() else ""
#     formula = list(formula)
#     i = 0
#     while i < len(formula) -1:
#         if formula[i].isalpha() and not formula[i+1].isalpha():
#             formula.insert(i+1,"1")
#             i += 1
#         i +=1
#     formula = list(map(lambda x: int(x) if x.isdigit() else x, formula))
#     data = {}
#     for i in range(0, len(formula), 2):
#         if formula[i] not in data:
#             data[formula[i]] = formula[i+1]
#         else:
#             data[formula[i]] += formula[i+1]
#         return data
#
# print(elements_count("C2H5OH"))
# ------ задача тинкоф про кабинеты и как их расположить
# def get_cabinet_area(x1,y1,x2,y2,x3,y3,x4,y4):
#     max_x = max(x1,x2,x3,x4)
#     min_x = min(x1,x2,x3,x4)
#     max_y = max(y1,y2,y3,y4)
#     min_y = min(y1,y2,y3,y4)
#     length = max(max_x - min_x, max_y - min_y)
#     area = length ** 2
#     return area
# print(get_cabinet_area(6,6,8,8, 1, 8, 4,9))

# На вход функции поступает N целое положительное число
# вывести N первых простых чисел больше 0
#
# from math import sqrt
#
# n = int(input())
#
# i = 2
# while i <= sqrt(n):
#     if n % i == 0:
#         print("не простое число")
#         break
#     i += 1
# else:
#     print("Простое число")

# def get_prime_number(n):
#     prime_number = []
#     number = 1
#     while len(prime_number) < n:
#         for i in range(2,range//2 +1):
#             if not number % i:
#                 break
#         else:
#             n  -= 1
#             yield number
#         number +=1
#     else:
#         raise StopIteration
# prime = get_prime_number(5)
# for number in prime:
