from .database import db


class Computation(db.Model):
    __tablename__ = "computation"
    id = db.Column(db.Integer, primary_key=True)
    dividend = db.Column(db.Integer, nullable=False)
    divisor = db.Column(db.Integer, nullable=False)
    result = db.Column(db.Float, nullable=False)
