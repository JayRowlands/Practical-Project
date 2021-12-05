
from application import db

class Prize(db.Model):
    prize_id = db.Column(db.Integer, primary_key = True)
    prize_name = db.Column(db.String(45))
    colour = db.Column(db.String(45))
    cost = db.Column(db.Integer)
    type = db.Column(db.String(45))