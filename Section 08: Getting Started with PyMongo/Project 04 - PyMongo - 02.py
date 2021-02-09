import pymongo
from pymongo import MongoClient

client = MongoClient()
db = client.mydb
Users = db.users
Users.find().count()
Users.find({"password": "bbff", "username": "sara"}).count()