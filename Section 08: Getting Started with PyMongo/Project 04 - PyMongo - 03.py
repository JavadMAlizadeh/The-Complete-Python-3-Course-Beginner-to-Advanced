import pymongo
from pymongo import MongoClient
import datetime

client = MongoClient()
db = client.mydb
Users = db.users

current_date = datetime.datetime.now()

old_date = datetime.datetime(2009, 8 ,11)
uid = Users.insert_one({"username": "beth", "date": current_date})

Users.find({"date": {"$gte": old_date}}).count()

Users.find({"date": {"$exists": True}}).count()

Users.find({"username": {"$ne": "sara"}}).count()

db.users.create_index([("username", pymongo.ASCENDING)])

