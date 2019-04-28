from flask import render_template

from app.admin import admin


@admin.route('/')
def home():
    return render_template('admin/home.html')
