from aifc import Error
import sqlite3


def create_connection():
    conn = None
    try:
        conn = sqlite3.connect('C:\\Users\\bapti\\Desktop\\PYTHON_FTP\\SQL\\ftpServer.db')
    except Error as e:
        print(e)

    return conn
