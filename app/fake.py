from random import randint, sample

from faker import Faker
from sqlalchemy.exc import IntegrityError

from . import db
from .models import User, Post, Comment, Follow, Category


def users(count=50):
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


def categorys():
    category_list = ['心灵鸡汤','时事新闻','财经资讯','娱乐世界','我的生活','图片视频']
    for i in category_list:
        c = Category(name=i)
        db.session.add(c)
    db.session.commit()

def posts():
    fake = Faker('zh_CN')
    user_count = User.query.count()
    for i in range(20):
        u = User.query.offset(randint(0, user_count - 1)).first()
        for j in range(30):
            p = Post(title=fake.text(randint(10, 16)), body=fake.text(),
                     timestamp=fake.past_date(),
                     author=u)
            db.session.add(p)
    db.session.commit()


def comments(count=20):
    fake = Faker('zh_CN')
    posts = Post.query.all()
    authors = User.query.all()
    for post in posts:
        for author in sample(authors, 5):
            comment = Comment(body=fake.text(randint(10, 20)), post_id=post.id, author_id=author.id)
            db.session.add(comment)
    db.session.commit()


def follow():
    fake = Faker('zh_CN')
    user_number = User.query.count()
    for i in range(1, user_number + 1):
        for j in range(1, user_number + 1):
            if i != j:
                follow = Follow(follower_id=i, followed_id=j)
                db.session.add(follow)
    db.session.commit()
