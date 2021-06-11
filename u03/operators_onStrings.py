#!/usr/bin/env python3
#   Example from courses made by Prof. Dr. Daniel F. Abawi and Michael B. Schmidt
#   htw saar, Saarbrücken, Germany

mymessage = 'Tea'
print(mymessage)

# concatenation
mymessage = mymessage + ' leaf'
print(mymessage)

# repeat
mymessage = 'Bee' * 3
print(mymessage)

# slice
mymessage = mymessage[::-1]
print(mymessage)

# XXX
mymessage = mymessage[0:3]
print(mymessage)

# calling a method from the class str
mymessage = mymessage.lower()
