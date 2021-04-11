import string

from main import app
from flask import render_template, redirect, url_for, flash, get_flashed_messages, request
from main.forms import LetterButton
from main.modules import Letters, AllLetters
from main import db


@app.route('/', methods=['GET', 'POST'])
def home_page():

    Letters.query.delete()
    AllLetters.query.delete()
    l = list(string.ascii_uppercase)
    for i in l:
        x = AllLetters(lett=i)
        db.session.add(x)
    db.session.commit()

    form = LetterButton()
    all_letters = AllLetters.query.all()
    return render_template('home.html', form=form, all_letters=all_letters)

@app.route('/play', methods=['GET', 'POST'])
def play():
    form = LetterButton()
    all_letters = AllLetters.query.all()
    return render_template('home.html', form=form, all_letters=all_letters)


@app.route('/delete_letter/<letter>', methods=['GET', 'POST'])
def delete_letter(letter):
    letter = AllLetters.query.filter_by(lett=letter).first()
    try:
        db.session.delete(letter)
        db.session.commit()
        return redirect(url_for('play'))
    except:
        return 'Error deleting'
