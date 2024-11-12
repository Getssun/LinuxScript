from auth import connexion

def command_user(client_ssh, username, password, sudo_password):
    command = (f"sudo -S useradd -m {username} -p {password}")

    stdin, stdout, stderr = client_ssh.exec_command(command ,get_pty=True)
    stdin.write(sudo_password + '\n')
    stdin.flush()
    stdout = stdout.readlines()
    errors = stderr.read().decode()
    return stdout, errors

# Crée un utilisateur
def create_user(host, user, mdp, sudo_password, username, password):

    client_ssh = connexion(host, user, mdp)
    stdout, errors = command_user(client_ssh, username, password, sudo_password) 
    if errors:
        print(f"Erreur : {errors}")
    else:
        print(f"Utilisateur {username} créé avec succès.")
    client_ssh.close()