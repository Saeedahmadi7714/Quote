from flask import Blueprint, render_template, session, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from .categories import create_cats

from .models import User, Post
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


@bp.route('/posts-list/')
def posts_list():
    db = get_db()
    user_id = session["user_id"]
    first_name = session["first_name"]
    user_posts = Post.objects(author=user_id)
    return render_template("user/dashboard.html", user_posts=user_posts, first_name=first_name)


@bp.route('/create-post/')
def create_post():
    if session:
        user = session
        if request.method == 'POST':
    
            # password = request.form.get("password")
            # user_name = request.form.get("user_name")
            db = get_db()
            
            return redirect(url_for('blog.home'))
        
    return render_template("user/create_post.html", user=user, categories=create_cats())


@bp.route('/edit-post/<post_id>/')
def edit_post(post_id):
    pass


@bp.route('/change_password/', methods=['POST'])
def change_password():
    if session is None:
        return redirect(url_for('blog.login'))

    db = get_db()
    old_password = request.form.get('old_password')
    new_password = request.form.get('password')
    user = User.objects(id=session['user_id']).first()
    if check_password_hash(user["password"], old_password):
        user.password = generate_password_hash(new_password, method='sha256')
        user.save()
        print('=========================OK')
        flash('Your password successfully changed.')
        return redirect(url_for('user.profile'))

    flash('Your old password is incorrect.', 'error')
    return redirect(url_for('user.profile'))
