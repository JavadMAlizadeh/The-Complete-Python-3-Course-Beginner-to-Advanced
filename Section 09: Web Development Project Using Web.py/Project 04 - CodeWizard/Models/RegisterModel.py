import pymongo
from pymongo import MongoClient
import bcrypt

class RegisterModel:

    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.codewizard
        self.Users = self.db.users

    def insert_user(self, data):
        hashed = bcrypt.hashpw(data.password.encode(), bcrypt.gensalt())

        id = self.Users.insert({"username": data.username, "name": data.name, "password": hashed, "email": data.email})
        print("UID is", id)
        myuser = self.Users.find_one({'username': data.username})

        if bcrypt.checkpw("123@456#789".encode(), myuser["password"]):
            print("This matches!")
