"""
Hangman game implementation.

@author xt0fer
@version 1.0.0
@date 5/27/21 11:02 AM
"""


class WordGuess:
    def __init__(self, secret_word='cat', max_wrong=6):
        self.secret_word = secret_word
        self.user_guesses_num = 0
        self.user_wrong_guesses = max_wrong
        self.guessed_letters = set()

    def show_help(self):
        print("Guess the secret word by entering one letter at a time.")
        print("Type 'quit' to exit, 'help' to show this message.")

    def display_progress(self):
        display = ' '.join([ch if ch in self.guessed_letters else '_' for ch in self.secret_word])
        print(display)

    def guess(self, letter):
        if len(letter) != 1:
            print("Please enter a single letter.")
            return
        letter = letter.lower()
        if letter in self.guessed_letters:
            print(f"You already guessed '{letter}'.")
            return
        self.guessed_letters.add(letter)
        self.user_guesses_num += 1
        if letter not in self.secret_word:
            self.user_wrong_guesses -= 1
            print(f"Wrong guess. Remaining wrong guesses: {self.user_wrong_guesses}")
        else:
            print("Good guess!")
        self.display_progress()

    def is_won(self):
        return all(ch in self.guessed_letters for ch in self.secret_word)

    def is_lost(self):
        return self.user_wrong_guesses <= 0


def main():
    print("Welcome to WordGuess (Type 'help' on how to play)")
    game = WordGuess()
    game.display_progress()

    while True:
        user_input = input("Enter a letter? (or 'quit'): ").strip()
        if not user_input:
            continue
        if user_input.lower() == 'quit':
            break
        if user_input.lower() == 'help':
            game.show_help()
            continue

        game.guess(user_input)

        if game.is_won():
            print(f"Congratulations! You guessed the word '{game.secret_word}' in {game.user_guesses_num} guesses.")
            break
        if game.is_lost():
            print(f"Game over. The word was '{game.secret_word}'.")
            break

    print("see ya")


if __name__ == '__main__':
    main()
