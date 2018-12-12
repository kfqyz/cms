from random import randint, sample

from faker import Faker

from app import db
from app.models.category import Category
from app.models.comment import Comment
from app.models.follow import Follow
from app.models.post import Post
from app.models.role import Permission, Role
from app.models.tag import Tag
from app.models.user import User

fake = Faker('zh_CN')


def fake_all():
    roles()
    print('Successful fake roles.')
    users()
    print('Successful fake users.')
    add_admin()
    print('Successful add admin user.')
    categorys()
    print('Successful fake categorys.')
    posts()
    print('Successful fake posts.')
    comments()
    print('Successful fake comments.')
    follow()
    print('Successful fake follow.')
    print('fake all is ok ^-^ ')


def roles():
    roles = {
        '注册用户': [Permission.FOLLOW, Permission.COMMENT, Permission.WRITE],
        '管理员': [Permission.FOLLOW, Permission.COMMENT,
                Permission.WRITE, Permission.MODERATE],
        '超级管理员': [Permission.FOLLOW, Permission.COMMENT,
                  Permission.WRITE, Permission.MODERATE,
                  Permission.ADMIN],
    }
    default_role = '注册用户'
    for r in roles:
        role = Role.query.filter_by(name=r).first()
        if role is None:
            role = Role(name=r)
        role.reset_permissions()
        for perm in roles[r]:
            role.add_permission(perm)
        role.default = (role.name == default_role)
        db.session.add(role)
    db.session.commit()


def users(count=20):
    i = 0
    while i < count:
        u = User(email=fake.email(),
                 username=fake.user_name(),
                 phone_number=fake.phone_number(),
                 password='asdf',
                 confirmed=True,
                 name=fake.name(),
                 location=fake.city(),
                 about_me=fake.text(20),
                 create_time=fake.past_date(),
                 last_seen=fake.past_date())
        db.session.add(u)
        i += 1
    db.session.commit()


def add_admin():
    admin = User(username='admin', email='admin@qq.com', phone_number=18999999999, password='asdf', role_id=3,
                 confirmed=True)
    db.session.add(admin)
    db.session.commit()


def categorys():
    users = User.query.all()
    for i in range(8):
        for user in users:
            c = Category(name=fake.text(6).replace('.', ''), user=user)
            db.session.add(c)
    db.session.commit()


def tags():
    posts = Post.query.all()
    for i in range(4):
        for post in posts:
            name = fake.text(6).replace('.', '')
            if name not in [tag.name for tag in Tag.query.all()]:
                t = Tag(name=name, posts=[post])
                db.session.add(t)
    db.session.commit()


def posts():
    user_count = User.query.count()
    for i in range(20):
        u = User.query.offset(randint(0, user_count - 1)).first()
        for j in range(10):
            p = Post(title=fake.text(randint(8, 20)), body=fake.text(100),
                     create_time=fake.past_date(),
                     author=u)
            db.session.add(p)
    db.session.commit()


def comments():
    posts = Post.query.all()
    authors = User.query.all()
    for post in posts:
        for author in sample(authors, 5):
            comment = Comment(body=fake.text(20), post_id=post.id, author_id=author.id)
            db.session.add(comment)
    db.session.commit()


def follow(num=10):
    user_id_list = [user.id for user in User.query.all()]
    from random import sample
    for follower_id in user_id_list:
        for followed_id in sample(user_id_list, num):
            if followed_id != follower_id:
                follow = Follow(follower_id=follower_id, followed_id=followed_id)
                db.session.add(follow)
    db.session.commit()
