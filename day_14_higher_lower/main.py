from random import choice
import os
from art import logo, vs
from game_data import data

def data_display(item):
    """Takes the data and return a display output for comparing variables.
    """
    return f"{item['name']}, a {item['description']}, from {item['country']}."

def answer(item_a, item_b):
    """Checks who has more followers between A or B and returns the winner"""
    if item_a['follower_count'] > item_b['follower_count']:
        return "a"
    else:
        return "b"

print(logo)
compare_a = choice(data)
print("Compare A: " + data_display(compare_a))

score = 0
while True:
    print(vs)
    compare_b = choice(data)
    while compare_a == compare_b:
        compare_b = choice(data)
    print("Against B: " + data_display(compare_b))

    correct_answer = answer(item_a=compare_a, item_b=compare_b)
    question = input("Who has more followers? Type 'A' or 'B': ").lower()
    if question != correct_answer:
        os.system("clear")
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        break
    else:
        score += 1
        os.system("clear")
        print(logo)
        print(f"You're right! Current score: {score}.")
        compare_a = compare_b
        print("Compare A: " + data_display(compare_a))
