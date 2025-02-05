from auth import connexion
from main import main

#Met en DHCP la carte réseau de la machine

def dhcp(host, user, pwd, sudo_password):
    try:
        carte_reseau = input('Entrez le nom de la carte réseau : ')
        client_ssh = connexion(host, user, pwd)
       
        command_delete_ip = f"echo {sudo_password} | sudo -S nmcli connection delete {carte_reseau}"
        stdin, stdout, stderr = client_ssh.exec_command(command_delete_ip)

        command_ip = f"echo {sudo_password} | sudo -S nmcli connection add type ethernet con-name {carte_reseau} ifname {carte_reseau} ipv4.method auto"
        stdin, stdout, stderr = client_ssh.exec_command(command_ip)

        command_start = f"echo {sudo_password} | sudo -S nmcli connection up {carte_reseau}"
        stdin, stdout, stderr = client_ssh.exec_command(command_start)

        main()
        stdout = stdout.readlines()
        errors = stderr.read().decode()
        if errors:
            print(f"Erreur lors du passage en DHCP : {errors}")
        else:
            print(f"Passage en DHCP effectué avec succès.")
    except Exception as e:
        print(f"Erreur lors du passage en DHCP : {e}")



#Change l'adresse IP de la machine
def change_ip(host, user, pwd, sudo_password):
    try:
        carte_reseau = input('Entrez le nom de la carte réseau : ')
        new_ip = input('Entrez la nouvelle adresse IP : ')
        new_netmask = input('Entrez le nouveau masque de sous-réseau en CIDR : /')
        new_gateway = input('Entrez la nouvelle passerelle : ')
        client_ssh = connexion(host, user, pwd)

        command_tools = f"echo {sudo_password} | sudo -S apt install network-manager"
        stdin, stdout, stderr = client_ssh.exec_command(command_tools)

        command_delete_ip = f"echo {sudo_password} | sudo -S nmcli connection delete {carte_reseau}"
        stdin, stdout, stderr = client_ssh.exec_command(command_delete_ip)

        command_ip = f"echo {sudo_password} | sudo -S nmcli connection add type ethernet con-name {carte_reseau} ifname {carte_reseau} ip4 {new_ip}/{new_netmask} gw4 {new_gateway}"

        command_start = f"echo {sudo_password} | sudo -S nmcli connection up {carte_reseau}"
        stdin, stdout, stderr = client_ssh.exec_command(command_start)

        stdin, stdout, stderr = client_ssh.exec_command(command_ip)
        #stdin, stdout, stderr = client_ssh.exec_command(command_gateway)
        main()

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
