#This will be our python file for creating queries
import sqlite3

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

    def createUser(self, user_id, username, email, date_created, password):

db = DissDB()
print(db.getAllUsers())
print(db.getOneUser(1000))
