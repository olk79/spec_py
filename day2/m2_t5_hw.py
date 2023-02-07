'''
Задача №1
Дано натуральное число N. Если число N двузначное,
то найти сумму цифр числа. Если число N трехзначное,
то найти произведение ненулевых цифр числа,
иначе написать, что число неподходящее.

Если в 3-х значном и десятки и единицы нули, то выводим сотни.

In: 300
Out: 3

In: 405
Out: 20

In: 230
Out: 6

In: 67
Out: 13

In: 6
Out: 'число неподходящее'

In: 5678
Out: 'число неподходящее'
'''
length = res = i = 0
n = input("Введите натуральное число, двух или трёх значное ")

if len(n) in range(2, 4):
    while i < len(n):
        if len(n) == 2:
            res += int(n[i])
            expr_type = "Сумма"
        else:
            if (x := int(n[i])) > 0 and res > 0:
                res *= x
            else:
                res += x
            expr_type = "Произведение"
        i += 1
        length = len(n)
    print(f'{expr_type} {length}-х знакового числа = ', res)
else:
    print("Вы ввели недопустимое значение")
    exit()
