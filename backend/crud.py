from database import get_connection

def get_all_books():
    conn = get_connection()
    rows = conn.execute("SELECT*FROM books").fetchall()
    conn.close()
    return [dict(rows) for row in rows]

def get_book_by_id(book_id: int):
    conn = get_connection()
    row = conn.execute("SELECT*FROM books WHERE id = ?", (book_id,)).fetchone()
    conn.close()
    return dict(row) if row else None
