from sqlalchemy import Column, String, Integer, ForeignKey

from app.models.base import Base


class Category(Base):
    __tablename__ = 'categorys'
    name = Column(String(64), nullable=False, unique=True)
    user_id = Column(Integer, ForeignKey('users.id'))

    def __repr__(self):
        return '{} {}'.format(self.id, self.name)
