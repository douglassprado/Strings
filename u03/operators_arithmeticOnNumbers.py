#!/usr/bin/env python3
#   Example from courses made by Prof. Dr. Daniel F. Abawi and Michael B. Schmidt
#   htw saar, Saarbrücken, Germany

print('Here are some arithmetic operators on numbers:')
# to give variable x an initial value; an assignment
x = 4
print("x =", x)

# addition
x = x + 2
print('x = x + 2')
print('x has now the value', x, "and it's type is", type(x))

# multiplication
x = x * 2.5
print('\nx = x * 2.5')
print('x has now the value', x, "and it's type is", type(x))

# division (real)
x = x / 2
print('\nx = x / 2')
print('x has now the value', x, "and it's type is", type(x))

# division (integer)
x = x // 2
print('\nx = x // 2')
print('x has now the value', x, "and it's type is", type(x))

# remainder
x = x % 2
print('\nx = x % 2')
print("x has now the value", x, "and it's type is", type(x))

# watch this
print('\nWatch my arithmetic skills:')
a = 0.7 + 0.3 - 0.2
print('0.7 + 0.3 - 0.2 =', a, "and it's type is", type(a))

b = 0.7 + 0.1
print('0.7 + 0.1 =', b, "and it's type is", type(b))

print('\nNow try yourself with arithmetic operators on numbers, i.e. in the Python console.')