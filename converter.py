#! usr/bin/env python3

NAMES_FOR_UNITS = {
    'обороты': 'об или ob',
    'градусы': 'гр или deg',
    'радиан': 'рад или rad',
    'секстант': 'секстан, секстант или sct',
    'град': 'грд или grd',
    'минуты': 'мин или min',
    'секунды': 'сек или sec',
    'румб': 'рб или rb'
}

DEG_IN_OTH_UNITS = {
    'ob': 360,
    'deg': 1,
    'rad': 57.295779513,
    'sct': 60,
    'secst': 60,
    'grd': 0.9,
    'min': 0.0166666666666666666,
    'sec': 0.0002777777777777777,
    'rb': 11.25,
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


value = list(input())
num = []
unit = []
for el in value:
    if el.isnumeric() or el == '.':
        num.append(el)
    if el.isalpha():
        unit.append(el)

user_req = (float(''.join(num)), ''.join(unit))
try:
    conv_to_deg = DEG_IN_OTH_UNITS.get(user_req[1]) * user_req[0]
except TypeError:
    print('Unknown unit, please choose correct unit from list ant type it in commandline')
    print(NAMES_FOR_UNITS)
    unit_value = input()
    conv_to_deg = DEG_IN_OTH_UNITS.get(unit_value) / user_req[0]
    print(conv_to_deg)


