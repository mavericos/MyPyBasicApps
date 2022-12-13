import sqlite3
import hashlib

conn = sqlite3.connect("userdata.db")
cur = conn.cursor()

cur.execute(
""" 
CREATE TABLE IF NOT EXIST userdata (
    if INTEGER PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
)
""")

username1, password1 = "Mitko", hashlib.sha256("mitkospass".encode()).hexdigest()
username2, password2 = "Svetla", hashlib.sha256("svetlaspass".encode()).hexdigest()
username3, password3 = "Spaska", hashlib.sha256("spaskaspass".encode()).hexdigest()
username4, password4 = "Stanka", hashlib.sha256("stankaspass".encode()).hexdigest()
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username1, password1))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username2, password2))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username3, password3))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username4, password4))

conn.commit()