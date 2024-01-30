# Fermi_Pico_Bagel
Guess the number game with hints of Fermi, Pico, and Bagel, implemented in Python.

## Overview:
The Fermi-Pico-Bagel game is a simple yet entertaining guessing game implemented in Python. It's a variation of the classic "Guess the Number" game where the player tries to guess a randomly generated number within a certain range. However, instead of receiving direct clues about the guessed number's value, the player receives hints in the form of "Fermi," "Pico," and "Bagel."

## How to Play:
Setup: The game randomly selects a secret number within a specified range, without revealing it to the player.

Guessing: The player makes a guess by inputting a number within the same range.

Hints:
1. Fermi: If a guessed digit is in the correct position within the secret number, it's called a "Fermi."
2. Pico: If a guessed digit is in the secret number but not in the correct position, it's called a "Pico."
3. Bagel: If none of the guessed digits are present in the secret number, it's called a "Bagel."

Feedback: Based on the hints provided, the player refines their guesses to deduce the secret number.

Win/Lose: The player continues guessing until they correctly identify the secret number (win) or exhaust their attempts without guessing it (lose).

## Features:
Customizable Range: The game allows customization of the range within which the secret number is generated.
