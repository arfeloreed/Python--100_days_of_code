import os
from random import *
from art import *

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def calculate_score(cards_list):
    """Takes the list of cards and returns its total sum"""
    score = sum(cards_list)
    if score == 21 and len(cards_list) == 2:
        score = 0
    if score > 21 and 11 in cards_list:
        card = cards_list.index(11)
        cards_list[card] = 1
        score = sum(cards_list)
    return score

def check_winner(score_user, score_computer, cards_user, cards_computer):
    """Compares score_user and score_computer and checks the winner"""
    print(f"Your final cards: {cards_user}, final score: {score_user}")
    print(f"Computer's final cards: {cards_computer}, final score: {score_computer}")
    if score_user == score_computer:
        print("Draw")
    elif score_user == 0:
        print("You win with a Blackjack")
    elif score_computer == 0:
        print("Opponent wins with a Blackjack. You lose")
    elif score_user > 21:
        print("You went over 21. You lose")
    elif score_computer > 21:
        print("Computer went over 21. You win")
    elif score_user > score_computer:
        print("You win")
    else:
        print("You lose")

while True:
    intro = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if intro == "n":
        os.system("clear")
        break
    else:
        os.system("clear")
        print(logo)
        user_cards = sample(cards, 2)
        computer_cards = sample(cards, 2)

        GAME_ACTIVE = True
        while GAME_ACTIVE:
            user_score = calculate_score(user_cards)
            computer_score = calculate_score(computer_cards)
            print(f"Your cards: {user_cards}, current score: {user_score}")
            print(f"Computer's first card: {computer_cards[0]}")
            if user_score == 0 or computer_score == 0 or user_score > 21:
                check_winner(user_score, computer_score, user_cards, computer_cards)
                break

            repeat = input("Type 'y' to draw another card. Type 'n' to pass: ")
            if repeat == "y":
                user_cards.append(choice(cards))
            else:
                while computer_score < 17:
                    computer_cards.append(choice(cards))
                    computer_score = calculate_score(computer_cards)
                check_winner(user_score, computer_score, user_cards, computer_cards)
                break
