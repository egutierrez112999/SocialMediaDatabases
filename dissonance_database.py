#This will be our python file for creating queries
import sqlite3
import random
import time

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
        

    def createPost(self, user_id, channel_id, message):
        cdata = [channel_id]
        self.cursor.execute("SELECT server_id FROM channels WHERE channel_id = ?",cdata)
        chdata = self.cursor.fetchone()
        server_id = int(chdata[0])
        server_members = self.getServerMembers(server_id)
        member = False
        for i in server_members:
            if user_id == i[0]:
                member = True
        if(member):
                post_id = random.randint(3000, 3999)
                timestamp = time.time()
                data = [post_id, channel_id, server_id, user_id, message, timestamp]
                self.cursor.execute("INSERT INTO posts (post_id, channel_id, server_id, user_id, message, timestamp) VALUES (?, ?, ?, ?, ?, ?)", data)
                self.connection.commit()
                print("Successfully made Post")


    def likeDislikePost(self, post_id, user_id, gusto):
        pdata = [post_id]
        self.cursor.execute("SELECT user_id FROM likes WHERE post_id = ?", pdata)
        found = self.cursor.fetchall()
        for i in found:
            if (i[0] == user_id):
                return
        if(gusto):
            data = [post_id, user_id]
            self.cursor.execute("INSERT INTO likes (post_id, user_id, like, dislike) VALUES (?, ?, 1, 0)", data)
            self.connection.commit()
            print("Post Liked")
        elif gusto == 0:
            data = [post_id, user_id]
            self.cursor.execute("INSERT INTO likes (post_id, user_id, like, dislike) VALUES (?, ?, 0, 1)", data)
            self.connection.commit()
            print("Post Disliked")

    def getFeedChannel(self, user_id, channel_name):
        cdata = [channel_name]
        self.cursor.execute("SELECT channel_id, server_id FROM channels WHERE channel_name = ?",cdata)
        chdata = self.cursor.fetchall()
        server_members = self.getServerMembers(int(chdata[0][1]))
        member = False
        for i in server_members:
            if user_id == i[0]:
                member = True
        if(member):
                data = [chdata[0][0]]
                self.cursor.execute("SELECT u.username, message FROM posts JOIN users AS u ON posts.user_id = u.user_id WHERE channel_id = ? ORDER BY timestamp ASC LIMIT 10", data)
                return self.cursor.fetchall()


    def joinServer(self, user_id, server_id, server_name):
        sdata = [server_id]
        self.cursor.execute("SELECT user_id FROM blacklist WHERE server_id = ?", sdata)
        blacklisted_users = self.cursor.fetchall()
        for i in blacklisted_users:
            if i[0] == user_id:
                print("Cannot Join Because You have Been Banned")
                return
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

#print(db.getServerMembers(2002))
#db.joinServer(1000,2000, 'cs')

#print(db.getFeedChannel(1000, 'discussion'))
#db.createPost(1000, 20020, "I love fruit")
#print(db.getFeedChannel(1000, 'discussion'))

db.joinServer(1002,2002, 'research_seminar')
#db.likeDislikePost(3000, 1002 ,1);
#db.likeDislikePost(3000, 1002 ,0);
