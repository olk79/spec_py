"""
Задача №2
Напишите программу, определяющую количество уникальных символов в строке.
Вывести список символов и количество.

Например, в строке Hello, World! содержится десять
уникальных символов, а в строке zzz – один.
In: zzz
Out: [z], 1

In: Hello, World!
Out: ['H', ...., '!'], 10

!set еще не придумали
"""

in_str = input('Введите строку: ')

res = [simbol for simbol in in_str if in_str.count(simbol) == 1]
print(f'Список символов {res}, количество: {len(res)} ')

