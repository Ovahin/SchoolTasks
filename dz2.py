# Задача С

# Запрашиваем у пользователя данные и превращаем их в число, чтобы Python понимал, что это число, а не строка:
number = int(input('Введите число: '))
# Получаем первую цифру (разряд едениц), беря остаток от деления на 10:
e = number % 10
# Получаем вторую цифру (разряд десятков), беря остаток от деления количества полных десяток на 10 (сложна):
d = (number // 10) % 10
# Получаем третью цифру (разряд сотен), просто беря количестов полных сотен:
s = number // 100
# Сравниваем все числа между собой и выводим наибольшее:
print('Наибольшая цифра:', max(e, d, s))