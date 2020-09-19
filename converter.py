#! usr/bin/env python3

NAMES_FOR_UNITS = {
    'обороты': 'об',
    'градусы': 'гр',
    'радиан': 'рад',
    'секстант': 'секстан, секстант',
    'град': 'грд',
    'минуты': 'мин',
    'секунды': 'сек',
    'румб': 'рб'
}

DEG_IN_OTH_UNITS = {
    'об': 360,
    'гр': 1,
    'рад': 57.295779513,
    'секстант': 60,
    'секстан': 60,
    'грд': 0.9,
    'мин': 0.0166666666666666666,
    'сек': 0.0002777777777777777,
    'рб': 11.25
}


def convert_to_deg(val, unit):
    return value * DEG_IN_OTH_UNITS.get(unit)

print('Напишите число и единицу измерения, разделенные пробелом')
value = list(input())
print('Напишите единицы, в которые хотите конвертировать')
units_to_convert = input()
num = []
unit = []
for el in value:
    if el.isnumeric() or el == '.':
        num.append(el)
    if el.isalpha():
        unit.append(el)

value = float(''.join(num))
unit = ''.join(unit)

try:
    convertion = convert_to_deg(value, unit=unit) / DEG_IN_OTH_UNITS.get(units_to_convert)
except TypeError:
    print('Неверные единицы измерения. Выберите единицы измерения из списка ниже')
    print(NAMES_FOR_UNITS)
    print('Введите единицы, в которых измеряется Ваш запрос')
    unit = input()
    print('Введите единицы, в которые Вы хотите конвертировать')
    units_to_convert = input()
    convertion = convert_to_deg(value, unit=unit) / DEG_IN_OTH_UNITS.get(units_to_convert)
    print(conv_to_deg)


