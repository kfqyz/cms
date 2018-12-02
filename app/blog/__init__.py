from flask import Blueprint

blog = Blueprint('blog', __name__)

from . import views, errors
from app.models.role import Permission


@blog.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)
