from flask import Blueprint, render_template, redirect, url_for, request, session
from .database import get_db

bp = Blueprint("blog", __name__)


@bp.route("/")
def home():
    db = get_db()
    print(db)
    posts = db.COLLECTION_NAME.find().sort("date_posted").limit(5)
    return render_template('/blog/index.html', posts=posts)


@bp.route('/post/<post_id>')
def post(post_id):
    pass


@bp.route('/category-posts/<category_id>')
def category(category_id):
    pass


@bp.route('/tag-posts/<tag_id>')
def tag(tag_id):
    pass


@bp.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["name"]
        session["user"] = user
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))

        return render_template("login.html")


@bp.route('/user')
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("login"))
