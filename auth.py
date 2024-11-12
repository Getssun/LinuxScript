import paramiko

def connexion(host, utilisateur, mdp):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=utilisateur, password=mdp)
    return client
