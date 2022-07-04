from CONNECT import *

def sql_insert_user(first_name,last_name,pseudo,passwd,city,ban) :
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("insert into users (fName, lName, login, password, site, role, ban) values (?, ?, ?, ?, ?, ?, ?)",
                (first_name, last_name, pseudo, passwd,city, '1', ban))
    conn.commit()
    conn.close()