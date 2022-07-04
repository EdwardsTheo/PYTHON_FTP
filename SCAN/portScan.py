import logging
import pyfiglet
import sys
import socket
from datetime import datetime, date

ascii_banner = pyfiglet.figlet_format("port SCAN by Baptiste and Loeiz-Bi")
print(ascii_banner)

today = date.today()
d = today.strftime("%d_%m_%Y")
logfile = "C:\\Users\\bapti\\Desktop\\pyFTP\\LOG\\STORAGE\\" + "portscan_log_" + d + ".log"
logging.basicConfig(filename=logfile,
                    format='%(asctime)s %(message)s',
                    filemode='a+')
logger = logging.getLogger()

# Defining a target
target = "127.0.0.1"
# Add Banner
print("-" * 50)
print("Scanning Target: " + target)
print("Scanning started at:" + str(datetime.now()))
print("-" * 50)

try:

    # will scan ports between 1 to 65,535
    for port in range(1, 65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        # returns an error indicator
        result = s.connect_ex((target, port))
        if result == 0:
            logger.setLevel(logging.INFO)
            logger.info("Port {} is open".format(port))
        s.close()

except KeyboardInterrupt:
    print("\n Exiting Program !!!!")
    sys.exit()
except socket.gaierror:
    print("\n Hostname Could Not Be Resolved !!!!")
    sys.exit()
except socket.error:
    print("\ Server not responding !!!!")
    sys.exit()
