# Importez vos modules
import getpass
from services import *
from users import *
from reseau import *
from menu import Menu, ClientFromSSH
from auth import connexion
from fichier import *

def main():
    # Demander les informations de connexion
    user = input("Nom d'utilisateur : ")
    pwd = getpass.getpass("Mot de passe : ")
    host = input("Adresse IP : ")
    
    # Connexion SSH
    client_ssh = connexion(host, user, pwd)
    
    if client_ssh is None:  # Si la connexion échoue
        print("Impossible de se connecter. Veuillez réessayer.")
        return  # Fin du programme principal
    
    # Si la connexion réussit, passez à l'exécution des menus
    print("Connexion réussie. Affichage du menu principal.")
    menu = Menu(client_ssh)

    while True:
        # Afficher le menu principal
        choice = menu.main_menu()

        if choice == "1":  # Users Menu
            while True:
                user_choice = menu.users_menu()
                # Liste les utilisateurs
                if user_choice == "1":
                    list_users(client_ssh)
                # Crée un utilisateur
                elif user_choice == "2":
                    create_user = input("Nom d'utilisateur : ")
                    create_password = getpass.getpass("Mot de passe : ")
                    sudo_password = getpass.getpass("Mot de passe sudo : ")
                    create_users(host, user, pwd, sudo_password, create_user, create_password)
                # Supprime un utilisateur
                elif user_choice == "3":
                    delete_user = input("Nom d'utilisateur : ")
                    sudo_password = getpass.getpass("Mot de passe sudo : ")
                    delete_users(client_ssh, delete_user, sudo_password)
                # Met à jour un utilisateur
                elif user_choice == "4":
                    update_user = input("Nom d'utilisateur : ")
                    sudo_password = getpass.getpass("Mot de passe sudo : ")
                    update_users(client_ssh, update_user, sudo_password)
                # Retour
                elif user_choice == "5":
                    break
                else:
                    print("Choix invalide dans Users Menu.")


        elif choice == "2":  # Services Menu
            while True:
                service_choice = menu.services_menu()
                # Liste les services
                if service_choice == "1":
                    sudo_password = getpass.getpass("Mot de passe sudo : ")
                    grep_option = input("Voulez-vous filtrer les services actifs ? (o/n par défaut n) : ")
                    if grep_option == "o":
                        grep_service = input("Nom du service : ")
                        list_services_grep(client_ssh, sudo_password, grep_service)
                    else:
                        list_services(client_ssh, sudo_password)
                # Installe le service
                elif service_choice == "2":
                    sudo_password = getpass.getpass("Mot de passe sudo : ")
                    service_name = input("Nom du service : ")
                    install_service(client_ssh, service_name, sudo_password)
                # Lance le service
                elif service_choice == "3":
                    sudo_password = getpass.getpass("Mot de passe sudo : ")
                    service_name = input("Nom du service : ")
                    start_service(client_ssh, service_name, sudo_password)
                # Arrêter un service
                elif service_choice == "4":
                    sudo_password = getpass.getpass("Mot de passe sudo : ")
                    service_name = input("Nom du service : ")
                    stop_service(client_ssh, service_name, sudo_password)
                # Redemarrer un service
                elif service_choice == "5":
                    sudo_password = getpass.getpass("Mot de passe sudo : ")
                    service_name = input("Nom du service : ")
                    restart_service(client_ssh, service_name, sudo_password)
                # Retour
                elif service_choice == "6":
                    break
                else:
                    print("Choix invalide dans Services Menu.")


        elif choice == "3":  # Network Menu
            while True:
                network_choice = menu.network_menu()
                if network_choice == "1":
                    print("Changer IP (placeholder)")
                    sudo_password = getpass.getpass("Mot de passe sudo : ")
                    change_ip(host, user, pwd, sudo_password)
                elif network_choice == "2":
                    print("Changer DNS (placeholder)")
                    sudo_password = getpass.getpass("Mot de passe sudo : ")
                    change_dns(host, user, pwd, sudo_password)
                elif network_choice == "3":
                    print("Changer Gateway (placeholder)")
                elif network_choice == "4":
                    break
                else:
                    print("Choix invalide dans Network Menu.")

        
        elif choice == "4":  # Files Menu
            while True:
                files_choice = menu.files_menu()
                # Liste les fichiers locaux
                if files_choice == "1":
                    local_path = input("Chemin du répertoire : ")
                    getListofFilesLocal(local_path)

                # Liste les fichiers distants
                elif files_choice == "2":
                    remote_path = input("Chemin du répertoire distant : ")
                    getListofFilesRemote(client_ssh, remote_path)

                # Télécharger un fichier
                elif files_choice == "3":
                    remote_path = input("Chemin absolu du fichier distant : ")  # Ex: /home/deb/test/
                    local_path = input("Chemin absolu du fichier local : ")   # Ex: C:\temp
                    
                    print ("Voulez-vous télécharger un fichier ou dossier ?")
                    print ("1. Un seul fichier")
                    print ("2. Tous les fichiers d'un dossier")
                    files_choice = input("Entrez votre choix : ")

                    if files_choice == "1":
                        file = input("Nom du fichier : ")
                        downloadFile(client_ssh, remote_path, local_path, file)
                    elif files_choice == "2":
                        downloadFileAll(client_ssh, remote_path, local_path)
                                 
                elif files_choice == "4":
                    local_path = input("Chemin du fichier local : ")
                    remote_path = input("Chemin du fichier distant : ")
                    print ("Voulez-vous envoyer un fichier ou dossier ?")
                    print ("1. Un seul fichier")
                    print ("2. Tous les fichiers d'un dossier")
                    files_choice = input("Entrez votre choix : ")
                    if files_choice == "1":
                        document = input("Nom du fichier : ")
                        uploadFile(client_ssh, remote_path, local_path, document)
                    elif files_choice == "2":
                        uploadFilesAll(client_ssh, remote_path, local_path)

                elif files_choice == "5":
                    break


        elif choice == "5":  # Exit
            print("Au revoir!")
            break
        else:
            print("Choix invalide dans le menu principal.")

if __name__ == "__main__":
    main()
