import socket

hote = ''
port = 12800

connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_principale.bind((hote, port))
connexion_principale.listen(5)
print("Le serveur écoute à présent sur le port {}".format(port))

connexion_avec_client, infos_connexion = connexion_principale.accept()

Valeur1 = float(connexion_avec_client.recv(1024).decode())
Valeur2 = float(connexion_avec_client.recv(1024).decode())
Signe = connexion_avec_client.recv(1024).decode()

resulat = ""

if Signe == "+":
    resultat = Valeur1 + Valeur2
    print(resultat)
    resultat = str(resultat).encode()
    connexion_avec_client.send(resultat)
elif Signe == "-":
    resultat = Valeur1 - Valeur2
    print(resultat)
    resultat = str(resultat).encode()
    connexion_avec_client.send(resultat)
elif Signe == "*":
    resultat = Valeur1 * Valeur2
    print(resultat)
    resultat = str(resultat).encode()
    connexion_avec_client.send(resultat)
else:
    resultat = Valeur1 / Valeur2
    print(resultat)
    resultat = str(resultat).encode()
    connexion_avec_client.send(resultat)