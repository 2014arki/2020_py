#! usr/bin/env python3

NAMES_FOR_UNITS = {
    'cycle': 'ob',
    'degree': 'deg',
    'radian': 'rad',
    'sextant': 'sct or secst',
    'grad': 'grd',
    'minute': 'min',
    'second': 'sec',
    'rhumb': 'rb'
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
}


def conv_to_deg(val, unit):
    return val * DEG_IN_OTH_UNITS.get(unit)


def print_dict(dictionary):
    for key, val in dictionary.items():
        print(f'{key}: {val}')


print('Type value and units separated by whitespace. Choose unit signature from list')
print_dict(NAMES_FOR_UNITS)
user_req = list(input())
print('Choose unit to convert')
unit_to_convert = input()

num = []
unit_chars = []
for el in user_req:
    if el.isnumeric() or el == '.':
        num.append(el)
    if el.isalpha():
        unit_chars.append(el)

value = float(''.join(num))
unit = ''.join(unit_chars)

try:
    value_in_units = conv_to_deg(value, unit) / DEG_IN_OTH_UNITS.get(unit_to_convert)
except TypeError:
    print('Unknown units, please choose correct units from list ant type it in commandline.')
    print_dict(NAMES_FOR_UNITS)
    print('Units of request')
    unit = input()
    print('Units to convert')
    unit_to_convert = input()
    value_in_units = conv_to_deg(value, unit) / DEG_IN_OTH_UNITS.get(unit_to_convert)
print(f'{value_in_units} {unit_to_convert}')