from auth import connexion

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