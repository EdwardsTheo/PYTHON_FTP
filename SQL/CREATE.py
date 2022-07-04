import sqlite3

conn = sqlite3.connect('C:\\Users\\bapti\\Desktop\\SRC_FTP-master\\SQL\\ftpServer.db')
c = conn.cursor()

c.execute('''
          CREATE TABLE IF NOT EXISTS users
          ([users_id] INTEGER PRIMARY KEY, [fName] TEXT, [lName] TEXT, [login] TEXT, [password] TEXT, [site] INTEGER,
           [role] INTEGER, [ban] INTEGER)
          ''')

c.execute('''
          CREATE TABLE IF NOT EXISTS files
          ([files_id] INTEGER PRIMARY KEY, [fileName] TEXT, [fileType] INTEGER)
          ''')

c.execute('''
          CREATE TABLE IF NOT EXISTS userPerm
          ([userPerm_id] INTEGER PRIMARY KEY, [file_id] INTEGER, [users_id] INTEGER, [read] INTEGER, [write] INTEGER)
          ''')

c.execute('''
          CREATE TABLE IF NOT EXISTS city
          ([city_id] INTEGER PRIMARY KEY, [cityName] TEXT)
          ''')

##################################################
############### INSERT USERS #####################
##################################################

c.execute('''
          INSERT INTO users (users_id, fName, lName, login, password, site, role, ban)

                VALUES
                ('1', 'Baptiste', 'THEOBALD', 'btheobald', 'admin', '1', '0', '0')
          ''')

c.execute('''
          INSERT INTO users (users_id, fName, lName, login, password, site, role, ban)

                VALUES
                ('2', 'Fabien', 'PIRES', 'fpires', 'admin', '2', '1', '0')
          ''')

c.execute('''
          INSERT INTO users (users_id, fName, lName, login, password, site, role, ban)

                VALUES
                ('3', 'Loeiz-bi', 'KHEDJAM', 'lkhedjam', 'admin', '3', '1', '0')
          ''')

c.execute('''
          INSERT INTO users (users_id, fName, lName, login, password, site, role, ban)

                VALUES
                ('4', 'Loïc', 'MARCOU', 'lmarcou', 'admin', '4', '1', '0')
          ''')

##################################################
############### INSERT FILES #####################
##################################################

c.execute('''
          INSERT INTO files (files_id, fileName, fileType)
                VALUES
                ('1', 'MAIN', '0')
          ''')

c.execute('''
          INSERT INTO files (files_id, fileName, fileType)
                VALUES
                ('2', 'Paris', '0')
          ''')

c.execute('''
          INSERT INTO files (files_id, fileName, fileType)
                VALUES
                ('3', 'Poitiers', '0')
          ''')

c.execute('''
          INSERT INTO files (files_id, fileName, fileType)
                VALUES
                ('4', 'Rennes', '0')
          ''')

c.execute('''
          INSERT INTO files (files_id, fileName, fileType)
                VALUES
                ('5', 'Strasbourg', '0')
          ''')

##################################################
############### INSERT userPerm ##################
##################################################

c.execute('''
          INSERT INTO userPerm (userPerm_id, file_id, users_id, read, write)
                VALUES
                ('1', '2', '1', '1', '1')
          ''')

c.execute('''
          INSERT INTO userPerm (userPerm_id, file_id, users_id, read, write)
                VALUES
                ('2', '3', '2', '1', '1')
          ''')

c.execute('''
          INSERT INTO userPerm (userPerm_id, file_id, users_id, read, write)
                VALUES
                ('3', '4', '3', '1', '1')
          ''')

c.execute('''
          INSERT INTO userPerm (userPerm_id, file_id, users_id, read, write)
                VALUES
                ('4', '5', '4', '1', '1')
          ''')

##################################################
############### INSERT userCity ##################
##################################################

c.execute('''
          INSERT INTO city (city_id, cityName)
                VALUES
                ('1', 'Paris')
          ''')

c.execute('''
          INSERT INTO city (city_id, cityName)
                VALUES
                ('2', 'Poitier')
          ''')

c.execute('''
          INSERT INTO city (city_id, cityName)
                VALUES
                ('3', 'Rennes')
          ''')

c.execute('''
          INSERT INTO city (city_id, cityName)
                VALUES
                ('4', 'Nantes')
          ''')


conn.commit()
