import os

from flask_migrate import Migrate

from app import create_app, db

app = create_app(os.getenv('FLASK_ENV') or 'default')
migrate = Migrate(app, db)

#
# @app.shell_context_processor
# def make_shell_context():
#     return dict(fake=fake, db=db, User=User, Role=Role, Post=Post, Follow=Follow, Comment=Comment, Category=Category,
#                 Tag=Tag)
#
#
# @app.cli.command()
# def test():
#     import unittest
#     tests = unittest.TestLoader().discover('tests')
#     unittest.TextTestRunner(verbosity=2).run(tests)
