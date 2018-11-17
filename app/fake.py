from random import randint,sample
from sqlalchemy.exc import IntegrityError
from faker import Faker
from . import db
from .models import User, Post, Comment


def users(count=100):
    fake = Faker('zh_CN')
    i = 0
    while i < count:
        u = User(email=fake.email(),
                 username=fake.user_name(),
                 phone_number=fake.phone_number(),
                 password='asdf',
                 confirmed=True,
                 name=fake.name(),
                 location=fake.city(),
                 about_me=fake.text(),
                 member_since=fake.past_date())
        db.session.add(u)
        try:
            db.session.commit()
            i += 1
        except IntegrityError:
            db.session.rollback()


def posts(count=100):
    fake = Faker('zh_CN')
    user_count = User.query.count()
    for i in range(count):
        u = User.query.offset(randint(0, user_count - 1)).first()
        for i in range(1, 50):
            p = Post(body=fake.text(),
                     timestamp=fake.past_date(),
                     author=u)
            db.session.add(p)
    db.session.commit()


def comments(count=20):
    fake = Faker('zh_CN')
    posts = Post.query.all()
    authors = User.query.all()
    for post in posts:
        for author in sample(authors,20):
            comment = Comment(body=fake.text(randint(10, 20)), post_id=post.id, author_id=author.id)
            db.session.add(comment)
    db.session.commit()
