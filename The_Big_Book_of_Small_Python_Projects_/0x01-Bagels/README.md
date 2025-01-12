# Bagels Number guessing game

In Bagels, a deductive logic game, you 
must guess a secret three-digit number 
based on clues. The game offers one of 
the following hints in response to your guess: 
“Pico” when your guess has a correct digit in the 
wrong place, “Fermi” when your guess has a correct 
digit in the correct place, and “Bagels” if your guess 
has no correct digits. You have 10 tries to guess the 
secret number

This program uses not integer values but rather string 
values that contain numeric digits. For example, '426' is a different value 
than 426. We need to do this because we are performing string comparisons 
with the secret number, not math operations. Remember that '0' can be 
a leading digit: the string '026' is different from '26', but the integer 026 is 
the same as 26
