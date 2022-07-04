from CONNECT import *

def sql_delete_user(pseudo) :
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE login = ?", (pseudo,))
    conn.commit()
    conn.close()