import os
from art import logo

print(logo)

bidders = {}
bid_active = True
while bid_active:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))

    bidders[name] = bid

    repeat = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if repeat == "no":
        bid_active = False
        os.system("clear")
        highest_bid = max(bidders.values())
        for bidder in bidders:
            if bidders[bidder] == highest_bid:
                print(f"The winner is {bidder} with a bid of ${bidders[bidder]}")
    else:
        os.system("clear")
# print()
# print(bidders)
