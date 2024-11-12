from auth import connexion

# execute la commande d'installation du service
def service_installation(client_ssh, service_name, sudo_password):
    command = f"echo {sudo_password} | sudo -S apt update && echo {sudo_password} | sudo -S apt install -y {service_name}"
    stdin, stdout, stderr = client_ssh.exec_command(command)
    stdout = stdout.readlines()
    errors = stderr.read().decode()

    if errors:
        print(f"Erreur lors de l'installation de {service_name} : {errors}")
    else:
        print(f"{service_name} installé avec succès.")
    return stdout


# installe le service Apache
def service_setup_nginx(host, user, mdp, sudo_password):
    try:
        client_ssh = connexion(host, user, mdp)
        service_installation(client_ssh, "nginx", sudo_password)
    except Exception as e:
        print(f"Erreur lors de l'installation de Nginx : {e}")
    finally:
        client_ssh.close()


# installe le service LDAP
def service_setup_ldap(host, user, mdp, sudo_password):
    try:
        client_ssh = connexion(host, user, mdp)
        service_installation(client_ssh, "slapd", sudo_password)
    except Exception as e:
        print(f"Erreur lors de l'installation de LDAP : {e}")
    finally:
        client_ssh.close()


# installe le service FTP
def service_setup_ftp(host, user, mdp, sudo_password):
    try:
        client_ssh = connexion(host, user, mdp)
        service_installation(client_ssh, "vsftpd", sudo_password)
    except Exception as e:
        print(f"Erreur lors de l'installation de FTP : {e}")
    finally:
        client_ssh.close()