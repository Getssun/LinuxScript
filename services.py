from auth import connexion

# liste les services en filtrant par grep
def list_services_grep(client_ssh, sudo_password, grep_service):
    command = f"systemctl list-units --type=service --all | grep {grep_service}"
    stdin, stdout, stderr = client_ssh.exec_command(command)
    stdin.write(f"{sudo_password}\n")
    stdin.flush()

    stdout = stdout.readlines()
    errors = stderr.read().decode()

    if errors:
        print("Erreur lors de la récupération de la liste des services.")
    else:
        print("Liste des services :")
        for service in stdout:
            print(service)
    return stdout

# liste les services
def list_services(client_ssh, sudo_password):
    command = "systemctl list-units --type=service"
    stdin, stdout, stderr = client_ssh.exec_command(command)
    stdin.write(f"{sudo_password}\n")
    stdin.flush()

    stdout = stdout.readlines()
    errors = stderr.read().decode()

    if errors:
        print("Erreur lors de la récupération de la liste des services.")
    else:
        print("Liste des services :")
        for service in stdout:
            print(service)
    return stdout


# installe le service
def install_service(client_ssh, service_name, sudo_password):
    command = f"sudo -S apt install {service_name} -y"
    stdin, stdout, stderr = client_ssh.exec_command(command)
    stdin.write(f"{sudo_password}\n")
    stdin.flush()

    stdout = stdout.readlines()
    errors = stderr.read().decode()

    if errors:
        print(f"Erreur lors de l'installation de {service_name}")
    else:
        print(f"{service_name} installé avec succès.")
    return stdout

# lance le service
def start_service(client_ssh, service_name, sudo_password):
    command = f"sudo -S systemctl start {service_name}"
    stdin, stdout, stderr = client_ssh.exec_command(command)
    stdin.write(f"{sudo_password}\n")
    stdin.flush()

    stdout = stdout.readlines()
    errors = stderr.read().decode()

    if errors:
        print(f"Erreur lors du démarrage de {service_name}")
    else:
        print(f"{service_name} démarré avec succès.")


# arrête le service
def stop_service(client_ssh, service_name, sudo_password):
    command = f"sudo -S systemctl stop {service_name}"
    stdin, stdout, stderr = client_ssh.exec_command(command)
    stdin.write(f"{sudo_password}\n")
    stdin.flush()

    stdout = stdout.readlines()
    errors = stderr.read().decode()

    if errors:
        print(f"Erreur lors de l'arrêt de {service_name}")
    else:
        print(f"{service_name} arrêté avec succès.")
    return stdout

# active le service
def enable_service(client_ssh, service_name, sudo_password):
    command = f"sudo -S systemctl enable {service_name}"
    stdin, stdout, stderr = client_ssh.exec_command(command)
    stdin.write(f"{sudo_password}\n")
    stdin.flush()

    stdout = stdout.readlines()
    errors = stderr.read().decode()

    if errors:
        print(f"Erreur lors de l'activation de {service_name}")
    else:
        print(f"{service_name} activé avec succès.")
    return stdout

# désactive le service
def disable_service(client_ssh, service_name, sudo_password):
    command = f"sudo -S systemctl disable {service_name}"
    stdin, stdout, stderr = client_ssh.exec_command(command)
    stdin.write(f"{sudo_password}\n")
    stdin.flush()

    stdout = stdout.readlines()
    errors = stderr.read().decode()

    if errors:
        print(f"Erreur lors de la désactivation de {service_name}")
    else:
        print(f"{service_name} désactivé avec succès.")
    return stdout


# redémarre le service
def restart_service(client_ssh, service_name, sudo_password):
    command = f"sudo -S systemctl restart {service_name}"
    stdin, stdout, stderr = client_ssh.exec_command(command)
    stdin.write(f"{sudo_password}\n")
    stdin.flush()

    stdout = stdout.readlines()
    errors = stderr.read().decode()

    if errors:
        print(f"Erreur lors du redémarrage de {service_name}")
    else:
        print(f"{service_name} redémarré avec succès.")
    return stdout
