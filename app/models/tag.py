from datetime import datetime

from app import db, whooshee


# from sqlalchemy import Column, String, db.Integer, DateTime


@whooshee.register_model('name')
class Tag(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False, unique=True)
    create_time = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return 'Tag:{}-{}'.format(self.id, self.name)
