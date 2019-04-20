# from sqlalchemy import Column, db.Integer, db.ForeignKey, DateTime
from datetime import datetime

from app import db


class Follow(db.Model):
    __tablename__ = 'follows'
    follower_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    followed_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    create_time = db.Column(db.DateTime, default=datetime.utcnow)
