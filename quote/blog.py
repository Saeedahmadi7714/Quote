from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from .models import User
from .database import get_db
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from mongoengine import FieldDoesNotExist

bp = Blueprint("blog", __name__)


@bp.route("/home/")
@bp.route("/")
def home():
    db = get_db()
    return render_template('blog/index.html')


@bp.route('/post/<post_id>')
def post(post_id):
    pass


@bp.route('/category-posts/<category_id>')
def category(category_id):
    pass


@bp.route('/tag-posts/<tag_id>')
def tag(tag_id):
    pass


@bp.route('/register', methods=['GET', 'POST'])
def register():
    try:
        if request.method == 'POST':
            user_name = request.form.get("user_name")
            first_name = request.form.get("first_name")
            last_name = request.form.get("last_name")
            password = request.form.get("password")
            email = request.form.get("email")
            phone_number = request.form.get("phone_number")
            file = request.files.get('profile_image')
            if file:
                file_name = secure_filename(file.filename)
                file.save('quote/static/images/profile_images/' + file_name)
                image = file_name
            else:
                image = None
    
            db = get_db()
    
            email_exists = User.objects(email=email).first()
            username_exists = User.objects(user_name=user_name).first()
    
            if email_exists:
                flash('Email is already in use.')
            elif username_exists:
                flash('Username is already in use.')
            elif len(user_name) < 2:
                flash('Username is too short.')
            elif len(password) < 6:
                flash('Password is too short.')
            elif len(email) < 6:
                flash("Email is invalid.")
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
    
                flash('User created!')
                return redirect(url_for('blog.home'))
    
        return render_template("user/register.html")
    
    except FieldDoesNotExist:
        return render_template("user/register.html")
        


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        password = request.form.get("password")
        user_name = request.form.get("user_name")
        db = get_db()
        user = User.objects(user_name=user_name).first()  
        
        # check if user exists by username.
        if user:
            if check_password_hash(user["password"], password):
                # session['first_name'] = user['first_name']
                # session['user_name'] = user['user_name']
                # session["user_id"] = str(user["_id"])
                # session["profile_image"] = user["_id"]
                flash("Logged in!")

                return redirect(url_for('blog.home'))
            else:
                flash('Password is incorrect.')
                
        else:
            flash('Username does not exist.')


    return render_template("user/login.html")


@bp.route('/logout', methods=['GET', 'POST'])
def logout():
    pass
