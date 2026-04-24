import sqlite3

DB_NAME = "app.db"

def get_connection():
    conn=sqlite3.connect(DB_NAME)
    conn.row_factory=sqlite3.Row
    return conn

def init_db():
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            available BOOLEAN
    """)
    conn.commit()

    conn.close()