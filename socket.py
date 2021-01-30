from socket import socket
*** # on crée une prise
serveur = socket()
''# 0.0.0.0 : toutes les interfaces et le port 9999
serveur.bind(('0.0.0.0', 9999))
''# on met en mode écoute
serveur.listen()

''# on terminera avec un C-c
while True:
''    # sock_client est la prise entre le serveur et le client connecté
''    # ip_client est...l'adresse ip du client
    (sock_client, ip_client) = serveur.accept()
''    # le serveur attend au plus 100 octets du client
    donnees = sock_client.recv(100)
''    # tant que des données de longueur non nulles arrivent
    while donnees:
''        # on les affiche décodées
        print(donnees.decode())
''        # et on en attend d'autres
        donnees = sock_client.recv(100)
''    # on attend un autre client
    sock_client.close()
