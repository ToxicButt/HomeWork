number_1 = int(input("Введи число: "))
deystv = input("Введи знак действия, например: + - * / : ")
number_2 = int(input("Введи второе число: "))
# Сложение
if deystv == '+':
    print("{} + {} = ".format(number_1, number_2))
    print(number_1 + number_2)
# Вычитание
elif deystv == "-":
    print("{} - {} = ".format(number_1, number_2))
    print(number_1 - number_2)
# Умножение
elif deystv == "*":
    print("{} * {} = ".format(number_1, number_2))
    print(number_1 * number_2)
# Деление
elif deystv == "/":
    print("{} / {} = ".format(number_1, number_2))
    print(number_1 / number_2)
else:
    print("Ты ввел что-то не так, попробуй ещё раз")


