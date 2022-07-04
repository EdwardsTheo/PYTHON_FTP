import os
import zipfile
from datetime import date


def main_archive():  # Function to create the archive of the server
    path = 'C:\\Users\\bapti\\Desktop\\pyFTP\\Serveur_Storage\\'  # Path of all the directory
    today = date.today()    #
    d = today.strftime("%d_%m_%Y")
    archive = "archive_" + d + ".zip"  # Name of the archive

    check = 'C:\\Users\\bapti\\Desktop\\pyFTP\\ARCHIVE\\' + archive
    isDir = os.path.isfile(check)

    if isDir:
        print("The repository already exist")
        exit()
    else:
        with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipdir('C:\\Users\\bapti\\Desktop\\pyFTP\\Serveur_Storage\\', zipf)


def zipdir(path, ziph):  # Create the zip with all the directory and files inside it
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file),
                       os.path.relpath(os.path.join(root, file),
                                       os.path.join(path, '..')))