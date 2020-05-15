from flask import Flask, flash, redirect, render_template, request, session, abort, jsonify, session
import json
from random import randint
from time import time,sleep

app = Flask(__name__)

class DataStore():
    lower_bound = 1
    upper_bound = 10
    number = randint(lower_bound,upper_bound)

data = DataStore()

@app.route("/")
def splash():
    return render_template('splash.html')

@app.route("/playing", methods=['GET','POST'])
def inprogress():

    default_value = '0'
    try:
        current_guess = int(request.form.get('text',default_value))
        print(data.number)

        if current_guess == 0:
            guess_message = "You haven't guessed yet. Put something in the box!"
        elif current_guess == data.number:
            guess_message = "Well done! You guessed correctly. The number I was thinking of was " + str(data.number) + "."
        elif current_guess < data.number:
            guess_message = "Too low! Try again and guess a higher number!"
        else:
            guess_message = "Too high! Try again and guess a lower number!"

    except:
        guess_message = "Please enter a whole number between " + str(data.lower_bound) + " and " + str(data.upper_bound) + "."

    return render_template('playing.html',guess_message=guess_message,upper_bound=data.upper_bound,lower_bound=data.lower_bound)

if __name__ == "__main__":
    app.run(debug=True)
