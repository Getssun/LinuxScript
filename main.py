# Importez vos modules
import getpass
from services import *
from users import *
from reseau import *
from menu import Menu, ClientFromSSH
from auth import connexion

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
                if user_choice == "1":
                    print("Créer un utilisateur")
                    create_user = input("Nom d'utilisateur : ")
                    create_password = getpass.getpass("Mot de passe : ")
                    sudo_password = getpass.getpass("Mot de passe sudo : ")
                    create_users(host, user, pwd, sudo_password, create_user, create_password)
                elif user_choice == "2":
                    print("Supprimer un utilisateur")
                    delete_user = input("Nom d'utilisateur : ")
                    sudo_password = getpass.getpass("Mot de passe sudo : ")
                    delete_users(client_ssh, delete_user, sudo_password)
                elif user_choice == "3":
                    print("Mettre à jour un utilisateur")
                elif user_choice == "4":
                    break
                else:
                    print("Choix invalide dans Users Menu.")


        elif choice == "2":  # Services Menu
            while True:
                service_choice = menu.services_menu()
                if service_choice == "1":
                    print("Installer un service ")
                elif service_choice == "4":
                    break
                else:
                    print("Choix invalide dans Services Menu.")


        elif choice == "3":  # Network Menu
            while True:
                network_choice = menu.network_menu()
                if network_choice == "1":
                    print("Changer DNS (placeholder)")
                elif network_choice == "2":
                    print("Changer Gateway (placeholder)")
                elif network_choice == "3":
                    print("Changer IP (placeholder)")
                elif network_choice == "4":
                    break
                else:
                    print("Choix invalide dans Network Menu.")
        elif choice == "4":  # Exit
            print("Au revoir!")
            break
        else:
            print("Choix invalide dans le menu principal.")

if __name__ == "__main__":
    main()

