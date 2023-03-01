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
cur.execute("CREATE TABLE IF NOT EXISTS servers (server_id INTEGER PRIMARY KEY, user_id INTEGER, date_created TEXT)")
cur.execute("CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, username TEXT, email TEXT, date_created TEXT, password TEXT)")
cur.execute("CREATE TABLE IF NOT EXISTS posts (post_id INTEGER PRIMARY KEY, channel_id INTEGER, server_id INTEGER, user_id INTEGER, message TEXT, timestamp VARCHAR(30))")
cur.execute("CREATE TABLE IF NOT EXISTS likes (post_id INTEGER PRIMARY KEY, user_id INTEGER, like INTEGER, dislike INTEGER)")
cur.execute("CREATE TABLE IF NOT EXISTS blacklist (server_ID INTEGER, user_id INTEGER)")
cur.execute("CREATE TABLE IF NOT EXISTS owners (server_id INTEGER PRIMARY KEY, user_id INTEGER)")
cur.execute("CREATE TABLE IF NOT EXISTS friends (user_id INTEGER, friend_user_id INTEGER)")
cur.execute("CREATE TABLE IF NOT EXISTS channels (channel_id INTEGER PRIMARY KEY, server_id INTEGER)")

#insert Users
cur.execute("INSERT INTO users (user_id, username, email, date_created, password) VALUES (1000, 'usidorethewizard', 'colby@gmail.com', 'feb_29_2023', 'asdf')")
con.commit()
