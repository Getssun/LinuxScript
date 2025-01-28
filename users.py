from auth import connexion

def sudo_command_useradd(client_ssh, username, password, sudo_password):
    command = (f"sudo -S useradd -m {username} -p {password}")

    stdin, stdout, stderr = client_ssh.exec_command(command ,get_pty=True)
    stdin.write(sudo_password + '\n')
    stdin.flush()
    stdout = stdout.readlines()
    errors = stderr.read().decode()
    return stdout, errors

# Crée un utilisateur
def create_users(host, user, pwd, sudo_password, create_user, create_password):

    client_ssh = connexion(host, user, pwd)
    stdout, errors = sudo_command_useradd(client_ssh, create_user, create_password, sudo_password) 
    if errors:
        print(f"Erreur : {errors}")
    else:
        print(f"Utilisateur {create_user} créé avec succès.")
    client_ssh.close()

def delete_users(client_ssh, username, sudo_password):
    command = (f"sudo -S userdel -r {username}")

    stdin, stdout, stderr = client_ssh.exec_command(command ,get_pty=True)
    stdin.write(sudo_password + '\n')
    stdin.flush()
    stdout = stdout.readlines()
    errors = stderr.read().decode()
    return stdout, errors