#!/usr/bin/env python3
#   Example from courses made by Prof. Dr. Daniel F. Abawi and Michael B. Schmidt
#   htw saar, Saarbrücken, Germany

userSelectionCorrect = False
while userSelectionCorrect == False:
    print('Available commands:')
    print('===================')
    print('add    Adds a new record')
    print('edit   Edits a record')
    print('\nPlease enter your selection:')
    userSelection = input()

    if userSelection == 'add':
        print("add selected")           # you may call a function that performs the action
        userSelectionCorrect = True     # important, to stop the loop
    elif userSelection == 'edit':
        print("edit selected")          # you may call a function that performs the action
        userSelectionCorrect = True     # important, to stop the loop
    else:
        # so the input was not valid
        print("***Your selection is invalid!***")

print('**End of the program**')