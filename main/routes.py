import string

from main import app
from flask import render_template, redirect, url_for, flash, get_flashed_messages, request
from main.modules import Letters
from main import db

all_letters = list(string.ascii_uppercase)


@app.route('/',  methods=['GET', 'POST'])
def home_page():
    Letters.query.delete()
    db.session.commit()

    message = 'This is home'
    current = ''
    if request.method == 'POST':
        current = request.form["letter_button"]
        letter_db = Letters(letter=current)
        db.session.add(letter_db)
        db.session.commit()
        guessed = Letters.query.all()
        return render_template('play.html', message=message, letters=all_letters, guessed=guessed, current=current)

    return render_template('home.html', message=message, letters=all_letters)


@app.route('/play',  methods=['GET', 'POST'])
def play():
    current = request.form["letter_button"]
    letter_db = Letters(letter=current)
    letters_left = all_letters
    letters_left.remove(current)
    db.session.add(letter_db)
    db.session.commit()
    guessed = Letters.query.all()
    return render_template('play.html', letters=letters_left, guessed=guessed, current=current)

