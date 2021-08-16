from flask import Blueprint, render_template, session, url_for, redirect

from .models import User
from .database import get_db

bp = Blueprint("api", __name__)


@bp.route('/posts_list/<user_id>/')
def posts_list(user_id):
    pass


@bp.route('/post-delete/<post_id>')
def post_delete(post_id):
    pass


@bp.route('/post_deactivate/<post_id>/')
def post_deactivate(post_id):
    pass


@bp.route('/category-list/')
def categories_list():
    pass


@bp.route('/tags-list/')
def tags_list():
    pass


@bp.route('/search/')
def search():
    pass


@bp.route('/user-profile/<user_id>')
def user_profile(user_id):
    pass


def logout():
    session.clear()
    return redirect(url_for("blog.home"))
