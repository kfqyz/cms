from sqlalchemy import Column, Integer, ForeignKey

from app import db


class Follow(db.Model):
    __tablename__ = 'follows'
    follower_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    followed_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
