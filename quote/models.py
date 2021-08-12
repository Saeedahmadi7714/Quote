from mongoengine import *


class User(Document):
    user_name = StringField(max_length=50, required=True)
    first_name = StringField(max_length=50, required=True)
    last_name = StringField(max_length=50, required=True)
    password = StringField(max_length=100, required=True)
    email = StringField(max_length=50)
    phone_number = StringField(max_length=15, required=True)
    image = StringField(max_length=200, required=True)
