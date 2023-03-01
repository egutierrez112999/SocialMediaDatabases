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

    def getOneUser(self, user_name):
        data = [user_name]
        self.cursor.execute("SELECT * FROM users WHERE username = ?", data)
        return self.cursor.fetchone()

    def createUser(self, username, email, date_created, password):
        #create a user
        user_id = random.randint(1005,99999)
        data = [user_id, username, email, date_created, password]
        self.cursor.execute("INSERT INTO users (user_id, username, email, date_created, password) VALUES (?,?,?,?,?)", data)
        self.connection.commit()
        print(f"User {username} created!")

    def updateUser(self, user_id, username, email, password):
        #all fields to update: id, name, everything else
        user = self.getOneUser(username)
        data = [user[0], username, email ,user[3],password, user_id]
        self.cursor.execute("UPDATE users SET user_id = ?, username = ?, email = ?, date_created=?, password=? WHERE user_id = ?",data)
        self.connection.commit()
        print(f"User {username} successfully Updated")
        print(self.getOneUser(username))

    def addFriend(self, user_id, friend_id):
        #add friends
        data = [user_id, friend_id]
        fdata = [friend_id, user_id]
        self.cursor.execute("INSERT INTO friends (user_id, friend_user_id) VALUES (?, ?)",data)
        self.cursor.execute("INSERT INTO friends (user_id, friend_user_id) VALUES (?, ?)",fdata)
        print(f"Friendship Created between User {user_id} and User {friend_id}")
        self.connection.commit()

    def getFriends(self, user_id):
        #show friends
        data = [user_id]
        self.cursor.execute("SELECT users.username, friend_user_id, fu.username FROM users JOIN friends ON users.user_id = friends.user_id JOIN users AS fu ON friends.friend_user_id = fu.user_id WHERE friends.user_id = ?", data)
        friends = self.cursor.fetchall()
        return friends
        

    def createPost(self, user_id, channel_id, message):
        #check to see if they are a member of the server
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
                #create post
                post_id = random.randint(3000, 3999)
                timestamp = int(time.time())
                data = [post_id, channel_id, server_id, user_id, message, timestamp]
                pdata = [post_id]
                self.cursor.execute("INSERT INTO posts (post_id, channel_id, server_id, user_id, message, timestamp) VALUES (?, ?, ?, ?, ?, ?)", data)
                self.cursor.execute("INSERT INTO likes (post_id, user_id, like, dislike) VALUES (?, 0, 0, 0)",pdata)
                self.connection.commit()
                print("Successfully made Post")

    def deletePost(self, user_id, post_id):
        data = [post_id]
        self.cursor.execute("SELECT user_id FROM posts WHERE post_id = ?", data)
        user = (self.cursor.fetchone())
        if (user[0] == user_id):
            self.cursor.execute("DELETE FROM posts WHERE post_id = ?", data)
            self.cursor.execute("DELETE FROM likes WHERE post_id = ?", data)
            self.connection.commit()
            print(f"Post {post_id} Deleted")
            return
        print("Not the user of said post")


    def likeDislikePost(self, post_id, user_id, gusto):
        #check to see if the user has liked or dislike the post yet
        pdata = [post_id]
        self.cursor.execute("SELECT user_id FROM likes WHERE post_id = ?", pdata)
        found = self.cursor.fetchall()
        for i in found:
            if (i[0] == user_id):
                return
        if(gusto):#like the post
            data = [post_id, user_id]
            self.cursor.execute("INSERT INTO likes (post_id, user_id, like, dislike) VALUES (?, ?, 1, 0)", data)
            self.connection.commit()
            print("Post Liked")
        elif gusto == 0:#dislike the post
            data = [post_id, user_id]
            self.cursor.execute("INSERT INTO likes (post_id, user_id, like, dislike) VALUES (?, ?, 0, 1)", data)
            self.connection.commit()
            print("Post Disliked")

    def getFeedChannel(self, user_id, channel_name):
        #Check if user is a member of the server
        cdata = [channel_name]
        self.cursor.execute("SELECT channel_id, server_id FROM channels WHERE channel_name = ?",cdata)
        chdata = self.cursor.fetchall()
        server_members = self.getServerMembers(int(chdata[0][1]))
        member = False
        for i in server_members:
            if user_id == i[0]:
                member = True
        if(member):
                print("\nGetting Feed:")
                #if they are a member, show them their feed
                data = [chdata[0][0]]
                self.cursor.execute("SELECT u.username, message, SUM(like) AS likes, SUM(dislike) as dislikes FROM posts JOIN users AS u ON posts.user_id = u.user_id JOIN likes AS l ON posts.post_id = l.post_id WHERE channel_id = ? GROUP BY posts.post_id ORDER BY timestamp ASC LIMIT 10;",data)
                return self.cursor.fetchall()


    def joinServer(self, user_id, server_id, server_name):
        #check if user has been blacklisted
        sdata = [server_id]
        self.cursor.execute("SELECT user_id FROM blacklist WHERE server_id = ?", sdata)
        blacklisted_users = self.cursor.fetchall()
        for i in blacklisted_users:
            if i[0] == user_id:
                print("Cannot Join Because You have Been Banned")
                return
        #check if user is already a member
        server_members = self.getServerMembers(server_id)
        member = False
        for i in server_members:
            if user_id == i[0]:
                member = True
        if(member == False):
            #join Server
            data = [server_id, server_name, user_id]
            self.cursor.execute("INSERT INTO servers (server_id, server_name, user_id) VALUES (?, ?, ?)", data)
            self.connection.commit()
            print('Server Joined')
            return
        print(f'Already a Member of Server {server_name}')
        

    def getServerMembers(self, server_id):
        #get members for a given server
        data = [server_id]
        self.cursor.execute("SELECT user_id FROM servers WHERE server_id = ?", data)
        return self.cursor.fetchall()

    def getChannels(self, server_id):
        #get channels for a given server
        data = [server_id]
        self.cursor.execute("SELECT * FROM channels WHERE server_id = ?", data)
        return self.cursor.fetchall()

    def addChannel(self, user_id, channel_id, channel_name, server_id):
        #test to see if user is owner
        server_data = [server_id]
        self.cursor.execute("SELECT user_id FROM owners WHERE server_id = ?", server_data)
        server_owner = self.cursor.fetchone()
        owner = (user_id == server_owner[0])
        if (owner):
            #if owner, create channel
            data = [channel_id, channel_name, server_id]
            self.cursor.execute("INSERT INTO channels (channel_id, channel_name, server_id) VALUES (?, ?, ?)",data)
            self.connection.commit()
            print('Channel Made Succesfully')
            return
        print('YOU ARE NOT THE OWNER')

        def IntQuery1(self):
            #maybe if you are a owner, you can see all of the banned users?
            pass



