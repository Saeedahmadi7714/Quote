from flask import Blueprint, session, url_for, redirect, request, jsonify
from datetime import datetime
from .models import User, Comment, Post
from .database import get_db

bp = Blueprint("api", __name__)


@bp.route('/create_comment/', methods=['POST'])
def create_comment():
    if request.method == 'POST':
        db = get_db()
        comment = request.form.get('comment')
        post_id = request.form.get('postId')
        user_id = request.form.get('userId')

        post = Post.objects(id=post_id).first()

        # Create a comment
        user = User.objects(id=user_id).first()
        new_comment = Comment(owner=user, text=comment, created_date=datetime.now())
        new_comment.save()

        post.comments.append(new_comment)
        post.save()
        print(post.comments)
        return jsonify(comment)


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


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for("blog.home"))
