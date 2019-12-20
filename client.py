import socket

hote = "localhost"
port = 12800

connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_avec_serveur.connect((hote, port))
print("Connexion établie avec le serveur sur le port {}".format(port))


Valeur1 = input()
Valeur2 = input()
Signe = input()

Valeur1 = Valeur1.encode()
Valeur2 = Valeur2.encode()
Signe = Signe.encode()

connexion_avec_serveur.send(Valeur1)
connexion_avec_serveur.send(Valeur2)
connexion_avec_serveur.send(Signe)

result = connexion_avec_serveur.recv(1024).decode()
print(result)

print("Fermeture de la connexion")
connexion_avec_serveur.close()