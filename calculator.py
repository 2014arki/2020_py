#! usr/bin/env python3
import operator as op

OPERATORS = {
        '-': op.sub,
        '+': op.add,
        '/': op.truediv,
        '*': op.mul,
        '%': op.mod,
        '**': op.pow,
        '^': op.pow
}

try:
    a = int(input())
except ValueError:
    print('Please, enter integer')
    a = int(input())

action = input()

if action not in ('**', '^'):
    try:
        b = int(input())
    except ValueError:
        print('Please, enter integer')
        b = int(input())
else:
    b = float(input())

result = OPERATORS.get(action).__call__(a, b)
print(result)
