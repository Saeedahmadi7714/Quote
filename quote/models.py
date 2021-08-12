from mongoengine import *


class User(Document):
    user_name = StringField(max_length=50, required=True)
    first_name = StringField(max_length=50, required=True)
    last_name = StringField(max_length=50, required=True)
    password = StringField(max_length=100, required=True)
    email = StringField(max_length=50)
    phone_number = StringField(max_length=15, required=True)
    image = StringField(max_length=200, required=True)


class Post(Document):
    title = StringField(max_length=50, required=True)
    author = ReferenceField('User', reverse_delete_rule=CASCADE)
    content = StringField(max_length=5000,min_length=120)
    image_path = StringField(max_length=200)
    pub_date = DateTimeField()
    likes = ListField()
    comments = ListField()
    tags = ListField()


class Comment(Document):
    owner = ReferenceField('User', reverse_delete_rule=CASCADE)
    text = StringField(max_length=200)
    created_date = DateTimeField()


class Tag(Document):
    name = StringField(max_length=50)
