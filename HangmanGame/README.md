# Hangman Game

This is a simple implementation of the Hangman game in Python. The objective of the game is to guess the word chosen by the computer by suggesting letters within a certain number of guesses.

## How to Play

1. Start the Game: Run the Python script.
2. Guess a Letter: You will be prompted to guess a letter.
3. Check Guess: The program will check if the guessed letter is in the word.
   - If the guessed letter is in the word, it will be revealed in its correct positions.
   - If the guessed letter is not in the word, you will lose a life.
4. Repeat: Continue guessing letters until you either guess the word correctly or run out of lives.
5. Game Over: The game ends when you either guess the word or lose all your lives. The correct word will be displayed if you lose.

## Files

- `hangman.py`: The main script to run the game.
- `hangman_art.py`: Contains the ASCII art for the Hangman game stages and logo.
- `hangman_words.py`: Contains the list of words to be used in the game.

## Running the Game

Ensure you have Python installed on your system.
Clone the repository or download the script files.
Open a terminal and navigate to the directory containing the script files.
Run the script using the command: python hangman.py
