from datetime import datetime

from sqlalchemy import Column, SmallInteger, Integer, DateTime

from app import db


class Base(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True)
    create_time = Column(DateTime, index=True)
    status = Column(SmallInteger, default=1)

    def __init__(self, **kwargs):
        self.create_time = datetime.utcnow()

    def set_attr(self, attrs_dict):
        for key, value in attrs_dict.items():
            if hasattr(self, key) and key != id:
                setattr(self, key, value)

    def delete(self):
        self.status = 0
