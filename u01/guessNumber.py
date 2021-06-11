#!/usr/bin/env python3
#   A small script that implements "Guess My Number" in Python.
#   Without any exception handling and so on.
#
#   Example from courses made by Prof. Dr. Daniel F. Abawi and Michael B. Schmidt
#   htw saar, Saarbrücken, Germany
import random


# function that prints a welcomeMessage
def welcomeMessage():
    print("Welcome to my little game. I will choose a number between 1 and 100 and you have to guess it.")


# function to create a randomized number
def randomizeNumber():
    number = random.randint(1, 101)
    return number


welcomeMessage()        # calls the specific function (which prints the welcome message)
# welcomeMessage()      --> not executed, since in a comment
secretNumber = randomizeNumber()    # calls the specific function (which gives back a randomized number)
print('OK, I have chosen my secret number. Let\'s see how smart you are. Good luck.')


number_of_guesses = 0
guessedSuccessfully = False

while guessedSuccessfully == False:
    print('Please enter your guess (as a number): ')
    guess = int(input())
    number_of_guesses = number_of_guesses + 1
    if guess < secretNumber:
        print('your guess is too low')
    if guess > secretNumber:
        print('your guess is too high')
    if guess == secretNumber:
        guessedSuccessfully = True


if guessedSuccessfully == True:
    print('Congratulations! You guessed my secret number in ' + str(number_of_guesses) + ' tries!')