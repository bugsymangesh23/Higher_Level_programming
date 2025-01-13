#!/usr/bin/python3
"""Bagels, by Al Sweigart al@inventwithpython.com
 A deductive logic game where you must guess a number based on clues.
 View this code at https://nostarch.com/big-book-small-python-projects
 A version of this game is featured in the book "Invent Your Own
 Computer Games with Python" https://nostarch.com/inventwithpython
 Tags: short, game, puzzle
"""

import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    print('''Bagels, a deductive logic game.
     I am thinking of a {}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
When I say: That means:
Pico One digit is correct but in the wrong position.
Fermi One digit is correct and in the right position.
Bagels No digit is correct.For example, if the secret number was 248 and your guess was 843, the
clues would be Fermi Pico.'''.format(NUM_DIGITS))

# The main game loop
    while True:
        secret_num = getSecretNum() #stores secret number that player is to get
        print("I have thought of a number...")
        print(f"You have {MAX_GUESSES} attempts to get it.")
        numGuesses = 1
    while numGuesses <= MAX_GUESSES:
        guess = ''
# Keep looping until they enter a valid guess:
    while len(guess) != NUM_DIGITS or not guess.isdecimal():
        print('Guess #{}: '.format(numGuesses))
        guess = input('> ')

        clues = getClues(guess, secretNum)
        print(clues)
numGuesses += 1
if guess == secretNum:
break # They're correct, so break out of this loop.
if numGuesses > MAX_GUESSES:
print('You ran out of guesses.')
print('The answer was {}.'.format(secretNum))
