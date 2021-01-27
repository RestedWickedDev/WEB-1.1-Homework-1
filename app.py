"""Homework 1"""

from random import randint
from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    """Shows a greeting to the user."""
    return 'Are you there, world? It\'s me, Ducky!'

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    """Display a message to the user that changes based on their favorite dessert"""
    return f'How did you know I liked {users_dessert}?'

@app.route('/madlibs/<adjective>/<noun>')
def madlibs(adjective, noun):
    """Takes two strings and displays a funny safe for work story"""
    return f"""
    How can the net amount of {noun} of the universe be massively decreased?
    \nFive words were printed: INSUFFICIENT DATA FOR {adjective} ANSWER.
    """

@app.route("/multiply/<number1>/<number2>")
def multiply(number1, number2):
    """Takes two numbers and multiplies them"""
    if number1.isdigit() and number2.isdigit():
        result = int(number1) * int(number2)
        return f"{number1} times {number2} is {result}."
    else:
        return "Invalid inputs. Please try again by entering 2 numbers!"

@app.route("/sayntimes/<word>/<n>")
def sayntimes(word, n):
    """Takes a word and repeats it n amount of times"""
    if n.isdigit():
        result = ""
        for n in range(int(n)):
            result = result + str(word) + " "
        return result
    else:
        return "Invalid input. Please try again by entering a word and a number!"

@app.route("/dicegame")
def roll():
    """Roll a random number 1-6 if you roll a 6 you win, else you lose"""
    value = randint(1, 6)
    if value == 6:
        return "You rolled a 6. You won!"
    else:
        return f"You rolled a {value}. You lost!"

if __name__ == '__main__':
    app.run(debug=True)
