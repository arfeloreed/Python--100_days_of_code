"""Working file for the states"""
import pandas
from turtle import Turtle


class States(Turtle):
    """A subclass of Turtle class"""
    def __init__(self):
        """Initialize the attributes for States"""
        super().__init__()
        states = pandas.read_csv("50_states.csv")
        self.answer_list = states["state"].to_list()
        self.x_cor = states["x"].to_list()
        self.y_cor = states["y"].to_list()
        self.penup()
        self.hideturtle()
        self.correct_guess = []

    def show_state(self, position, state):
        """show the location of the state in the screen if the user input the correct answer"""
        self.setpos(position)
        self.write(arg=f"{state}")

    def check_answer(self, user_answer):
        """Check the answer of the user in the answer list"""
        if user_answer in self.answer_list:
            index = self.answer_list.index(user_answer)
            pos = (self.x_cor[index], self.y_cor[index])
            self.correct_guess.append(user_answer)
            self.show_state(position=pos, state=user_answer)
            return True

    def quit(self):
        """when user chose to quit, create a csv file about all the miss states for study purpose"""
        states_forgot = []
        for state in self.answer_list:
            if state not in self.correct_guess:
                states_forgot.append(state)
        file = pandas.DataFrame(states_forgot)
        file.to_csv("states to learn.csv")
