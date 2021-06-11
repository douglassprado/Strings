#!/usr/bin/env python3
#   Example from courses made by Prof. Dr. Daniel F. Abawi and Michael B. Schmidt
#   htw saar, Saarbrücken, Germany

print('Here are some operators on strings:')
mymessage = 'Tea'
print(mymessage)

# concatenation
mymessage = mymessage + ' leaf'
print(mymessage)

# repeat
mymessage = 'OneTwoThree' * 3
print(mymessage)

# range slice
mymessage = mymessage[0:4]
print(mymessage)

# slice
mymessage = mymessage[1]
print(mymessage)

# calling a method from the class str
mymessage = 'The flight code from Hong Kong to Frankfurt is LH797.'
print(mymessage)
print(mymessage.lower())

print('\nNow try yourself with operators on strings, i.e. in the Python console.')