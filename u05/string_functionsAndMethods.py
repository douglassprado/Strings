#!/usr/bin/env python3
#   Example from courses made by Prof. Dr. Daniel F. Abawi and Michael B. Schmidt
#   htw saar, Saarbrücken, Germany

s = 'abcdefghijklmnopqrstuvwxyz'

# please see https://docs.python.org/3/library/stdtypes.html#string-methods

# print the number of characters
print(len(s))

# return a string with all the cased characters converted to uppercase
print(s.upper())

# print the number of occurences of the substring
print(s.count('efg'))

s = '   This could be an user input with whitespace at the begin and/or end    '
print(s.strip())

# visit the above mentioned website for many more examples

# do also some hands on with the following methods on strings
s = '123ABC'
print('Is Alpha? ' + str(s.isalpha()))
print('Is Alpha or Numeric? '+ str(s.isalnum()))
print('Has only digits? '+ str(s.isdigit()))
print('Has only lower-cased characters? '+ str(s.islower()))
