import collections.abc
from getpass import getpass
from SQL.CONNECT import *
from SQL.DELETE import *
from SQL.INSERT import *
from SQL.MODIFY import *
from SQL.SELECT import *
collections.Callable = collections.abc.Callable
import re, bcrypt
from pyreadline import Readline

readline = Readline()
# Main menu
from colorama import init, deinit
from colors import Color


class Main:

    #########################
    #### USER MANAGEMENT#####
    #########################

    def add_user(self):  # Function to add an user
        Color.main("\n *********** ADD MENU ************** \n")
        first_name = input("Enter the first name of the user   :   ").strip()
        last_name = input("Enter the last name of the user   :   ").strip()
        last_name = last_name.upper()
        pseudo = input("Enter the pseudo of the user   :   ").strip()
        pseudo = self.check_pseudo_loop(pseudo)
        Color.warning(
            "****** Remember the Rules : Lenght superior to 8, one capital and small caps, a number and one special char ****** ")
        passwd = getpass("Enter the password of the user   :    \n")
        passwd = passwd.strip()
        passwd = self.check_password(passwd)
        passwd = self.hash_password(passwd)
        city_stored = self.show_city_avaible()
        city = input("Where this user is working ?:    ").strip()
        self.check_city(city, city_stored)
        city = self.get_city_id(city)
        ban = input("User banned or not, 0 = No, 1 = Yes:    ").strip()
        ban = self.check_ban(ban)
        sql_insert_user(first_name, last_name, pseudo, passwd, city[0][0], ban)
        Color.success("The user has been created !")

    def know_pseudo_id(self, pseudo):
        id = sql_get_id_pseudo(pseudo)
        return id

    def check_pseudo_loop(self, pseudo):
        check = False
        while not check:
            user = self.check_pseudo(pseudo)
            if user:
                Color.warning("\n !!!!!!! This pseudo is already taken !!!!!! ")
                pseudo = input("pseudo  :").strip()
            else:
                check = True
        return pseudo

    def check_password(self, password):  # Function to check if the password if checking all the rules
        check = False
        while check is False:
            check = self.pass_prompt(password)
            if check is False:
                Color.warning(
                    "Not a Valid Password, select an other one\nRemember the Rules : Lenght superior to 8, one capital and small caps, a number and one special char : ")
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

    def get_city_id(self, city):
        city = sql_get_city_id(city)
        return city

    def show_city_avaible(self):
        city = sql_show_city()
        for rows in city:
            print("\nThe city available are :    " + str(rows[0]))
        return city

    def check_city(self, city, city_stored):
        check = self.city_equal_stored(city, city_stored)
        while not check:
            Color.warning("\n !!!!!!! This city is not available !!!!!! ")
            self.show_city_avaible()
            city = input("Choose a city again  :").strip()
        return city

    def city_equal_stored(self, city, city_stored):
        check = False
        for rows in city_stored:
            if str(rows[0]) == city:
                check = True
        return check

    def main_list_user(self):
        Color.main("\n\n Enter an username or use 'all' to show all available users")
        command = input().strip()  # Input from user to select an action
        if command == 'all':
            users = sql_select_all_user()
        else:
            users = sql_check_user(command)
        self.show_user(users)

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

            count = count + 1

    def check_ban(self, ban):
        check = False
        while not check:
            if (ban == "0") or (ban == "1"):
                check = True
            else:
                Color.warning("\n Please select a correct value n \n")
                ban = input("User banned or not, 0 = No, 1 = Yes:    ").strip()
                print(ban)
        return ban

    def show_site(self, id):
        site = select_id_site(id)
        return site[0][0]

    #########################
    #### MODIFY USER    #####
    #########################

    def modify_user(self):
        users = sql_select_all_user()
        self.show_user(users)
        Color.main("\n\n Enter an username to modify his informations")
        command = input().strip()  # Input from user to select an action
        pseudo = self.check_pseudo_loop_modify(command)
        user = sql_select_info_user(pseudo)
        print(user[0][1])
        Color.warning(
            "\n ************** If you don't want to change, just press enter to keep the same informations ********** \n")
        fname = self.input_with_prefill("First name of the user : ", user[0][2])
        name = self.input_with_prefill("Last name of the user : ", user[0][1])
        name = name.upper()
        pseudo = self.input_with_prefill("Pseudo of the user  : ", user[0][3])
        if pseudo != user[0][3]: pseudo = self.check_pseudo_loop_modify_other(pseudo, user[0][3])
        passwd = getpass("Enter the password of the user   :    \n")
        passwd = passwd.strip()
        passwd = self.check_password(passwd)
        passwd = self.hash_password(passwd)
        # The city
        city = user[0][5]
        city = self.get_city_name(city)
        city_stored = self.show_city_avaible()
        city = self.input_with_prefill("The city where the user is working :  ", city)
        self.check_city(city, city_stored)
        city = self.get_city_id(city)
        ban = self.input_with_prefill("User banned or not, 0 = No, 1 = Yes:    ", user[0][7]).strip()
        ban = self.check_ban(ban)
        sql_update_user(fname, name, pseudo, passwd, city[0][0], ban, user[0][0])
        Color.success("The informations of the user have been correctly updated ! ")

    def get_city_name(self, city):
        city = sql_get_city_name(city)
        return city

    def ban_user(self):
        users = sql_select_all_user()
        self.show_user(users)
        Color.main("\n\n Enter the pseudo of the user you want to ban")
        pseudo = input().strip()  # Input from user to select an action
        user = self.check_pseudo(pseudo)
        print()
        if pseudo == user[0][3]:
            if user[0][7] == 0:
                print("\n You want to ban this user ? (Y/N ; yes or no) \n")
            else:
                print("\n You want to deban this user ? (Y/N ; yes or no) \n")
            command = input("Your choice   : ").strip()
            command = self.check_y_n(command, user[0][7])
            update_status_ban(user[0][0], command)
            Color.success("The status of the user has been correctly updated ! ")
        else:
            Color.warning("\n !!!!!!! Please select a existing user ")

    def admin_promote(self):
        users = sql_select_all_user()
        self.show_user(users)
        Color.main("\n\n Enter the pseudo of the user of which you want to change the role")
        pseudo = input().strip()  # Input from user to select an action
        user = self.check_pseudo(pseudo)
        print()
        if pseudo == user[0][3]:
            if user[0][6] == 0:
                print("\n You want to promote this user ? (Y/N ; yes or no) \n")
            else:
                print("\n You want to demote this user ? (Y/N ; yes or no) \n")
            command = input("Your choice   : ").strip()
            command = self.check_y_n(command, user[0][7])
            update_status_ban(user[0][0], command)
            Color.success("The status of the user has been correctly updated ! ")
        else:
            Color.warning("\n !!!!!!! Please select a existing user ")

    def check_y_n(self, test, status):
        print(status)
        check = False
        while not check:
            if test == "yes" or test == "no":
                if status == 0:
                    test = 1
                else:
                    test = 0
                check = True
            else:
                Color.warning("\n Please select a correct value\n")
                test = input("Confirm with yes/no):    ").strip()
        return test

    def check_modify_pseudo(self, pseudo, user):
        print(user)
        user = sql_modify_pseudo(user)
        for i in range(len(user)):
            if user[i][0] == pseudo:
                return user[i][0]

    def check_pseudo_loop_modify(self, pseudo):
        check = False
        while not check:
            user = self.check_pseudo(pseudo)
            if user:
                check = True
            else:
                Color.warning("\n !!!!!!! This user doesn't exist !!!!!! ")
                pseudo = input("Pseudo of the user  :   ").strip()
        return pseudo

    def check_pseudo_loop_modify_other(self, pseudo, user):
        check = False
        static_user = user
        while not check:
            user = self.check_modify_pseudo(pseudo, user)
            if user:
                Color.warning("\n !!!!!!! This pseudo is already taken !!!!!! ")
                user = static_user
                pseudo = input("Pseudo of the user  :   ").strip()
            else:
                check = True
        return pseudo

    def input_with_prefill(self, prompt, text,
                           check_pwd=False):  # Create an input with prefill informations, check_pwd required only if you want to fill for a pwd
        def hook():
            readline.insert_text(text)
            readline.redisplay()

        readline.set_pre_input_hook(hook)

        if check_pwd:
            result = getpass(prompt)  # MAKE THE PASSWORD INVISIBLE
        else:
            result = input(prompt).strip()

        readline.set_pre_input_hook()
        return result

    #########################
    ######## DELETE       ###
    #########################

    def delete_user(self):
        users = sql_select_all_user()
        self.show_user(users)
        Color.main("\n\n Enter an username to modify his informations")
        command = input().strip()  # Input from user to select an action
        pseudo = self.check_pseudo_loop_modify(command)
        sql_delete_user(pseudo)
        Color.success("The user have been successfully deleted ! ")

    #########################
    ######## LOGIN PROMPT ###
    #########################

    def __init__(self):
        self.check_login()
        self.main_menu()

    def check_login(self):
        init()
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
                    password = getpass("- Enter the password  :  ")
                    print(len(userInfo))
                    passwd = userInfo[0][4]
                    print(passwd)
                    password_check = self.check_passwd(password, passwd)

                    if password_check:
                        break
                    else:
                        Color.warning("\n !!!!!! Wrong password !!!!!! " + str(count - 1) + " more try")
                        count -= 1

                    if count == 0:
                        quit()
        if userInfo[0][6] == 1:
            Color.warning("\n YOU ARE NOT AN ADMIN !")
            quit()

    def check_pseudo(self, pseudo):  # Check if the pseudo exist inside the file
        userInfo = sql_check_user(pseudo)
        return userInfo

    def check_passwd(self, passwd, hashed):  # Compare the password given in input with the one existing for the user
        check = bcrypt.checkpw(passwd.encode("utf-8"), hashed.encode("utf-8"))
        return check

    #########################
    ######## MAIN MENU ######
    #########################

    def main_gestion_user(self):
        Color.main("\n\n ********Welcome to the user gestion program !*********** ")
        while True:  # While loop to keep the user in the program
            self.show_menu_admin()
            command = input().strip()  # Input from user to select an action
            if command == "1":
                self.add_user()
            elif command == "2":
                self.modify_user()
            elif command == "3":
                self.main_list_user()
            elif command == "4":
                self.delete_user()
            elif command == "5":
                self.ban_user()
            elif command == "6":
                self.admin_promote()
            elif command == "0":
                Color.main("\n ********** Good bye !  ************")
                deinit()
                break
            else:
                print("Choose a valid number !")

    def main_menu(self):
        # self.check_login()
        Color.main("\n\n ********Welcome in the main program !*********** ")
        while True:  # While loop to keep the user in the program
            self.show_menu_user()  # Print the menu
            command = input().strip()  # Input from user to select an action
            if command == "1":
                print("hello")
            elif command == "2":
                self.main_gestion_user()
            elif command == "0":
                Color.main("\n ********** Good bye !  ************")
                deinit()
                break
            else:
                print("Choose a valid number !")

    @staticmethod
    def show_menu_user():
        print("\n")
        Color.prompt("Please enter a number to select an action : \n")
        Color.prompt("1 : Launch server")
        Color.prompt("2 : Super admin menu")
        Color.prompt("0 : Quit the program")

    @staticmethod
    def show_menu_admin():
        print("\n")
        Color.prompt("Please enter a number to select an action : \n")
        Color.prompt("1 : Add user")
        Color.prompt("2 : Modify user")
        Color.prompt("3 : List user")
        Color.prompt("4 : Delete user")
        Color.prompt("5 : Change ban user")
        Color.prompt("6 : Change the role of the usr")
        Color.prompt("0 : Return to the main page")



start = Main()
