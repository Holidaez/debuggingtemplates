from .db import db


class Review(db.Model):
    __tablename__ = "reviews"

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(321), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    business_id = db.Column(db.Integer, db.ForeignKey('businesses.id'), nullable=False)

    user = db.relationship("User", back_populates="reviews")
    businesses = db.relationship("Businesses", back_populates="reviews")
