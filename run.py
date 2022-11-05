import random
import sys
import os
from colorama import Fore
from game_graphics import header, win, lose
from words import animals, fruits, movies


def clear_screen():
    """
    method for clearing the terminal.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def get_word(p_choice):
    """
    Picks a random word from the list based on the player's choice.
    """
    word = random.choice(p_choice)
    return word.upper()


def game_menu():
    """
    Game menu, player can chose to start game, read the rules or exit.
    """
    clear_screen()
    print(header)
    print("Press " + Fore.RED + "1" + Fore.WHITE +
          " to start the game")
    print("Press " + Fore.RED + "2" + Fore.WHITE +
          " to read the rules")
    print("Press " + Fore.RED + "3" + Fore.WHITE +
          " to exit game")
    while True:
        try:
            user_choice = int(input("\n"))
            if user_choice == 1:
                choose_category()
            elif user_choice == 2:
                show_rules()
            elif user_choice == 3:
                sys.exit()
            elif user_choice != 1 or 2 or 3:
                print("Must choose 1, 2 or 3")
        except ValueError:
            print("You must choose " + Fore.RED + "NUMBERS" + Fore.WHITE +
                  " 1, 2 or 3")


def show_rules():
    """
    Print rules of hangman for the player
    """
    clear_screen()
    print("""
Rules of the game:\n
You must guess the word to win.
Each right guess fills in the spaces.
Each wrong guess equals a life lost.
If you guess the word, you live.
If you run out of lives, you die.
Good luck.
    """)
    while True:
        user_choice = input("Press M to return to Menu or P to Play:\n")
        if user_choice.upper() == "M":
            game_menu()
        elif user_choice.upper() == "P":
            choose_category()
        else:
            print(Fore.RED + "You must press M or P." + Fore.WHITE)


def choose_category():
    """
    Player can chose category of words to guess from.
    """
    clear_screen()
    print("Select a category:")
    print("\n")
    print("Press 1: " + Fore.RED + "Animals")
    print(Fore.WHITE + "Press 2: " + Fore.RED + "Fruits")
    print(Fore.WHITE + "Press 3: " + Fore.RED + "Movie Genres" + Fore.WHITE)
    print("\n")
    print("Press 0 to exit to Menu")
    while True:
        try:
            user_choice = int(input("\n"))
            if user_choice == 1:
                word = get_word(animals)
                play(word)
            elif user_choice == 2:
                word = get_word(fruits)
                play(word)
            elif user_choice == 3:
                word = get_word(movies)
                play(word)
            elif user_choice == 0:
                game_menu()
            elif user_choice != 1 or 2 or 3 or 0:
                print("Must choose 1, 2, 3 or 0")
        except ValueError:
            print("Please only use " + Fore.RED + "NUMBER"
                  + Fore.WHITE + " from the choices given above.")


def play(word):
    """
    Runs the actual hangman game.
    """
    clear_screen()
    guess_word = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    lives = 6
    print("Let's play!")
    print(hangman_lives(lives))
    print(guess_word)
    print("\n")
    while not guessed and lives > 0:
        guess = input("Please guess a letter or a word: \n").upper()
        clear_screen()
        if len(guess) == 1 and guess.isalpha():
            """
            If the user guesses a letter.
            """
            if guess in guessed_letters:
                print("You've already tried the letter "
                      + Fore.RED + guess + Fore.WHITE)
            elif guess not in word:
                print("Sorry " + Fore.RED + guess + Fore.WHITE +
                      " is not in the word.")
                lives -= 1
                guessed_letters.append(guess)
            else:
                print("Good guess " + Fore.BLUE + guess + Fore.WHITE +
                      " is in the word.")
                guessed_letters.append(guess)
                word_as_list = list(guess_word)
                indices = [i for i, letter in enumerate(word)
                           if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                guess_word = "".join(word_as_list)
                if "_" not in guess_word:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            """
            If the player guesses a word, same length as the hidden word
            """
            if guess in guessed_words:
                print("You already guessed " + Fore.BLUE + guess + Fore.WHITE)
            elif guess != word:
                print(Fore.RED + guess + Fore.WHITE + " is not the right word")
                guessed_words.append(guess)
                lives -= 1
            else:
                guessed = True
                guess_word = word
        else:
            """
            For any other inputs
            """
            print("Not a valid guess")
        print(hangman_lives(lives))
        if lives > 1:
            print("You have " + Fore.RED + str(lives) + Fore.WHITE +
                  " chances left.")
        elif lives == 1:
            print(Fore.RED + "This is your last chance." + Fore.WHITE)
        print("You've used: " + Fore.BLUE + " ".join(guessed_letters)
              + Fore.WHITE)
        print(guess_word)
        print("\n")
    if guessed:
        clear_screen()
        print("Congratulations! You got the word.")
        print(win)
        play_again()
    else:
        clear_screen()
        print("Sorry. You're out of lives. The word was: " + word)
        print(lose)
        play_again()


def play_again():
    """
    Ask the player if they would like to play again.
    """
    while True:
        replay = input("""
Press P to play again. Press M to exit to menu.\n
""").upper()
        if replay == "P":
            choose_category()
        elif replay == "M":
            game_menu()
        else:
            clear_screen()
            print("Please only use prompted inputs.")


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


game_menu()
