# Hangman game

import random
from hangman_words import *
from hangman_art import *



def hangman():
    print(f"{' '.join(display)}")
    lives = 6
    active = True
    while active:
        guess = input("Guess a letter: ").lower()

        if guess in display:
            print(f"You've already guessed letter {guess}.")

        for letter in range(len(chosen_word)):
            if chosen_word[letter] == guess:
                display[letter] = guess
        print(f"{' '.join(display)}")

        if guess not in chosen_word:
            print(f"You guessed letter {guess}, that's not in the word. You lose a life.")
            lives -= 1
            if lives == 0:
                print("You are a dead man.You lose.")
                print(f"The word is {chosen_word}")
                active = False

        if "_" not in display:
            print("You win. You are saved.")
            active = False

        print(stages[lives])

game_active = True
while game_active:
    print(logo)

    print("You are about to be hanged. But you have a chance to escape death if you could guessed all"
        " the letters in a missing word. You have 6 chances, if you used all 6 chances, you lose and die.")

    chosen_word = random.choice(word_list)
    # print(f"pssst the word is {chosen_word}")

    display = []
    for letter in chosen_word:
        display.append("_")

    hangman()

    repeat = input("Want to play again? Type 'yes' or 'no'\n")
    if repeat == "no":
        game_active = False
        print("See ya.")
