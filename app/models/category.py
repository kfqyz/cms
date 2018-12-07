from datetime import datetime

from sqlalchemy import Column, String, Integer, ForeignKey, DateTime

from app import db


class Category(db.Model):
    __tablename__ = 'categorys'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    create_time = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '{} {}'.format(self.id, self.name)
