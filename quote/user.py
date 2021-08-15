from flask import Blueprint, render_template
from .database import get_db

bp = Blueprint("user", __name__, url_prefix="/user")


@bp.route('/profile/')
def profile():
    pass


@bp.route('/posts-list/<user_id>/')
def posts_list(user_id):
    pass


@bp.route('/create-post/')
def create_post():
    pass


@bp.route('/edit-post/<post_id>/')
def edit_post(post_id):
    pass
