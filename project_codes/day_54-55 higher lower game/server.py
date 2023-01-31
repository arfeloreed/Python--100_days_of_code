from flask import Flask
import random as rd


app = Flask(__name__)

# different routes using the app route decorator
@app.route('/')
def home():
    return '<h1>Guess a number between 0 and 9</h1>'\
        '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width=400>'

# get the number from the url as user input
@app.route('/<int:number>')
def guess(number):
    if number > correct_number:
        return '<h1 style="color: red;">Too high, try again!</h1>'\
            '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" width=400>'
    elif number < correct_number:
        return '<h1 style="color: purple;">Too low, try again!</h1>'\
            '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" width=400>'
    else:
        return '<h1 style="color: green;">You found me!</h1>'\
            '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" width=400>'

# generate a random number between 0 and 9
correct_number = rd.randint(0, 9)
print(correct_number)

if __name__ == '__main__':
    app.run(debug=True)
