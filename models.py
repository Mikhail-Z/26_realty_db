from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class RealtyAd(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    settlement = db.Column(db.String)
    under_construction = db.Column(db.Boolean)
    description = db.Column(db.String)
    price = db.Column(db.Integer)
    oblast_district = db.Column(db.String)
    living_area = db.Column(db.Float)
    has_balcony = db.Column(db.Boolean)
    address = db.Column(db.String)
    construction_year = db.Column(db.SmallInteger)
    rooms_number = db.Column(db.SmallInteger)
    premise_area = db.Column(db.Float)
    active = db.Column(db.Boolean)
    ad_id = db.Column(db.Integer)

