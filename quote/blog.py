from flask import Blueprint, render_template, redirect, url_for, request, flash, session, jsonify, current_app
from .models import User, Post, Comment, Tag, Category
from .database import get_db
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from .categories import create_cats
from .Utils import reading_time, random_post
from textblob import TextBlob
import os
import json
from bson import ObjectId

bp = Blueprint("blog", __name__)


@bp.route("/home/")
@bp.route("/")
def home():
    db = get_db()
    user = session
    posts = Post.objects()
    tags = Tag.objects()
    # Random post
    r_t = random_post()
    if r_t:
        return render_template("blog/index.html", categories=create_cats(), user=user, posts=posts, tags=tags, rand_post=r_t)
    return render_template("blog/index.html", categories=create_cats(), user=user, posts=posts, tags=tags)


@bp.route('/post/<post_id>/')
def post(post_id):
    db = get_db()
    user = session
    post_details = Post.objects(id=post_id).first()

    # Detect language from title for setting text direction
    blobline = TextBlob(post_details.title)
    language = blobline.detect_language()

    return render_template("blog/post.html", categories=create_cats(), post=post_details, user=user,
                           reading_time=reading_time(post_details.content), language=language)


@bp.route('/category-posts/<category_id>')
def category(category_id):
    db = get_db()
    user = session
    posts = Post.objects()

    return render_template("blog/category.html", user=user, posts=posts)


@bp.route('/tag-posts/<tag_id>', methods=['GET', 'POST'])
def tag(tag_id):
    if request.method == 'GET':
        db = get_db()
        posts = Post.objects()
        post_obj = []
        
        for post in posts:
            for tag in post.tags:
                if str(tag.id) == (tag_id):
                    # print(tag.id,"==", tag_id)
                    post = post.to_mongo().to_dict()
                    del post["categories"]
                    del post["likes"]
                    del post["comments"]
                    del post["tags"]
                    del post["author"]
                    post["_id"] = str(post["_id"])
                    post_obj.append(post)

        print(post_obj)          
        return jsonify(post_obj)


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':

        image = None
        user_name = request.form.get("user_name")
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        password = request.form.get("password")
        email = request.form.get("email")
        phone_number = request.form.get("phone_number")
        file = request.files.get('profile_image')
        
        if file:
            file_name = secure_filename(file.filename)
            file_ext = os.path.splitext(file_name)[1]
                
            if file_ext not in current_app.config['UPLOAD_EXTENSIONS']:
                flash('Your image must be one of these types: [.jpg, .png, .gif].', 'error')
                return redirect(url_for('blog.register'))
        
            file.save('quote/static/images/profile_images/' + file_name)
            image = file_name

        db = get_db()
        username_exists = User.objects(user_name=user_name).first()

        if username_exists:
            flash('Username is already in use.', 'error')
        else:
            new_user = User(
                user_name=user_name,
                first_name=first_name,
                last_name=last_name,
                password=generate_password_hash(password, method='sha256'),
                phone_number=phone_number,
                email=email,
                image=image
            )

            new_user.save()

            return redirect(url_for('blog.login'))

    return render_template("user/register.html")


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        password = request.form.get("password")
        user_name = request.form.get("user_name")
        db = get_db()
        user = User.objects(user_name=user_name).first()

        # Check if user exists with this  username.
        if user:
            if check_password_hash(user["password"], password):

                session.clear()
                session['first_name'] = user.first_name
                session["user_id"] = str(user.id)
                session["profile_image"] = user.image

                return redirect(url_for('blog.home'))
            else:
                flash('Password is incorrect.', 'error')

        else:
            flash('Username does not exist.', 'error')

    return render_template("user/login.html")


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for("blog.home"))
