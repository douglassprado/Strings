#!/usr/bin/env python3
#   Example from courses made by Prof. Dr. Daniel F. Abawi and Michael B. Schmidt
#   htw saar, Saarbrücken, Germany

print('Bus schedule from A to B:')
hour = 8

while hour <= 12:
    print(f'\t{hour} o\'clock:')
    minutes = 7

    while minutes <= 59:
        print(f'\t\t{hour:02}:{minutes:02}', end='')    # uses tabs and does not linebreak at the end
        minutes = minutes + 15

    print('')       # to have a line break after the inner loop
    hour = hour + 1