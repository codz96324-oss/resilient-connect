import sqlite3

conn = sqlite3.connect("messages.db")
cur = conn.cursor()

cur.execute(
    '''
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        content TEXT
    )
'''
)

conn.commit()

def save_message(message):
    cur.execute("INSERT INTO messages (content) VALUES (?)", (message,))
    conn.commit()
