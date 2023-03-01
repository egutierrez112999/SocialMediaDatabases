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

    def addFriend(self, user_id, friend_id):
        data = [user_id, friend_id]
        fdata = [friend_id, user_id]
        self.cursor.execute("INSERT INTO friends (user_id, friend_user_id) VALUES (?, ?)",data)
        self.cursor.execute("INSERT INTO friends (user_id, friend_user_id) VALUES (?, ?)",fdata)
        self.connection.commit()

    def getFriends(self, user_id):
        data = [user_id]
        self.cursor.execute("SELECT users.username, friend_user_id, fu.username FROM users JOIN friends ON users.user_id = friends.user_id JOIN users AS fu ON friends.friend_user_id = fu.user_id WHERE friends.user_id = ?", data)
        friends = self.cursor.fetchall()
        return friends
        
    def createPost(self):
        pass

    def getFeedChannel(self):
        pass

    def likeDislikePost(self):
        pass

    def joinServer(self, user_id, server_id, server_name):
        server_members = self.getServerMembers(server_id)
        member = False
        for i in server_members:
            if user_id == i[0]:
                member = True
        if(member == False):
            data = [server_id, server_name, user_id]
            self.cursor.execute("INSERT INTO servers (server_id, server_name, user_id) VALUES (?, ?, ?)", data)
            self.connection.commit()
            print('Server Joined')
            return
        print(f'Already a Member of Server {server_name}')
        

    def getServerMembers(self, server_id):
        data = [server_id]
        self.cursor.execute("SELECT user_id FROM servers WHERE server_id = ?", data)
        return self.cursor.fetchall()

    def getChannels(self, server_id):
        data = [server_id]
        self.cursor.execute("SELECT * FROM channels WHERE server_id = ?", data)
        return self.cursor.fetchall()

    def addChannel(self, user_id, channel_id, channel_name, server_id):
        server_data = [server_id]
        self.cursor.execute("SELECT user_id FROM owners WHERE server_id = ?", server_data)
        server_owner = self.cursor.fetchone()
        owner = (user_id == server_owner[0])
        if (owner):
            data = [channel_id, channel_name, server_id]
            self.cursor.execute("INSERT INTO channels (channel_id, channel_name, server_id) VALUES (?, ?, ?)",data)
            self.connection.commit()
            print('Channel Made Succesfully')
            return
        print('YOU ARE NOT THE OWNER')



db = DissDB()
#db.createUser('cool_dude', 'cd@dude.com', 'feb_29_2023', 'iamacooldude')
#print(db.getAllUsers())
#print(db.getOneUser(1000))
#print(db.getFriends(1001))
#db.addFriend(1001,1003)
#print(db.getFriends(1001))


#print(db.getChannels(2000))
#db.addChannel(1000, 20005, 'volunteers', 2000)
#db.addChannel(1003, 20005, 'volunteers', 2000)
#print(db.getChannels(2000))

#print(db.getServerMembers(2000))
#db.joinServer(1000,2000, 'cs')


