import string
from random import choice
from main import app
from flask import render_template, redirect, url_for, flash, get_flashed_messages, request
from main.forms import LetterButton
from main.modules import Letters, AllLetters, Word, CountryList
from main import db


@app.route('/', methods=['GET', 'POST'])
def home_page():
    Word.query.delete()
    Letters.query.delete()
    AllLetters.query.delete()
    db.session.commit()
    wordbase = ['Aruba', 'Afghanistan', 'Angola', 'Anguilla', 'Aland Islands', 'Albania', 'Andorra',
                'United Arab Emirates', 'Argentina', 'Armenia', 'American Samoa', 'Antarctica',
                'French Southern Territories', 'Antigua and Barbuda', 'Australia', 'Austria', 'Azerbaijan', 'Burundi',
                'Belgium', 'Benin', 'Burkina Faso', 'Bangladesh', 'Bulgaria', 'Bahrain', 'Bahamas',
                'Bosnia and Herzegovina', 'Belarus', 'Belize', 'Bermuda', 'Bolivia', 'Brazil', 'Barbados', 'Brunei',
                'Bhutan', 'Botswana', 'Central African Republic', 'Canada', 'Cocos Islands', 'Switzerland', 'Chile',
                'China', 'Cameroon', 'The Democratic Republic of the Congo', 'Congo', 'Cook Islands', 'Colombia',
                'Comoros', 'Cabo Verde', 'Costa Rica', 'Cuba', 'Cayman Islands', 'Cyprus', 'Czechia', 'Germany',
                'Djibouti', 'Dominica', 'Denmark', 'Dominican Republic', 'Algeria', 'Ecuador', 'Egypt', 'Eritrea',
                'Western Sahara', 'Spain', 'Estonia', 'Ethiopia', 'Finland', 'Fiji', 'Falkland Islands', 'France',
                'Faroe Islands', 'Micronesia', 'Gabon', 'United Kingdom', 'Georgia', 'Guernsey', 'Ghana', 'Gibraltar',
                'Guinea', 'Guadeloupe', 'Gambia', 'Guinea Bissau', 'Equatorial Guinea', 'Greece', 'Grenada',
                'Greenland', 'Guatemala', 'French Guiana', 'Guam', 'Guyana', 'Hong Kong', 'Honduras', 'Croatia',
                'Haiti', 'Hungary', 'Indonesia', 'Isle of Man', 'India', 'Ireland', 'Iran', 'Iraq', 'Iceland', 'Israel',
                'Italy', 'Jamaica', 'Jersey', 'Jordan', 'Japan', 'Kazakhstan', 'Kenya', 'Kyrgyzstan', 'Cambodia',
                'Kiribati', 'Saint Kitts and Nevis', 'South Korea', 'Kuwait', 'Laos', 'Lebanon', 'Liberia', 'Libya',
                'Liechtenstein', 'Sri Lanka', 'Lesotho', 'Lithuania', 'Luxembourg', 'Latvia', 'Macao', 'Morocco',
                'Monaco', 'Moldova', 'Madagascar', 'Maldives', 'Mexico', 'Marshall Islands', 'North Macedonia', 'Mali',
                'Malta', 'Myanmar', 'Montenegro', 'Mongolia', 'Mozambique', 'Mauritania', 'Martinique', 'Mauritius',
                'Malawi', 'Malaysia', 'Mayotte', 'Namibia', 'New Caledonia', 'Niger', 'Nigeria', 'Nicaragua',
                'Netherlands', 'Norway', 'Nepal', 'Nauru', 'New Zealand', 'Oman', 'Pakistan', 'Panama', 'Pitcairn',
                'Peru', 'Philippines', 'Palau', 'Papua New Guinea', 'Poland', 'Puerto Rico', 'North Korea', 'Portugal',
                'Paraguay', 'Palestine', 'French Polynesia', 'Qatar', 'Romania', 'Russian Federation', 'Rwanda',
                'Saudi Arabia', 'Sudan', 'Senegal', 'Singapore', 'South Georgia and the South Sandwich Islands',
                'Sierra Leone', 'El Salvador', 'San Marino', 'Somalia', 'Serbia', 'South Sudan',
                'Sao Tome and Principe', 'Suriname', 'Slovakia', 'Slovenia', 'Sweden', 'Eswatini', 'Sint Maarten',
                'Seychelles', 'Syria', 'Chad', 'Togo', 'Thailand', 'Tajikistan', 'Tokelau', 'Turkmenistan', 'Timor',
                'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Tuvalu', 'Taiwan', 'Tanzania', 'Uganda',
                'Ukraine', 'United States Minor Outlying Islands', 'Uruguay', 'United States of America', 'Uzbekistan',
                'Vatican', 'Venezuela', 'Viet Nam', 'Vanuatu', 'Samoa', 'Yemen', 'South Africa', 'Zambia', 'Zimbabwe']
    one_word = choice(wordbase).upper()
    word = len(one_word) * ' '
    x = Word(theword=one_word)
    db.session.add(x)
    db.session.commit()

    l = list(string.ascii_uppercase)

    for i in l:
        x = AllLetters(lett=str(i))
        db.session.add(x)
    db.session.commit()

    form = LetterButton()
    all_letters = AllLetters.query.all()
    colors = ['primary', 'secondary', 'success', 'danger', 'warning', 'info', 'dark']
    return render_template('home.html', form=form, all_letters=all_letters, colors=colors, word=word, tries_left='5')


@app.route('/play', methods=['GET', 'POST'])
def play():
    colors = ['primary', 'secondary', 'success', 'danger', 'warning', 'info', 'dark']
    our_word = db.session.query(Word.theword).filter_by(id=1).first()[0]
    all_letters = AllLetters.query.all()
    letters = Letters.query.all()
    letter_list = [str(i) for i in letters]
    word = []




    for i in our_word:
        if i in letter_list:
            word.append(i)
        else:
            word.append(' ')

    count = [i for i in word if i != ' ']

    correct_letters = len(set(count))
    tries_left = 5 - len(letter_list) + correct_letters


    if our_word == ''.join(word):
        return render_template('home.html', all_letters=all_letters, colors=colors, word=word,
                               message='YOU WIN!!!', tries_left=tries_left)
    elif tries_left < 1:
        return render_template('home.html', colors=['dark'], word=our_word,
                               message='YOU HAVE LOST!', tries_left='0')


    return render_template('home.html', all_letters=all_letters, colors=colors, word=word,
                           tries_left=tries_left)


@app.route('/delete_letter/<letter>', methods=['GET', 'POST'])
def delete_letter(letter):
    letter_delete = AllLetters.query.filter_by(lett=letter).first()
    letter_add = Letters(letter=letter)
    try:
        db.session.add(letter_add)
        db.session.delete(letter_delete)
        db.session.commit()
        return redirect(url_for('play'))
    except:
        return 'Error deleting'
