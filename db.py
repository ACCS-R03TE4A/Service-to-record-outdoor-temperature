# from pymongo import MongoClient
# from flaskr.config import DATABASE_NAME

# client = MongoClient()
# db = client[DATABASE_NAME]

from mongoengine import connect, Document, StringField
from config import DATABASE_CONNECTINO_STRING

connect(host=DATABASE_CONNECTINO_STRING)#pip install