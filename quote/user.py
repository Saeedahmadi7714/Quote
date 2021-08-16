from flask import Blueprint, render_template, session, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash

from .models import User
from .database import get_db

bp = Blueprint("user", __name__, url_prefix="/user")


@bp.route('/profile/', methods=['GET', 'POST'])
def profile():
    if request.method == 'GET':

        if session is None:
            return redirect(url_for('blog.login'))
        else:
            db = get_db()
            user = User.objects(id=session['user_id']).first()
            return render_template("user/profile.html", user=user)

    db = get_db()
    new_password = request.form.get('password')
    user = User.objects(id=session['user_id']).first()
    user.password = generate_password_hash(new_password, method='sha256')
    user.save()
    return redirect(url_for('user.profile'))


@bp.route('/posts-list/<user_id>/')
def posts_list(user_id):
    pass


@bp.route('/create-post/')
def create_post():
    pass


@bp.route('/edit-post/<post_id>/')
def edit_post(post_id):
    pass


@bp.route('/change_password/', methods=['POST'])
def change_password():
    if session is None:
        return redirect(url_for('blog.login'))

    db = get_db()
    new_password = request.form.get('password')
    user = User.objects(id=session['user_id']).first()
    user.password = generate_password_hash(new_password, method='sha256')
    user.save()
    flash('Your password successfully changed.')
    return redirect(url_for('user.profile'))
