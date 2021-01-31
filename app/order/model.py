from datetime import datetime

from app import db


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(101), nullable=False)
    shop = db.Column(db.String(101), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow())
    deadline = db.Column(db.DateTime, nullable=False)
    info = db.Column(db.String(240), nullable=False)








