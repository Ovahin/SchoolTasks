# Задача А:

times = int(input('Сколько раз повторить? '))
for i in range(0, times):
    print('Сообщение')


# Задача B:

count = 0
number = input('Введите число: ')
for i in range(0, len(number)):
    if number[i] == '1':
        count += 1
print(f'Единиц: {count}')
