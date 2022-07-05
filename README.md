# Descriptions des fichiers :

## ARCHIVE : 

Script pour créer une archive journalière sous format ZIP

## BRUTE

Script pour créer une attaque brute force sur un serveur ftp, fichier user et pass pour une banque de données utilisé lors de
l'execution du script. 

## CLIENT :

mainClient.py : Script pour l'interface de gestion du compte (voir ses informations et changer son mot de passe)
ftpClient : Client ftp pour communiquer avec le serveur FTP

## Client_Storage : 

Dossier contenant les fichiers à envoyée au serveur (juste pour la démo)

## LOG 

Dossier STORAGE : Contient les logs journaliers du serveur avec les anciens au format zip. 
Le fichier ftpserver_log_04_07_2022.log : Contient les logs des actions qui ont été executé pour la démo.

createLog.py : Script servant a créer le fichier de log journalier et à "zipper" l'ancien 

## SCAN

portScan.py : Scan de port sur le serveur FTP.

## SERVEUR :

mainServeur.py : Interface admin pour gèrer les clients utilisant le serveur FTP
ftpServeur : Serveur FTP

## Serveur_Storage :

Contient les fichiers du serveur

## SQL

Contient les scripts SQL et la base de données SQLite utilisées.