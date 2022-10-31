import random
from colorama import init, Fore, Back
from game_graphics import header, win, lose
from words import animals, fruits, movies
import sys
import operator
import os

def clear_screen():
    os.system("cls")

def get_word(p_choice):
    word = random.choice(p_choice)
    return word.upper()

# if else statement for players choice of category here

def game_menu():
    """
    Game menu, player can chose to start game, read the rules or exit
    """
    print(header)
    print ("Press " + Fore.RED + "1" + Fore.WHITE +
           " to start the game")
    print ("Press " + Fore.RED + "2" + Fore.WHITE +
           " to read the rules")
    print("Press " + Fore.RED + "3" + Fore.WHITE +
          " to exit game")
    while True:
        user_choice = input("\n")
        if user_choice == "1":
            choose_category()
        elif user_choice == "2":
            show_rules()
        elif user_choice == "3":
             sys.exit()
        else:
            print("Must choose 1, 2 or 3 !")


def choose_category():
    """
    Player can chose category of words to guess from.
    """
    clear_screen()
    print("Select a category:")
    print("Press 1: " + Fore.RED + "Animals")
    print(Fore.WHITE + "Press 2: " + Fore.RED + "Fruits")
    print(Fore.WHITE + "Press 3: " + Fore.RED + "Movie Genres")

which = get_word(animals)

print(which)

def play(word):
    guess_word = "_ " * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    lives = 6
    print("Let's play!")
    print(display_hangman(lives))
    print(guess_word)
    print("\n")
    while not guessed and lives > 0:
        guess = input ("Please guess a letter or a word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You've already tried this one ", guess)
            elif guess not in word:
                print("Your guess is not in the word.")
                lives -= 1
                guessed_letters.append(guess)
            else:
                print("Good guess", guess, "is in the word.")
                guessed_letters.append(guess)
                word_as_list = list(guess_word)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                guess_word = "".join(word_as_list)
                if "_" not in guess_word:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed", guess)
            elif guess != word:
                print(guess, "is not the right word")
                guessed_words.append(guess)
                tries -= 1
            else:
                guessed = True
                guess_word = word
        else:
            print("Not a valid guess")
            print(display_hangman(lives))
            print(guess_word)
            print("\n")
    if guessed:
        print("Congratulations! You got the word.\n")
        print(win)
    else:
        print("Sorry. You're out of lives.\n")
        print(lose)



def hangman_lives(lives):
    """
    Displays hangman graphic based on lives left
    """
    lives_left = [
        """
        ___________
        |/        |
        |         O
        |        /|\\
        |         |
        |        / \\
        |\\
        ========
        """,
        """
        ___________
        |/        |
        |         O
        |        /|\\
        |         |
        |        /
        |\\
        ========
        """,
        """
        __________
        |/        |
        |         O
        |        /|\\
        |         |
        |
        |\\
        ========
        """,
        """
        __________
        |/        |
        |         O
        |        /|
        |         |
        |
        |\\
        ========
        """,
        """
        __________
        |/        |
        |         O
        |         |
        |         |
        |
        |\\
        ========
        """,
        """
        __________
        |/        |
        |         O
        |
        |
        |
        |\\
        ========
        """,
        """
        __________
        |/
        |
        |
        |
        |
        |\\
        ========
        """
    ]
    return lives_left[lives]

def main():
    game_menu()

main()