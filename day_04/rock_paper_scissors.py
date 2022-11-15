# Rock Paper Scissors

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game = [rock, paper, scissors]

# set the code input for the ai

ai_player = random.randint(0, 2)

# set and get the user_player's input

user_player = int(input("What do you choose?\nType 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
if user_player > 2 or user_player < 0:
    print("Game over. You type an invalid number.")
else:
    print()
    user_player_choice = game[user_player]
    print(f"You chose:\n{user_player_choice}")

    # display ai's choice
    print()
    ai_player_choice = game[ai_player]
    print(f"Computer chose:\n{ai_player_choice}")

    # calculate results

    if user_player == ai_player:
        print("It's a draw")
    elif user_player == 0:
        if ai_player == 2:
            print("You win.")
        else:
            print("You lose.")
    elif user_player == 1:
        if ai_player == 0:
            print("You win.")
        else:
            print("You lose.")
    elif user_player == 2:
        if ai_player == 1:
            print("You win.")
        else:
            print("You lose.")
