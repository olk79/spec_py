"""
Задача №4. Посчитать размер вклада на депозите за несколько лет.

Вход:
размер начального вклада (от 100 до 1_000_000 рублей)(float),
годовой процент начисления(от 1 до 20)(float) с ежегодной капитализацией,
количество лет по вкладу(от 1 до 100)(int).
Интервалы для чисел включительно

Выход:
Проверить введеные данные и посчитать итоговую сумму на счету.
Если данные неверные, то вывести сообщение об этом.
! Циклы еще не придумали, а if уже придумали.
"""
deposit = float(input("Введите размер депозита от 100 до 1_000_000 рублей "))
if (deposit < 100.0 or deposit > 1000000.0):
    print("Вы ввели недопустимое значение")
    quit()

percentage_per_year = float(
    input("Введите процент начисления от 1 до 20 % "))
if (percentage_per_year < 1 or percentage_per_year > 20):
    print("Вы ввели недопустимое значение")
    quit()

years_depo = int(input("Введите количество лет от 1 до 100 лет "))
if (years_depo < 1 or years_depo > 100):
    print("Вы ввели недопустимое значение")
    quit()
elif years_depo == 1:
    years_format = 'год'
elif years_depo > 1 and years_depo < 4:
    years_format = 'года'
elif years_depo > 4:
    years_format = 'лет'

# Вычисляем размер депозита с капитализацией

S = deposit * (1 + percentage_per_year / 100) ** years_depo

print(
    f'Размер вашего вклад за период {years_depo} {years_format} составит '
    f'{S:.2f} рублей')

