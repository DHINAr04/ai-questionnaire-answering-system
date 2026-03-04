import sqlite3

conn = sqlite3.connect("app.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS answers (
id INTEGER PRIMARY KEY AUTOINCREMENT,
question TEXT,
answer TEXT,
citation TEXT
)
""")

conn.commit()