from auth import connexion
from auth import sudo_command_service


# installe le service Apache
def service_setup_nginx(host, user, mdp, sudo_password):
    try:
        client_ssh = connexion(host, user, mdp)
        sudo_command_service(client_ssh, "nginx", sudo_password)
    except Exception as e:
        print(f"Erreur lors de l'installation de Nginx : {e}")
    finally:
        client_ssh.close()


# installe le service LDAP
def service_setup_ldap(host, user, mdp, sudo_password):
    try:
        client_ssh = connexion(host, user, mdp)
        sudo_command_service(client_ssh, "slapd", sudo_password)
    except Exception as e:
        print(f"Erreur lors de l'installation de LDAP : {e}")
    finally:
        client_ssh.close()


# installe le service FTP
def service_setup_ftp(host, user, mdp, sudo_password):
    try:
        client_ssh = connexion(host, user, mdp)
        sudo_command_service(client_ssh, "vsftpd", sudo_password)
    except Exception as e:
        print(f"Erreur lors de l'installation de FTP : {e}")
    finally:
        client_ssh.close()