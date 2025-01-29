from auth import connexion

#Change l'adresse IP de la machine
def change_ip(host, user, pwd, sudo_password):
    try:
        new_ip = input('Entrez la nouvelle adresse IP : ')
        new_netmask = input('Entrez le nouveau masque de sous-réseau : ')
        client_ssh = connexion(host, user, pwd)
        command = f"echo {sudo_password} | sudo -S ifconfig eth0 {new_ip} netmask {new_netmask}"
        stdin, stdout, stderr = client_ssh.exec_command(command)

        stdout = stdout.readlines()
        errors = stderr.read().decode()
        if errors:
            print(f"Erreur lors du changement d'IP : {errors}")
        else:
            print(f"IP modifiée avec succès.")
    except Exception as e:
        print(f"Erreur lors du changement d'IP : {e}")

#Change la passerelle de la machine
def change_dns(host, user, pwd, sudo_password):
    try:
        nameserver = input('Entrez le nouveau serveur DNS : ')
        client_ssh = connexion(host, user, pwd)
        command = f"echo {sudo_password} | sudo -S echo {nameserver} > /etc/resolv.conf"
        stdin, stdout, stderr = client_ssh.exec_command(command)

        stdout = stdout.readlines()
        errors = stderr.read().decode()
        if errors:
            print(f"Erreur lors du changement de DNS : {errors}")
        else:
            print(f"DNS modifié avec succès.")
    except Exception as e:
        print(f"Erreur lors du changement de DNS : {e}")

