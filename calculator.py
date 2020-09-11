#! usr/bin/env python3
import operator as op

OPERATORS = {
        '-': op.sub,
        '+': op.add,
        '/': op.truediv,
        '*': op.mul,
        '%': op.mod
}

try:
    a = int(input())
except ValueError:
    print('Please, enter integer')
    a = int(input())

action = input()

try:
    b = int(input())
except ValueError:
    print('Please, enter integer')
    b = int(input())

result = OPERATORS.get(action).__call__(a, b)
print(result)
