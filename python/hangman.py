from person import Person
from person_interface import PersonInterface

class WordGuess:
    def __init__(self, player, secret_word='steelers', max_wrong=8):
        self.player = player
        self.secret_word = secret_word
        self.user_guesses_num = 0
        self.user_wrong_guesses = max_wrong
        self.guessed_letters = set()

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
            print(f"Oops. Remaining wrong guesses: {self.user_wrong_guesses}")
        else:
            print("Awesome guess!")
        self.display_progress()

    def is_won(self):
        return all(ch in self.guessed_letters for ch in self.secret_word)

    def is_lost(self):
        return self.user_wrong_guesses <= 0

def main():
    print("Welcome to WordGuess")
    player = Person()

    print(f"\nHello {player.get_first_name()} {player.get_last_name()}!")
    game = WordGuess(player)
    game.display_progress()

    

    while True:
        user_input = input("Enter a letter? (or 'quit'): ").strip()
        if not user_input:
            continue
        if user_input.lower() == 'quit':
            break

        game.guess(user_input)

        if game.is_won():
            print(f"Congratulations! You guessed the word '{game.secret_word}' in {game.user_guesses_num} guesses.")
            break
        if game.is_lost():
            print(f"Aww Jeez. Game over. The word was '{game.secret_word}'.")
            break

    print(f"Thanks for playing, {player.get_first_name()}!")


if __name__ == '__main__':
    main()
