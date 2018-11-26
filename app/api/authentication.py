from flask import g, jsonify
from flask_httpauth import HTTPBasicAuth

from . import api
from .errors import unauthorized, forbidden
from ..models import User

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(token, password):
    if token == '':
        return False
    if password == '':
        g.current_user = User.verify_auth_token(token)
        g.token_used = True
        return g.current_user is not None
    user = User.query.filter_by(username=token).first() \
           or User.query.filter_by(email=token).first() \
           or User.query.filter_by(phone_number=token).first()
    if not user:
        return False
    g.current_user = user
    g.token_used = False
    return user.verify_password(password)


@auth.error_handler
def auth_error():
    return unauthorized('无效的认证')


@api.before_request
@auth.login_required
def before_request():
    if not g.current_user.is_anonymous and \
            not g.current_user.confirmed:
        return forbidden('账户没有认证')


@api.route('/tokens/', methods=['POST'])
def get_token():
    if g.current_user.is_anonymous or g.token_used:
        return unauthorized('无效的认证')
    return jsonify({'token': g.current_user.generate_auth_token(
        expiration=3600), 'expiration': 3600})
