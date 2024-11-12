import getpass
import sys
from services import service_setup_nginx
from services import service_setup_ldap
from services import service_setup_ftp
from users import create_user


host = '192.168.50.135'
user = 'deb'
mdp = 'a'
sudo_password = getpass.getpass('Entrez le mot de passe sudo : ')

create_user(host, user, mdp, sudo_password, 'test8', 'test')