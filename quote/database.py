from flask import current_app
from flask import g
from pymongo import MongoClient


def get_db():

    if "db" not in g:
        client = MongoClient('mongodb://127.0.0.1:27017')
        db_name = current_app.config['DB_NAME']
        g.db = client[db_name]

    return g.db
