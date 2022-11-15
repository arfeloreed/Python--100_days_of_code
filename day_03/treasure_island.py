print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Bibic's Treasure Island.")
print("Your mission is to find the treasure.")
print()
choice_1 = input("Habang nagalakaw lakaw ka, nakakita ka ug dalawa ka pwertahan"
                 "\npili: pula or puti? ").lower()
if choice_1 == "pula":
    choice_2 = input("Pagkasulod nimu sa pula na door, Magic naabot dayun ka sa lake "
                     "na naay gamay na island sa tunga. Gusto nimu muadto sa gamay na "
                     "island. Pwede ka mulangoy o mangita ug bangka.\nPili: swim or wait? ").lower()
    if choice_2 == "swim":
        choice_3 = input("Nakaabot nka sa gamay na island. Ug sa tunga nakakita "
                         "ka ug tulo ka treasure chest. Pili sa tulo ka treaseure "
                         "chest. \nleft, middle or right? ").lower()
        if choice_3 == "left":
            print("Congratulations, ang sulod sa treasure chest kay mga picx ni "
                  "Reed pogi. Edisplay sa imung kwarto.")
        elif choice_3 == "middle":
            print("Ang sulod sa treasure chest kay utot na bahu ni ngatpi. Game over.")
        elif choice_3 == "right":
            print("Ang sulod sa treasure chest kay mga pimples ni badon kulot. Game over.")
        else:
            print("Pasaway ka. Game over.")
    else:
        print("Nakakita ka ug bangka, pero naa halimaw gabantay na kulot. "
              "Game over.")
else:
    print("Gikaon ka sa halimaw na lapad ug ilong. Game over.")
