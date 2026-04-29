from database import get_connection

def get_all_doctors():
    conn = get_connection()
    rows = conn.cursor().execute("select * from doctors").fetchall()
    conn.close()
    return [dict(row)for row in rows]

def get_doctor_by_id(doctor_id: int):
    conn = get_connection()
    row = conn.cursor().execute("select * from doctors where id=?",(doctor_id,)).fetchone()
    conn.close()
    return dict(row) if row else None

def create_doctor(data:dict):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("insert into doctors (name, profession, age, available) values (?,?,?,?)",
                   (data['name'], data['profession'], data['age'], data['available']))
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return new_id

