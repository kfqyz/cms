from datetime import datetime

from sqlalchemy import Column, Integer, Text, Boolean, ForeignKey, DateTime

from app import db


class Comment(db.Model):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    body = Column(Text)
    disabled = Column(Boolean, default=False)
    create_time = Column(DateTime, default=datetime.utcnow)
    author_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('posts.id'))
