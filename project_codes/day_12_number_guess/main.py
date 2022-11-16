from random import randint
import art

def difficulty_level(number_attempts):
    attempts = number_attempts

    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess_number = int(input("Make a guess: "))
        if guess_number == number:
            print(f"You got it! The answer was {guess_number}")
            break
        else:
            if guess_number < number:
                print("Too low.")
            elif guess_number > number:
                print("Too high.")
            attempts -= 1
            if attempts == 0:
                print("You've run out of guesses, you lose.")
                break
            print("Guess again.")

print(art.logo)
print()
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100. Guess the number.")

number = randint(1, 100)
# print(f"Psst the correct answer is {number}")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == "easy":
    attempts =  10
    difficulty_level(attempts)
else:
    attempts = 5
    difficulty_level(attempts)
