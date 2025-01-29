

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
        print("1. Users Menu")
        print("2. Services Menu")
        print("3. Network Menu")
        print("4. Exit")
        choice = input("Enter your choice: ")
        return choice

    def users_menu(self):
        print("Users Menu")
        print("1. Create User")
        print("2. Delete User")
        print("3. Update User")
        print("4. Back")
        choice = input("Enter your choice: ")
        return choice

    def services_menu(self):
        print("Services Menu")
        print("1. Install Service")
        print("2. Stop Service")
        print("3. Restart Service")
        print("4. Back")
        choice = input("Enter your choice: ")
        return choice

    def network_menu(self):
        print("Network Menu")
        print("1. Change DNS")
        print("2. Change Gateway")
        print("3. Change IP")
        print("4. Back")
        choice = input("Enter your choice: ")
        return choice

