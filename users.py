from auth import connexion
from auth import sudo_command_user


# Crée un utilisateur
def create_user(host, user, mdp, sudo_password, username, password):

    client_ssh = connexion(host, user, mdp)
    stdout, errors = sudo_command_user(client_ssh, username, password, sudo_password) 
    if errors:
        print(f"Erreur : {errors}")
    else:
        print(f"Utilisateur {username} créé avec succès.")
    client_ssh.close()