import random
from colorama import init, Fore, Back
from game_graphics import header, win, lose
from words import animals, fruits, movies
import sys
import operator
import os


def clear_screen():
    """
    method for clearing the terminal.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def get_word(p_choice):
    word = random.choice(p_choice)
    return word.upper()


def game_menu():
    """
    Game menu, player can chose to start game, read the rules or exit.
    """
    clear_screen()
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


def show_rules():
    """
    Print rules of hangman for the player
    """
    clear_screen()
    print("""
    You must guess the word.
    Each right guess fills in the spaces.
    Each wrong guess equals a life lost.
    When you run out of lives, you die.
    Good luck
    """)
    while True:  
        user_choice = input("Press E to return to menu:\n")
        if user_choice.upper() == "E":
            game_menu()
        elif user_choice != "E":
            print(Fore.RED + "You must press E to exit." + Fore.WHITE)


def choose_category():
    """
    Player can chose category of words to guess from.
    """
    clear_screen()
    print("Select a category:")
    print("Press 1: " + Fore.RED + "Animals")
    print(Fore.WHITE + "Press 2: " + Fore.RED + "Fruits")
    print(Fore.WHITE + "Press 3: " + Fore.RED + "Movie Genres" + Fore.WHITE)
    while True:  
        user_choice = input("\n")
        if user_choice == "1":
            word = get_word(animals)
            play(word)
        elif user_choice == "2":
            word = get_word(fruits)
            play(word)
        elif user_choice == "3":
            word = get_word(movies)
            play(word)
        else:
            print("Please input 1, 2 or 3 to select a category")    
       

def play(word):
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
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You've already tried the letter " + Fore.RED + guess + Fore.WHITE)
            elif guess not in word:
                print("Sorry " + Fore.RED + guess + Fore.WHITE + " is not in the word.")
                lives -= 1
                guessed_letters.append(guess)
            else:
                print("Good guess " + Fore.BLUE + guess + Fore.WHITE + " is in the word.")
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
                print("You already guessed " + Fore.BLUE + guess + Fore.WHITE)
            elif guess != word:
                print(Fore.RED + guess + Fore.WHITE + " is not the right word")
                guessed_words.append(guess)
                lives -= 1
            else:
                guessed = True
                guess_word = word
        else:
            print("Not a valid guess")
        print(hangman_lives(lives))
        print(guess_word)
        print("\n")
    if guessed:
        clear_screen()
        print("Congratulations! You got the word.\n")
        print(win)
    else:
        clear_screen()
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