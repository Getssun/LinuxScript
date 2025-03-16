

class ClientFromSSH :
    def __init__(self, ip, user, pwd):
        self.ip = ip
        self.user = user
        self.pwd = pwd

    def connect(self):
        print("Connecting to server with ip: ", self.ip, " username: ", self.username, " password: ", self.password)

    def execute(self, command):
        print("Executing command: ", command)

    def close(self):
        print("Closing connection to server")

class Menu :
    def __init__(self, client):
        self.client = client

    def main_menu(self):
        print("Main Menu")
        print("1. Utilisateurs")
        print("2. Services")
        print("3. Réseau")
        print("4. Fichiers")
        print("5. Quitter")
        choice = input("Entrez votre choix: ")
        return choice

    def users_menu(self):
        print("Utilisateurs Menu")
        print("1. Lister les utilisateurs")
        print("2. Ajouter un utilisateur")
        print("3. Supprimer un utilisateur")
        print("4. Mettre à jour un utilisateur")
        print("5. Retour")
        choice = input("Entrez votre choix: ")
        return choice

    def services_menu(self):
        print("Services Menu")
        print("1. Lister les services")
        print("2. Installer un service")
        print("3. Démarrer un service")
        print("4. Arrêter un service")
        print("5. Redémarrer un service")
        print("6. Retour")
        choice = input("Entrez votre choix: ")
        return choice

    def network_menu(self):
        print("Réseau Menu")
        print("1. Changement d'adresse IP")
        print("2. Changement DNS") 
        print("3. Changement de passerelle")
        print("4. Retour")
        choice = input("Entrez votre choix: ")
        return choice
    
    def files_menu(self):
        print("Fichiers Menu")
        print("1. Lister les fichiers")
        print("2. Lister les fichiers distants")
        print("3. Telecharger un fichier")
        print("4. Envoyer un fichier")
        print("5. Retour")
        choice = input("Entrez votre choix: ")
        return choice
