
#Importation des librairies
import socket
from datetime import datetime
import colorama

colorama.init()
print(colorama.Fore.RED + 'some red text' + colorama.Style.RESET_ALL)

#Pour faire jolie
print """
 .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .-----------------.
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |   ______     | || |  ____  ____  | || |    _______   | || |     ______   | || |      __      | || | ____  _____  | |
| |  |_   __ \   | || | |_  _||_  _| | || |   /  ___  |  | || |   .' ___  |  | || |     /  \     | || ||_   \|_   _| | |
| |    | |__) |  | || |   \ \  / /   | || |  |  (__ \_|  | || |  / .'   \_|  | || |    / /\ \    | || |  |   \ | |   | |
| |    |  ___/   | || |    \ \/ /    | || |   '.___`-.   | || |  | |         | || |   / ____ \   | || |  | |\ \| |   | |
| |   _| |_      | || |    _|  |_    | || |  |`\____) |  | || |  \ `.___.'\  | || | _/ /    \ \_ | || | _| |_\   |_  | |
| |  |_____|     | || |   |______|   | || |  |_______.'  | || |   `._____.'  | || ||____|  |____|| || ||_____|\____| | |
| |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
"""

#Demande a l'utilisateur de rentrer different parametres
host = raw_input("Enter host to scan: ") #Adresse destination
beginto = raw_input("Enter beginning port: ") #Debut de la pkage de port a scanner
stopto = raw_input("Enter stoping port: ") #Fin de la pkage de port a scanner

#Enregistrement de l'heure du debut du scan pour le calcul du temps d'execution du scan
t1 = datetime.now()

#Pour chaque ports dans la plage definie, on vois si il est ouvert grace au socket
for port in range(int(beginto),int(stopto)):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((host, port))
        if result == 0:
            print(colorama.Fore.GREEN + "Port {}:      Open".format(port) + colorama.Style.RESET_ALL)

        else:
            print(colorama.Fore.RED + "Port {}:      Close".format(port) + colorama.Style.RESET_ALL)
        sock.close()

#Pour chaque ports dans la plage definie on vois si il est ouvert grace au socket
t2 = datetime.now()

#Calcul du temps d'execution du scan
total =  t2 - t1

#Affichage du temps d'execution du scan
print 'Scanning Completed in: ', total