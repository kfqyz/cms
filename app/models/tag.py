from datetime import datetime

from sqlalchemy import Column, String, Integer, DateTime

from app import db


class Tag(db.Model):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False, unique=True)
    create_time = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return 'Tag:{}-{}'.format(self.id, self.name)
