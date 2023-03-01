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
cur.execute("CREATE TABLE IF NOT EXISTS likes (post_id INTEGER, user_id INTEGER, like INTEGER, dislike INTEGER)")
cur.execute("CREATE TABLE IF NOT EXISTS blacklist (server_ID INTEGER, user_id INTEGER)")
cur.execute("CREATE TABLE IF NOT EXISTS owners (server_id INTEGER PRIMARY KEY, user_id INTEGER)")
cur.execute("CREATE TABLE IF NOT EXISTS friends (user_id INTEGER, friend_user_id INTEGER)")
cur.execute("CREATE TABLE IF NOT EXISTS channels (channel_id INTEGER PRIMARY KEY, channel_name TEXT, server_id INTEGER)")

#insert Users
cur.execute("INSERT INTO users (user_id, username, email, date_created, password) VALUES (1000, 'usidorethewizard', 'colby@gmail.com', 'feb_29_2023', 'asdf')")
cur.execute("INSERT INTO users (user_id, username, email, date_created, password) VALUES (1001, 'sovietbear1945', 'erick@gmail.com', 'feb_29_2023', 'SemiSecurePwd11')")
cur.execute("INSERT INTO users (user_id, username, email, date_created, password) VALUES (1002, 'fractal13', 'curtis@gmail.com', 'feb_29_2023', 'emacsisawesome')")
cur.execute("INSERT INTO users (user_id, username, email, date_created, password) VALUES (1003, 'russross', 'russ@gmail.com', 'feb_29_2023', 'apple2easy')")
cur.execute("INSERT INTO users (user_id, username, email, date_created, password) VALUES (1004, 'bartstander', 'bart@gmail.com', 'feb_29_2023', 'hawaiianstyle')")
cur.execute("INSERT INTO users (user_id, username, email, date_created, password) VALUES (1005, 'renquinn', 'ren@gmail.com', 'feb_29_2023', 'backonsoylent')")
con.commit()

#insert servers
cur.execute("INSERT INTO servers (server_id, server_name, user_id) VALUES (2000, 'cs', 1000)")
cur.execute("INSERT INTO servers (server_id, server_name, user_id) VALUES (2000, 'cs', 1001)")
cur.execute("INSERT INTO servers (server_id, server_name, user_id) VALUES (2000, 'cs', 1002)")
cur.execute("INSERT INTO servers (server_id, server_name, user_id) VALUES (2000, 'cs', 1003)")
cur.execute("INSERT INTO servers (server_id, server_name, user_id) VALUES (2000, 'cs', 1004)")
cur.execute("INSERT INTO servers (server_id, server_name, user_id) VALUES (2000, 'cs', 1005)")
cur.execute("INSERT INTO servers (server_id, server_name, user_id) VALUES (2002, 'research_seminar', 1000)")
cur.execute("INSERT INTO servers (server_id, server_name, user_id) VALUES (2002, 'research_seminar', 1001)")
cur.execute("INSERT INTO servers (server_id, server_name, user_id) VALUES (2002, 'research_seminar', 1003)")
cur.execute("INSERT INTO servers (server_id, server_name, user_id) VALUES (2002, 'research_seminar', 1005)")
con.commit()

#insert friends
cur.execute("INSERT INTO friends (user_id, friend_user_id) VALUES (1000, 1001)")
cur.execute("INSERT INTO friends (user_id, friend_user_id) VALUES (1001, 1000)")
cur.execute("INSERT INTO friends (user_id, friend_user_id) VALUES (1000, 1002)")
cur.execute("INSERT INTO friends (user_id, friend_user_id) VALUES (1002, 1000)")
cur.execute("INSERT INTO friends (user_id, friend_user_id) VALUES (1000, 1003)")
cur.execute("INSERT INTO friends (user_id, friend_user_id) VALUES (1003, 1000)")
cur.execute("INSERT INTO friends (user_id, friend_user_id) VALUES (1000, 1004)")
cur.execute("INSERT INTO friends (user_id, friend_user_id) VALUES (1004, 1000)")
cur.execute("INSERT INTO friends (user_id, friend_user_id) VALUES (1000, 1005)")
cur.execute("INSERT INTO friends (user_id, friend_user_id) VALUES (1005, 1000)")
cur.execute("INSERT INTO friends (user_id, friend_user_id) VALUES (1003, 1005)")
cur.execute("INSERT INTO friends (user_id, friend_user_id) VALUES (1005, 1003)")
cur.execute("INSERT INTO friends (user_id, friend_user_id) VALUES (1001, 1005)")
cur.execute("INSERT INTO friends (user_id, friend_user_id) VALUES (1005, 1001)")
con.commit()

#insert owners
cur.execute("INSERT INTO owners (server_id, user_id) VALUES (2000, 1003)")
cur.execute("INSERT INTO owners (server_id, user_id) VALUES (2002, 1005)")
con.commit()

#insert blacklist
cur.execute("INSERT INTO blacklist (server_id, user_id) VALUES (2002, 1002)")
cur.execute("INSERT INTO blacklist (server_id, user_id) VALUES (2002, 1004)")
con.commit()

#insert channels
cur.execute("INSERT INTO channels (channel_id, channel_name, server_id) VALUES (20000, 'teachers', 2000)")
cur.execute("INSERT INTO channels (channel_id, channel_name, server_id) VALUES (20001, 'students', 2000)")
cur.execute("INSERT INTO channels (channel_id, channel_name, server_id) VALUES (20002, 'supervisors', 2000)")
cur.execute("INSERT INTO channels (channel_id, channel_name, server_id) VALUES (20020, 'discussion', 2002)")
con.commit()

#insert posts
cur.execute("INSERT INTO posts (post_id, channel_id, server_id, user_id, message, timestamp) VALUES (3000, 20020, 2002, 1000, 'That paper was really good! I loved it!', '1677698679')")
con.commit()
#insert likes
cur.execute("INSERT INTO likes (post_id, user_id, like, dislike) VALUES (3000, 1003, 1, 0)")
cur.execute("INSERT INTO likes (post_id, user_id, like, dislike) VALUES (3000, 1005, 1, 0)")
cur.execute("INSERT INTO likes (post_id, user_id, like, dislike) VALUES (3000, 1001, 0, 1)")
con.commit()

