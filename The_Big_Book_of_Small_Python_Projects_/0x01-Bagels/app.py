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

            if guess == secret_num:
                print('Congratulations!You guessed it right')
                break # They're correct, so break out of this loop.
    
    clues = getClues(guess, secret_num)
    print(clues)
    if numGuesses > MAX_GUESSES:
        print('You ran out of guesses.')
        print('The answer was {}.'.format(secret_num))

# Ask player if they want to play again. 
print('Do you wish to play again?(Yes or No)')
if not input('> ').lower().startswith('y'):
    break
print('Thanks for playing!')

# Random string for the guesses
def getSecretNum():
    numbers = list('0123456789') #list of digits 0-9
    random.shuffle(numbers) # shuffle numbers in random order

    # Get the first NUM_DIGITS digits in the list for the secret number:
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum +=(numbers[i])
    return secretNum

# Clues definition 
def getClues(guess, secretNum):
    if guess == secretNum:
        return 'You got it!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels' #No correct digits at all
    else:
        # sort clues into alphabetic order so that their order 
        # dont give info away
        clues.sort()
        # make a single string from the clues string
        return ''.join(clues)
    if __name__ == '__main__':
        main()
