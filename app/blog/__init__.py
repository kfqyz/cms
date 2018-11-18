from flask import Blueprint

main = Blueprint('blog', __name__)

from  . import views, errors
from ..models import Permission

@main.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)