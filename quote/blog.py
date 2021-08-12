from flask import Blueprint, render_template, redirect, url_for,request, flash, session
from .models import User
from .database import get_db
from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint("blog", __name__)
bp.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


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
    if request.method == 'POST':
        user_name = request.form.get("user_name")
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        password = request.form.get("password")
        email = request.form.get("email")
        phone_number = request.form.get("phone_number")
        profile_image = request.form.get("profile_image")
        
        db = get_db()
        
        email_exists = User.objects(email=email).first()
        username_exists = User.objects(user_name=user_name).first()

        if email_exists:
            print('Email is already in use.', 'error')
        elif username_exists:
            print('Username is already in use.','error')
        elif len(user_name) < 2:
            print('Username is too short.', 'error')
        elif len(password) < 6:
            print('Password is too short.', 'error')
        elif len(email) < 6:
            print("Email is invalid.", 'error')  
        else:
            new_user = User(
            user_name =user_name,
            first_name=first_name,
            last_name=last_name,
            password=generate_password_hash(password, method='sha256'),
            phone_number=phone_number,
            email=email,
            image="img"      #must be fixed!
            )
            
            new_user.save()
            
            print('User created!')
            return redirect(url_for('blog.home'))

    return render_template("user/register.html")


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        password = request.form.get("password")
        email = request.form.get("email")
        
        db = get_db()
        
        user = User.objects(email=email).first()   #check if user exists by email.
        if user:
            if check_password_hash(user["password"], password):
                print("Logged in!",'success')
                return redirect(url_for('blog.home'))
            else:
                print('Password is incorrect.', 'error')
        else:
            print('Email does not exist.','error')

    return render_template("user/login.html")