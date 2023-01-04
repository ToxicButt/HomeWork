# def foo():
#     print("foo")
#
#
# foo()
# foo()
# def multiply(a, b):
#     c = a * b
#     return c, a, b
#
# res = multiply(2,10)
# print(multiply(6,2))
# def sum(*args):
#     s = 0
#     for i in args:
#         s += 1
#     return s
# print(sum(1,2,3,4,5))

# def bar(**kwargs):
#     print()

# def baz (a,b, c=5, *args, d=None):
#     print(a)
#     print(b)
#     print(c)
#     print(args)
#     print(d)
# baz(1,2,3,4,5,6,7,8,9)
# def foo(a, b=None):
#     if b is None:
#         b = []
#     b.append(a)
#     return b
# print(foo(4))
# print(foo(4))


# ----
# a = 5
#
# def foo():
#     a = 4
#     def bar():
#         a = 3
#         print(a)
#     bar()

# multiply = lambda a, b: a * b
# print(multiply(5, 6))
# words = ["hello", 'python', "Aple", "Abc"]
# words.sort(key=lambda x: x.lower())
# # ['hello'. 'python', 'aple', 'abc']
# print(words)

# a = 5
# def foo():
#     a = 4
#     def bar():
#         global a
#         print(a)
#     bar()
# foo()

# numbers = ['1','2',"3"]
# numbers = list(map(lambda x: int(x) **2, numbers))
# print(numbers)
# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
# print(numbers)
#
# numbers = [1,2,3,4,5,6,7,8,9]
# numbers = list(filter(lambda x: x % 2 ==0, numbers))
# print(numbers)
#
# ---zip заканчивает на самой короткой коллекции
# numbers = [1,2,3,4]
# text = "hello"
# t = (True, False, None)
# res = list(zip(numbers,text, t))
# print(res)



# keys = ("name", "age", "city")
# values = ('alex', 16, "minsk")
# dara = dict(zip(keys, values))
# print(dara)
# --- замыкание внизу
# def foo(a):
#     def bar(b):
#         return a * b
#     return bar
#
# res = foo(6)
# print(res)
# print(res(4))


# def multiply(a,b):
#     return  a*b
#
# def foo(func, a, b):
#     print(func(a,b))
#
# foo(multiply, 6,6)
#

# ---Конфигурирование
# def foo():
#     print("foo")
#
# def bar():
#     print("bar")
#
# def error():
#     print("error")
#
# a=1
# data = {
#     1: foo,
#     2: bar
# }
# data.get(a,error)()
# ----генератор
# users = [
#     ("alex", 32),
#     ("alex", 34),
#     ("alex", 35),
#     ("alex", 36),
#
# ]
# def get_users():
#     for user in users:
#         yield user
#
# res = get_users()
# for user in res:
#     print(user)


# numbers = [1,2,3,4,5,6, [4,5,67,8,9,9,], 3,56,7,8,[3,4,6,7,8,6,4,],2,2,4,6,7,8,4,[5,5,7,8,42,],6,94,2,1,3]

# def recurseve(numbers):
#     res = 1
#     for number in numbers:
#         if isinstance(number, (int, float)):
#             res *= number
#         elif isinstance(number, (list,tuple,set,frozenset)):
#             res *= recurseve(number)
#     return res
# print(recurseve(numbers))



