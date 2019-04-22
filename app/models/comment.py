from datetime import datetime

from app import db, whooshee


# from sqlalchemy import Column, db.Integer, db.Text, db.Boolean, db.ForeignKey, DateTime
# from sqlalchemy.orm import db.relationship


@whooshee.register_model('body')
class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    disabled = db.Column(db.Boolean, default=False)
    create_time = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    replied = db.relationship('Comment', back_populates='replies', remote_side=[id])
    replies = db.relationship('Comment', back_populates='replied', cascade='all')
    replied_id = db.Column(db.Integer, db.ForeignKey('comments.id'))

    def __repr__(self):
        return 'Comment:{}'.format(self.id)
