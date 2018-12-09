from datetime import datetime

from sqlalchemy import Column, Integer, Text, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from app import db


class Comment(db.Model):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    body = Column(Text)
    disabled = Column(Boolean, default=False)
    create_time = Column(DateTime, default=datetime.utcnow, index=True)
    author_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('posts.id'))
    replied_id = Column(Integer, ForeignKey('comments.id'))
    replied = relationship('Comment', back_populates='replies', remote_side=[id])
    replies = relationship('Comment', back_populates='replied', cascade='all')
