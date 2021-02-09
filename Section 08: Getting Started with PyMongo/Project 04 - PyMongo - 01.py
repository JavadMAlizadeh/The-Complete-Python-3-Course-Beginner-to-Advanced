from pymongo import MongoClient

myClient = MongoClient()
db = myClient.mydb
users = db.user
user1 = {"username": "nick", "password": "mysecurepassword", "favorite_number": 333, "hobbies": ["programming", "onlinecourses", "workingpaper"]}
user_id = users.insert_one(user1).inserted_id

users =[{"username": "alex", "password": "bbff"}, {"username": "sara", "pasword": 123456}]
Users =db.users
Ins = Users.insert_many(users)
Ins.inserted_ids


