from datetime import datetime
from flask import render_template, session, redirect, url_for
from . import main
from .forms import NameForm
from .. import db
from ..models import User
from flask_login import login_required


@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        return redirect(url_for('.index'))
    return render_template('index.html', form=form, name=session.get('name'), \
                           known=session.get('known', False), current_time=datetime.utcnow())


from ..decorators import admin_required, permission_required


@main.route('/secret')
@login_required
@admin_required
def secret():
    return '登录才能看到啊！'
