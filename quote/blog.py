from flask import Blueprint, render_template, request, redirect, url_for, session
from .database import get_db

bp = Blueprint("blog", __name__)

db = get_db()


class Blogpost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    subtitle = db.Column(db.String(50))
    author = db.Column(db.String(20))
    date_posted = db.Column(db.DateTime)
    content = db.Column(db.Text)


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
