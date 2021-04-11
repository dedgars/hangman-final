from main import db

class Letters(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    letter = db.Column(db.String(length=5), nullable=False)

    def __repr__(self):
        return self.letter

class AllLetters(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    lett = db.Column(db.String(length=5), nullable=False)

    def __repr__(self):
        return self.lett


class Word(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    theword = db.Column(db.String(length=60), nullable=False)

    def __repr__(self):
        return self.word

class CountryList(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    country = db.Column(db.String(length=100), nullable=False)

    def __repr__(self):
        return self.country














