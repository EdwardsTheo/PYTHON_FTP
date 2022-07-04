import os
import zipfile
from datetime import datetime, timedelta, date
from os.path import exists


def create_file(): # Create the new log file
    today = date.today()
    d = today.strftime("%d_%m_%Y")
    name = "C:\\Users\\bapti\\Desktop\\pyFTP\\LOG\\STORAGE\\" + "ftpserver_log_" + d + ".log"
    with open(name, 'w') as f:
        f.write('###Beginning of the log file###')


def rotate_log():  # Zip the last day file
    d = datetime.today() - timedelta(days=1)
    d = d.strftime("%d_%m_%Y")
    logfile = "C:\\Users\\bapti\\Desktop\\pyFTP\\LOG\\STORAGE\\" + "ftpserver_log_" + d + ".log"
    file_exists = exists(logfile)
    if file_exists:
        logfile = "ftpserver_log_" + d + ".log"
        logarchive = "ftpserver_log_" + d + ".zip"
        os.chdir('C:\\Users\\bapti\\Desktop\\pyFTP\\LOG\\STORAGE\\')
        zipfile.ZipFile(logarchive, 'w').write(logfile)
        os.remove(logfile)


create_file()
rotate_log()
