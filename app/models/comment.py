from sqlalchemy import Column, Integer, Text, Boolean, ForeignKey

from app.models.base import Base


class Comment(Base):
    __tablename__ = 'comments'
    body = Column(Text)
    disabled = Column(Boolean, default=False)
    author_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('posts.id'))
