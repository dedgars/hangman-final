from main import db

class Letters(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    letter = db.Column(db.String(length=5), nullable=False)

    def __repr__(self):
        return self.letter










