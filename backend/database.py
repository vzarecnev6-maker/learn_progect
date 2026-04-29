import sqlite3

DB_NAME = 'app.db'

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS doctors(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    profession TEXT NOT NULL,
    age INTEGER NOT NULL,
    available INTEGER NOT NULL''')
    conn.commit()
    conn.close()

