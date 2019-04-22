from datetime import datetime

from app import db, whooshee

post_categorys = db.Table('post_categorys', db.Column('category_id', db.Integer, db.ForeignKey('categorys.id')),
                          db.Column('post_id', db.Integer, db.ForeignKey('posts.id')))

post_tags = db.Table('post_tags', db.Column('tag_id', db.Integer, db.ForeignKey('tags.id')),
                     db.Column('post_id', db.Integer, db.ForeignKey('posts.id')))


@whooshee.register_model('title', 'body')
class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False, unique=True)
    body = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comments = db.relationship('Comment', backref='post', lazy='dynamic', cascade='all')
    categorys = db.relationship('Category', secondary=post_categorys, backref=db.backref('posts', lazy='dynamic'),
                             lazy='dynamic')
    tags = db.relationship('Tag', secondary=post_tags, backref=db.backref('posts', lazy='dynamic'),
                           lazy='dynamic')

    def __repr__(self):
        return 'Post:{}-{}'.format(self.id, self.title)
