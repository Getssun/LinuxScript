import paramiko

def connexion(host, utilisateur, mdp):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=utilisateur, password=mdp)
    return client



# execute la commande d'installation du service
def sudo_command_service(client_ssh, service_name, sudo_password):
    command = f"echo {sudo_password} | sudo -S apt install -y {service_name}"
    stdin, stdout, stderr = client_ssh.exec_command(command)
    stdout = stdout.readlines()
    errors = stderr.read().decode()

    if errors:
        print(f"Erreur lors de l'installation de {service_name} : {errors}")
    else:
        print(f"{service_name} installé avec succès.")
    return stdout



def sudo_command_user(client_ssh, username, password, sudo_password):
    command = (f"sudo -S useradd -m {username} -p {password}")

    stdin, stdout, stderr = client_ssh.exec_command(command ,get_pty=True)
    stdin.write(sudo_password + '\n')
    stdin.flush()
    stdout = stdout.readlines()
    errors = stderr.read().decode()
    return stdout, errors