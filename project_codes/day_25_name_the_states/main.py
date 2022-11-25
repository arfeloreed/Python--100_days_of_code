import turtle as t
from states import States

my_screen = t.Screen()
image = "blank_states_img.gif"
my_screen.bgpic(image)
my_screen.title("U.S. States Game")
my_screen.setup(width=800, height=520)

# create turtle object for the states
states_usa = States()

# track score
score = 0
while states_usa.correct_guess != 50:
    # ask for the user input
    answer = my_screen.textinput(title=f"{score}/50    Guess the State", prompt="Enter a name of a State: ").title()
    if answer == "Quit":
        states_usa.quit()
        break
    if answer not in states_usa.correct_guess:
        if states_usa.check_answer(answer):
            score += 1
