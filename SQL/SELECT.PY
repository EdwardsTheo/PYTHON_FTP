from SQL.CONNECT import *


def sql_check_user(pseudo):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE login = ?", (pseudo,))
    rows = cur.fetchall()
    return rows


def sql_select_all_user():
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE role = 1")
    rows = cur.fetchall()
    return rows


def sql_select_info_user(pseudo):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE login = ?", (pseudo,))
    rows = cur.fetchall()
    return rows


def sql_show_city():
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT cityName FROM city")
    rows = cur.fetchall()
    return rows


def sql_get_city_id(city):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT city_id FROM city WHERE cityName = ?", (city,))
    rows = cur.fetchall()
    return rows


def select_id_site(id):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT cityName FROM city WHERE city_id = ?", (id,))
    rows = cur.fetchall()
    return rows


def sql_get_id_pseudo(pseudo):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT id FROM users WHERE login = ?", (pseudo,))
    rows = cur.fetchall()
    return rows


def sql_modify_pseudo(pseudo):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT login FROM users WHERE login NOT IN (?)", (pseudo,))
    rows = cur.fetchall()
    return rows


def sql_get_city_name(city):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT cityName FROM city WHERE city_id = ?", (city,))
    rows = cur.fetchall()
    return rows
