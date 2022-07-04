import collections.abc
from getpass import getpass

from SQL.MODIFY import *
from SQL.SELECT import *

collections.Callable = collections.abc.Callable
import re, bcrypt
from colors import Color
from pyreadline import Readline

readline = Readline()


class mainClient:

    def modify_user(self, user):
        passwd = input("Enter your new password  :    ")
        passwd = passwd.strip()
        passwd = self.check_password(passwd)
        passwd = self.hash_password(passwd)
        update_password(passwd, user[0][0])
        Color.success("Your password have been successfully updated ")

    def check_password(self, password):  # Function to check if the password if checking all the rules
        check = False
        while check is False:
            check = self.pass_prompt(password)
            if check is False:
                Color.warning(
                    "Not a Valid Password, select an other one\nRemember the Rules : Lenght superior to 8, "
                    "one capital and small caps, a number and one special char : ")
                password = getpass("Password : ").strip()
            else:
                print("Valid Password")
                check = True
        return password

    def pass_prompt(self, password):
        if (len(password) < 8):
            check = False
        elif not re.search("[a-z]", password):
            check = False
        elif not re.search("[A-Z]", password):
            check = False
        elif not re.search("[0-9]", password):
            check = False
        elif not re.search("[_@!%&#?*$]", password):
            check = False
        elif re.search("\s", password):
            check = False
        else:
            check = True
        return check

    def hash_password(self, passwd):  # Hash the password for the user
        passwd = passwd.encode("utf-8")
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(passwd, salt)
        hashed = hashed.decode("utf-8")
        return hashed

    def show_user(self, users):
        count = 0
        for rows in users:
            Color.main("\n-User number: " + str(count + 1))
            Color.prompt("Nom: " + rows[1])
            Color.prompt("Prenom: " + rows[2])
            Color.prompt("Login: " + rows[3])
            site = self.show_site(rows[5])
            Color.prompt("Site: " + site)
            if rows[7] == 0:
                Color.prompt("Ban : Non")
            else:
                Color.prompt("Ban : Oui")

    def show_site(self, id):
        site = select_id_site(id)
        return site[0][0]

    def __init__(self):
        user = self.check_login()
        self.main_menu_users(user)

    def main_menu_users(self, user):  # Menu controller for a simple user
        Color.main("\n\n ********Welcome on the user interface !*********** ")

        while True:  # While loop to keep the user in the program
            Color.main("\n *********** MAIN MENU **************")
            self.show_menu_user()  # Print the menu
            command = input().strip()  # Input from user to select an action

            if command == "1":
                self.show_user(user)
            elif command == "2":
                self.modify_user(user)
            elif command == "0":
                Color.main("\n ********** Good bye !  ************")
                break
            else:
                print("Choose a valid number !")

    def check_login(self):
        Color.main("\n\n ******* WELCOME ! THIS PROGRAM WAS MADE BY LOEIZ-BI AND BAPTISTE ******** \n\n")
        userInfo = password_check = False

        while not userInfo:
            pseudo = input("- Enter your pseudo to login  : ").strip()
            userInfo = self.check_pseudo(pseudo)  # Check if the pseudo exist
            if not userInfo:
                Color.warning("\n !!!! Select an existing user !!!!! \n")
            else:
                count = 3
                while True:
                    print()
                    password = input("- Enter the password  :  ")
                    print(len(userInfo))
                    passwd = userInfo[0][4]
                    password_check = self.check_passwd(password, passwd)

                    if password_check:
                        break
                    else:
                        Color.warning("\n !!!!!! Wrong password !!!!!! " + str(count - 1) + " more try")
                        count -= 1

                    if count == 0:
                        quit()

        return userInfo

    def check_pseudo(self, pseudo):  # Check if the pseudo exist inside the file
        userInfo = sql_check_user(pseudo)
        return userInfo

    def check_passwd(self, passwd, hashed):  # Compare the password given in input with the one existing for the user
        check = bcrypt.checkpw(passwd.encode("utf-8"), hashed.encode("utf-8"))
        return check

    def show_menu_user(self):  # Display menu for the simple users
        print("\n")
        Color.prompt("Please enter a number to select an action : \n")
        Color.prompt("1 : Display my informations")
        Color.prompt("2 : Update my password")
        Color.prompt("0 : Leave the program")


start = mainClient()
