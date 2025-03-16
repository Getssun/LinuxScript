from auth import connexion

#Change l'adresse IP de la machine
def change_ip(host, user, pwd, sudo_password):
    try:
        new_ip = input('Entrez la nouvelle adresse IP 5 : ')
        new_netmask = input('Entrez le nouveau masque de sous-réseau : ')
        new_gateway = input('Entrez la nouvelle passerelle : ')
        client_ssh = connexion(host, user, pwd)
        command = f"echo {sudo_password} | echo -e \"auto eth0\niface eth0 inet static\n    address {new_ip}\n    netmask {new_netmask}\n    gateway {new_gateway}\" | sudo -S tee /etc/network/interfaces > /dev/null && sudo -S systemctl restart networking"
        stdin, stdout, stderr = client_ssh.exec_command(command)


        stdout = stdout.readlines()
        errors = stderr.read().decode()
        if errors:
            print(f"Erreur lors du changement d'IP : {errors}")
        else:
            print(f"IP modifiée avec succès.")
    except Exception as e:
        print(f"Erreur lors du changement d'IP : {e}")

#Change le DNS de la machine
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

#Change la passerelle de la machine

def change_gateway(host, user, pwd, sudo_password):
    try:
        new_gateway = input('Entrez la nouvelle passerelle : ')
        client_ssh = connexion(host, user, pwd)
        command = f"echo {sudo_password} | sudo -S ip route add default via {new_gateway}"
        stdin, stdout, stderr = client_ssh.exec_command(command)

        stdout = stdout.readlines()
        errors = stderr.read().decode()
        if errors:
            print(f"Erreur lors du changement de la passerelle : {errors}")
        else:
            print(f"Passerelle modifiée avec succès.")
    except Exception as e:
        print(f"Erreur lors du changement de la passerelle : {e}")
