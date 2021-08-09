from flask import Blueprint, render_template, request, redirect, url_for, session
from .database import get_db

bp = Blueprint("blog", __name__)







# For testing that project is correctly running
@bp.route("/")
def index():
    posts = Blogpost.query.order_by(Blogpost.date_posted.desc()).all()
    return render_template('/blog/index.html', posts=posts)


@bp.route('/about')
def about():
    return render_template('about.html')


@bp.route("/home/")
def home():
    posts = Blogpost.query.filter_by().all()
    return render_template('home.html', posts=posts)


@bp.route('/post/<post_id>')
def post(post_id):
    db = get_db()
    pass


@bp.route('/category-posts/<category_id>')
def category(category_id):
    pass


@bp.route('/tag-posts/<tag_id>')
def tag(tag_id):
    pass


@bp.route('/login')
def login():
    pass


@bp.route("/logout")
def logout():
    session.pop('user')
    return redirect('/')
