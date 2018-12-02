from sqlalchemy import Column, String

from app.models.base import Base


class Tag(Base):
    __tablename__ = 'tags'
    name = Column(String(64), nullable=False, unique=True)

    def __repr__(self):
        return self.name
