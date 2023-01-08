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

# ----- рекурсия
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


# ------ декоратор
# def mydickor(func):
#     def wrapper(*args):
#         for i in args:
#             if not isinstance(i, (int, float)):
#                 raise  TypeError
#         return func(*args)
#
#     return wrapper
#
# @mydickor
# def multiply (a, b):
#     return a * b
#
# print(multiply(1,3))


#
# На вход функции, поступает строка, на ее основании сформировать
# список, который будет содержать только слова, длина которых >=5


# numbers = input("")
# numbers = list(filter(lambda x: len(x) >=5, numbers.split()))
# print(numbers)
#

#  Написать функцию generate_password принимающая на вход 2 аргумента
# имя ресурса, длина пароля, функция должна генерировать пароль указанной длины
# с использованием букв и цифр и записывать его в глобальный словарь passwords
# имя ресурса - ключ, пароль - значения.
# from random import choice


#
# from random import choice, randint
# from string import ascii_letters, digits
#
# import password as password
#
#
# def generate_password(name, length):
#
#     for _ in range(length):
#         password += choice(ascii_letters + digits)
#         password[name] = password
# generate_password("telega",10)
# print(password)
#
# def sayhello():
#     print("hello")
#     print("boop")
#     print("and everbode")
#
# def square(x):
#     print('Квадрат числа',x,'=',x**2)
# for i in range(1,11):
#     square(i)
#
#
# def toxic(a,b):
#     return a + b
#
# print(toxic("abc","wmn"))

# turtle.title("Turtle Drawing")
# circle = turtle.Turtle()
# circle.shape("turtle")
# circle.pensize(5)
# circle.pencolor("cyan")
#
# circle.dot(20)
# circle.penup()
# circle.goto(0, -100)
# circle.pendown()
# circle.circle(100)
# # turtle.exitonclick()
# import turtle
#
# def pepes():
#     turtle.left(90)
#     turtle.pensize(10)
#     turtle.penup()
#     turtle.forward(100)
#     turtle.pendown()
#     turtle.pencolor("cyan")
#     turtle.begin_fill()
#     turtle.circle(70, 230)
#     turtle.pensize(10)
#     turtle.pencolor("cyan")
#
#     turtle.pencolor("cyan", )
#     turtle.forward(140)
#     turtle.seth(40)
#     turtle.forward(135)
#     turtle.pencolor("cyan")
#     turtle.right(5)
#     turtle.circle(70, 210)
#     turtle.pencolor("black")
#
#     turtle.seth(30)
#     turtle.fillcolor("cyan")
#     turtle.end_fill()
#     turtle.seth(-90)
#     turtle.pencolor("cyan")
#     turtle.pensize(3)
#     turtle.forward(50)
#     turtle.pencolor("black")
#
#     turtle.hideturtle()
#     turtle.done()
# pepes()