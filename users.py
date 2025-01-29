from auth import connexion

# Crée un utilisateur
def create_users(host, user, mdp, sudo_password,create_username, create_password):
    try:
        client_ssh = connexion(host, user, mdp)
        command = (f"sudo -S useradd -m {create_username} -p {create_password}")
        stdin, stdout, stderr = client_ssh.exec_command(command ,get_pty=True)
        stdin.write(sudo_password + '\n')
        stdin.flush()
        stdout = stdout.readlines()
        errors = stderr.read().decode()
        print (f"L'utilisateur a été créé {create_username}")
        return stdout, errors
    
    except Exception as e:
        print(f"Erreur lors de la création de l'utilisateur : {e}")

# Supprime un utilisateur
def delete_users(client_ssh, username, sudo_password):
    command = (f"sudo -S userdel -r {username}")

    stdin, stdout, stderr = client_ssh.exec_command(command ,get_pty=True)
    stdin.write(sudo_password + '\n')
    stdin.flush()
    stdout = stdout.readlines()
    errors = stderr.read().decode()
    print (f"L'utilisateur a été supprimé {username}")
    return stdout, errors

# Met à jour un utilisateur
def update_users(client_ssh, username, sudo_password):
    command = (f"sudo -S usermod -l {username}")

    stdin, stdout, stderr = client_ssh.exec_command(command ,get_pty=True)
    stdin.write(sudo_password + '\n')
    stdin.flush()
    stdout = stdout.readlines()
    errors = stderr.read().decode()
    print (f"L'utilisateur a été mis à jour {username}")
    return stdout, errors