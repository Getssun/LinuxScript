import os

def getListofFilesLocal(localFilePath):
    try: 
        print(f"Liste des fichiers : {os.listdir(localFilePath)}")
    except Exception as err:
        print(f"Erreur inconnue lors de la récupération des fichiers : {err}")



def getListofFilesRemote(client_ssh, remoteFilePath):
    sftp_client = client_ssh.open_sftp()  
    try: 
        print(f"Liste des fichiers distants : {sftp_client.listdir(remoteFilePath)}")
    except Exception as err:
        print(f"Erreur lors de la récupération de la liste des fichiers distants : {err}")



def downloadFile(client_ssh, remote_path, local_path, file):
    sftp_client = client_ssh.open_sftp()
    try:
        local_file_path = os.path.join(local_path, file)
        remote_file_path = os.path.join(remote_path, file)
        sftp_client.get(remote_file_path, local_file_path)
    except Exception as err:
        print(f"Erreur lors du téléchargement du fichier : {err}")

def downloadFileAll(client_ssh, remote_path, local_path):
    sftp_client = client_ssh.open_sftp()
    try:
        for filename in sftp_client.listdir(remote_path):
            remote_file_path = os.path.join(remote_path, filename)
            local_file_path = os.path.join(local_path, filename)
            sftp_client.get(remote_file_path, local_file_path)
            print(f"Fichiers {filename} avec succès dans {local_path}") 
    except Exception as err:
        print(f"Erreur lors du téléchargement des fichiers : {err}")



def uploadFile(client_ssh, remoteFilePath, localFilePath, document):
    sftp_client = client_ssh.open_sftp()
    try:
        local_file_path = os.path.join(localFilePath, document)
        remote_file_path = os.path.join(remoteFilePath, document)
        sftp_client.put(local_file_path, remote_file_path)
        print(f"Fichier {document} avec succès dans {remoteFilePath}")
    except Exception as err:
        print(f"Erreur lors de l'envoi du fichier : {err}")

def uploadFilesAll(client_ssh, remote_path, local_path):
    sftp_client = client_ssh.open_sftp()
    try:
        for filename in os.listdir(local_path):
            local_file_path = os.path.join(local_path, filename)
            remote_file_path = os.path.join(remote_path, filename)
            sftp_client.put(local_file_path, remote_file_path)
            print(f"Fichiers {filename} avec succès dans {remote_path}") 
    except Exception as err:
        print(f"Erreur lors de l'envoi des fichiers : {err}")

