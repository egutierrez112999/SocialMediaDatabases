#This will be our python file for creating queries
import sqlite3
import random

class DissDB:

    def __init__(self):
        self.connection = sqlite3.connect("dissonance.db")
        self.cursor = self.connection.cursor()


    def getAllUsers(self):
        self.cursor.execute("SELECT * FROM users")
        return self.cursor.fetchall()

    def getOneUser(self, userID):
        data = [userID]
        self.cursor.execute("SELECT * FROM users WHERE user_id = ?", data)
        return self.cursor.fetchone()

    def createUser(self, username, email, date_created, password):
        user_id = random.randint(1005,99999)
        data = [user_id, username, email, date_created, password]
        self.cursor.execute("INSERT INTO users (user_id, username, email, date_created, password) VALUES (?,?,?,?,?)", data)
        self.connection.commit()

    def getFriends(self, user_id):
        data = [user_id]
        self.cursor.execute("SELECT users.username, friend_user_id, fu.username FROM users JOIN friends ON users.user_id = friends.user_id JOIN users AS fu ON friends.friend_user_id = fu.user_id WHERE friends.user_id = ?", data)
        friends = self.cursor.fetchall()
        return friends
        

#    Creating users
#    Adding relationships between users
#    Posting for a user
#    Checking the feed for a user (the most recent n posts of people that user follows)
#    Other interactions to use your additional features

db = DissDB()
db.createUser('cool_dude', 'cd@dude.com', 'feb_29_2023', 'iamacooldude')
print(db.getAllUsers())
#print(db.getOneUser(1000))
#print(db.getFriends(1000))
