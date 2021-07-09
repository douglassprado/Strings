#!/usr/bin/env python3
#   Example from courses made by Prof. Dr. Daniel F. Abawi and Michael B. Schmidt
#   htw saar, Saarbrücken, Germany

# using variables inside a formatted string
print('using variables inside a formatted string, part 1')
name = 'Tim'
age = 27
print(f'{name} is {age} years old.')

# using variables inside a formatted string
print('\nusing variables inside a formatted string, part 2')
x = 47
y = 23
result = x * y
print(f'The result of {x}*{y} is {result}')

# some examples of formatted values on numbers
print('\nsome examples of formatted values on numbers')
floatNumber = 1234567.890123    # be aware of the dot (no comma!)
print(f'{floatNumber:,.2f}')
print(f'{floatNumber:,>7.4f}')
print(f'{floatNumber:>7.2f}')

number1 = 456000
number2 = 123456789
print(f'{number1:>9d}')
print(f'{number2:>9d}')

myFraction = 1/7
print(myFraction)
print(f'{myFraction:.2}')