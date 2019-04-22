from datetime import datetime

from app import db, whooshee


# from sqlalchemy import Column, String, db.Integer, db.ForeignKey, DateTime

@whooshee.register_model('name')
class Category(db.Model):
    __tablename__ = 'categorys'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    create_time = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return 'Category:{}-{}'.format(self.id, self.name)
