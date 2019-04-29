from functools import wraps
from urllib.parse import urlparse, urljoin

from flask import request, redirect, abort, url_for
from flask_login import current_user

from app.models.role import Permission


# 权限要求装饰器
def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.can(permission):
                abort(403)
            return f(*args, **kwargs)

        return decorated_function

    return decorator


# 管理员权限要求装饰器
def admin_required(f):
    return permission_required(Permission.ADMIN)(f)


# 判断访问Url的安全性
def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc


# 重定向回上一个页面
def redirect_back(default='blog.index', **kwargs):
    target = request.args.get('next')
    if target is not None and is_safe_url(target):
        return redirect(target)
    return redirect(url_for(default, **kwargs))
