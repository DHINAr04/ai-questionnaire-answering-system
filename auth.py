import sqlite3
import hashlib

conn = sqlite3.connect("app.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
email TEXT UNIQUE,
password TEXT
)
""")

conn.commit()


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def signup(email, password):

    hashed = hash_password(password)

    try:
        cursor.execute(
            "INSERT INTO users(email,password) VALUES (?,?)",
            (email, hashed)
        )
        conn.commit()
        return True
    except:
        return False


def login(email, password):

    hashed = hash_password(password)

    cursor.execute(
        "SELECT password FROM users WHERE email=?",
        (email,)
    )

    user = cursor.fetchone()

    if user and user[0] == hashed:
        return True

    return False