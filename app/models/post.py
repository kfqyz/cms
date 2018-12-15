from datetime import datetime

from sqlalchemy import Column, Integer, ForeignKey, String, Text, DateTime
from sqlalchemy.orm import relationship, backref

from app import db

post_categorys = db.Table('post_categorys', Column('category_id', Integer, ForeignKey('categorys.id')),
                          Column('post_id', Integer, ForeignKey('posts.id')))

post_tags = db.Table('post_tags', Column('tag_id', Integer, ForeignKey('tags.id')),
                     Column('post_id', Integer, ForeignKey('posts.id')))


class Post(db.Model):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(128), nullable=False, unique=True)
    body = Column(Text, nullable=False)
    create_time = Column(DateTime, default=datetime.utcnow, index=True)
    author_id = Column(Integer, ForeignKey('users.id'))
    comments = relationship('Comment', backref='post', lazy='dynamic', cascade='all')
    categorys = relationship('Category', secondary=post_categorys, backref=backref('posts', lazy='dynamic'),
                             lazy='dynamic')
    tags = relationship('Tag', secondary=post_tags, backref=backref('posts', lazy='dynamic'),
                        lazy='dynamic')

    def __repr__(self):
        return 'Post:{}-{}'.format(self.id, self.title)
