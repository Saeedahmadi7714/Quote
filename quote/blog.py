from flask import Blueprint, render_template
from .database import get_db

bp = Blueprint("blog", __name__)


@bp.route("/home/")
@bp.route("/")
def home():
    db = get_db()
    # test_post = {
    #     
    # }
    # db.user.insert(doc1)
    # print(db.collection_names())
    return render_template('/blog/index.html')


@bp.route('/post/<post_id>')
def post(post_id):
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