def displayList(lst):
    for i in lst:
        print(i)


#initialize Database Class
print("Initializing DB....\n\n")
db = DissDB()

#Creating users
print("---Testing Create Users-------")
print("Current Users: ")
displayList(db.getAllUsers())
db.createUser('cool_dude', 'cd@dude.com', 'feb_29_2023', 'iamacooldude')
db.createUser('dj', 'holt@gmail.com', 'feb_29_2023', 'applesux')
db.createUser('bob', 'computerbob@gmail.com', 'feb_29_2023', 'password123')
print("Current Users: ")
displayList(db.getAllUsers())
print("Updating User Soviet Bear: ")
db.updateUser(1001, 'sovietbear1945', 'bear@gmail.com', 'password123')
print("Current Users: ")
displayList(db.getAllUsers())


print("\n\n---Testing Relationships-------")
print("Showing Friends For User sovietbear1945")
displayList(db.getFriends(1001))
db.addFriend(1001,1003)
db.addFriend(1001,1002)
displayList(db.getFriends(1001))


print("\n\n---Testing Post and Feed Functionality-------")
displayList(db.getFeedChannel(1000, 'discussion'))
db.likeDislikePost(3000, 1005 ,1);
db.likeDislikePost(3000, 1005 ,0);
displayList(db.getFeedChannel(1000, 'discussion'))
db.createPost(1000, 20020, "I love fruit")
db.createPost(1001, 20020, "What is computer science?")
displayList(db.getFeedChannel(1000, 'discussion'))
db.deletePost(1001,3000)
db.deletePost(1000,3000)
displayList(db.getFeedChannel(1000, 'discussion'))


print("\n\n---Testing Other Functionality-------")
displayList(db.getChannels(2000))
print("Non Owner Creating a new channel: ")
db.addChannel(1000, 20005, 'volunteers', 2000)
print("Owner Creating a new channel: ")
db.addChannel(1003, 20005, 'volunteers', 2000)
displayList(db.getChannels(2000))
print("\nGetting Server Members: ")
displayList(db.getServerMembers(2002))
print("\nJoining a Server as a member already: ")
db.joinServer(1000,2000, 'cs')
print("\nJoining a Server not already joined: ")
db.joinServer(1002,2002, 'research_seminar')
displayList(db.getServerMembers(2002))


