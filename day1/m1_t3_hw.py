"""
Задача №3
В подъезде №1 пятиэтажного жилого дома 15 квартир.
Определить, на каком этаже этого подъезда находится
квартира с заданным номером.

Решить без использования if.

"""
# Ваш код
import math

appartment_num = int(input('Введите номер квартиры: '))
floor_num = math.ceil(appartment_num / 3)

print(f"Квартира на этаже №  {floor_num}")
