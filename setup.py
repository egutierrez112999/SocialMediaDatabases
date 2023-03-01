import sqlite3

con = sqlite3.connect("dissonance.db")
cur = con.cursor()

#Recreate All tables
cur.execute("DROP TABLE servers")
cur.execute("DROP TABLE users")
cur.execute("DROP TABLE posts")
cur.execute("DROP TABLE likes")
cur.execute("DROP TABLE channels")
cur.execute("DROP TABLE blacklist")
cur.execute("DROP TABLE owners")
cur.execute("DROP TABLE friends")
cur.execute("CREATE TABLE IF NOT EXISTS servers (server_id INTEGER, server_name TEXT,user_id INTEGER)")
cur.execute("CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, username TEXT, email TEXT, date_created TEXT, password TEXT)")
cur.execute("CREATE TABLE IF NOT EXISTS posts (post_id INTEGER PRIMARY KEY, channel_id INTEGER, server_id INTEGER, user_id INTEGER, message TEXT, timestamp VARCHAR(30))")
cur.execute("CREATE TABLE IF NOT EXISTS likes (post_id INTEGER PRIMARY KEY, user_id INTEGER, like INTEGER, dislike INTEGER)")
cur.execute("CREATE TABLE IF NOT EXISTS blacklist (server_ID INTEGER, user_id INTEGER)")
cur.execute("CREATE TABLE IF NOT EXISTS owners (server_id INTEGER PRIMARY KEY, user_id INTEGER)")
cur.execute("CREATE TABLE IF NOT EXISTS friends (user_id INTEGER, friend_user_id INTEGER)")
cur.execute("CREATE TABLE IF NOT EXISTS channels (channel_id INTEGER PRIMARY KEY, server_id INTEGER)")

#insert Users
cur.execute("INSERT INTO users (user_id, username, email, date_created, password) VALUES (1000, 'usidorethewizard', 'colby@gmail.com', 'feb_29_2023', 'asdf')")
cur.execute("INSERT INTO users (user_id, username, email, date_created, password) VALUES (1001, 'sovietbear1945', 'erick@gmail.com', 'feb_29_2023', 'SemiSecurePwd11')")
cur.execute("INSERT INTO users (user_id, username, email, date_created, password) VALUES (1002, 'fractal13', 'curtis@gmail.com', 'feb_29_2023', 'emacsisawesome')")
cur.execute("INSERT INTO users (user_id, username, email, date_created, password) VALUES (1003, 'russross', 'russ@gmail.com', 'feb_29_2023', 'apple2easy')")
cur.execute("INSERT INTO users (user_id, username, email, date_created, password) VALUES (1004, 'bartstander', 'bart@gmail.com', 'feb_29_2023', 'hawaiianstyle')")
cur.execute("INSERT INTO users (user_id, username, email, date_created, password) VALUES (1005, 'renquinn', 'ren@gmail.com', 'feb_29_2023', 'backonsoylent')")
con.commit()

#insert servers
cur.execute("INSERT INTO servers (server_id, server_name, user_id) VALUES (2000, 'cs', 1004)")
con.commit()
#insert friends

#insert owners

#insert blacklist

#insert channels

#insert posts

#insert likes
