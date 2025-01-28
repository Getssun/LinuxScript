import paramiko

def connexion(host, user, pwd):
    try:
        # Création de l'objet SSHClient
        client_ssh = paramiko.SSHClient()
        client_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # Tentative de connexion
        client_ssh.connect(hostname=host, username=user, password=pwd)
        
        print(f"Connexion réussie à {host}")
        return client_ssh
    except paramiko.AuthenticationException:
        print("Échec de l'authentification. Vérifiez votre utilisateur/mot de passe.")
        return None
    except paramiko.SSHException as ssh_error:
        print(f"Erreur SSH : {ssh_error}")
        return None
    except Exception as e:
        print(f"Erreur générale : {e}")
        return None
