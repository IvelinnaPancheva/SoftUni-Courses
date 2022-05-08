import random
import string
from hangmn_words_list import words


def get_valid_word(words):
    word = random.choice(words) #randomly selects a word from the list
    while " " in word or "-" in word:
        word = random.choice(words)
    return word


def hangman():
    word = (get_valid_word(words)).upper() # randomly selected word by the computer, string
    word_letters = set(word) # letters in the selected word, valid guesses
    alphabet = set(string.ascii_uppercase) # a set of the alphabet uppercase leters
    used_letters = set() # what the user has guessed = the correct guesses

    tries = 10
    # while condition - keeps iterating until either user wins (guesses the word) or has no more tries left
    while len(word_letters) > 0 and tries > 0:
        # inform user which letters are already used
        print(f"You have already used these letters \n{', '.join(used_letters)}")
        # display the current state of the word with the guessed letters and - for the unknown
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print(f"Current word is:\n{''.join(word_list)}")

        # user to enter input
        user_letter = input("Guess a letter:\n").upper() # user input defined in the function

        # letter input validations - if valid, but incorrect, if correct or if invalid
        if user_letter in (alphabet - used_letters): # => valid letter from alphabet, not yet used
            used_letters.add(user_letter)
            if user_letter in word_letters: # correct guess, letter in word
                word_letters.remove(user_letter)
            else: # valid, but incorrect guess, tries must be decremented by 1
                tries -= 1

        elif user_letter in used_letters:
            print("You have already used this letter. Please try again!")
        else: # input letter is not a valid letter from alphabet, nor it is used before
            print("Invalid input. Please enter a letter again!")
    # stops looping when len(word letters) == 0, all letters were guessed OR tries == 0 (no more tries left)
    # out of the loop, check which is the case
    if tries == 0:
        print(f"Sorry, no more tries left! The word was {word}.")
    else: # tries > 0, the user has won
        print(f"Congrats! You've guessed correctly the word {word}!")


hangman()