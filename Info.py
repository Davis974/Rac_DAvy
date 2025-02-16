

# Même chose ici. On a un tableau clients = []
# Et dedans on a créé 2 entités Client
clients = [
    Client("Alice", "Walker", "F", "2022-10-01", "alice@example.com", "alice1234"),
    Client("Bob", "Johnson", "M", "2023-06-15", "bob@example.com", "bobpass")
]

# Même chose ici.
films = [
    Film("Film 1", 120, "Un film d'action captivant."),
    Film("Film 2", 90, "Une comédie hilarante.")
]

# Même chose ici.
categories = [
    Categorie("Action", "Des films palpitants et intenses."),
    Categorie("Comédie", "Des films pour rire et se détendre.")
]

# on crée une fonction que l'on nomme afficher_clients

def afficher_clients():
    # La première chose qu'il fait c'est d'écrire Liste des clients
    # le symbole \n permet de faire un saut de ligne. Plus on en rajoute, plus on créé des espaces
    print("\nListe des clients :")
    # Ensuite on fait une boucle qui a la structure suivante
    # for _____ : et on ajoute après les 2 points ce que l'on souhaite exécuter
    # dans notre exemple on créé un index que l'on nomme idx (C'est just un chiffre qui augmente ici)
    # on va aller chercher le tableau clients et on va dire que l'on démarre le compteur à 1
    # sur cette même ligne on voit le mot client au singulier, cela veut dire que chaque entrée que l'on va
    # trouver dans le tableau clients on va l'appeler client
    for idx, client in enumerate(clients, start=1):
        print(f"{idx}. {client.nom} {client.prenom} - {client.courriel}")

# on créé la fonction ajouter_client
def ajouter_client():
    # La première chose qu'il fait c'est d'écrire Ajout d'un nouveau client toujours avec notre espace au dessus \n
    print("\nAjout d'un nouveau client")
    # on va créer des zones de textes dans lesquelles on va pouvoir écrire. Ca s'appelle des input
    # donc chaque input aura un intitulé comme par exemple Nom
    # Strip permet de retirer les espaces avant et après ce que l'on aura écrit
    # on stocke ses informations dans des variables comme par exemple nom (qui est au début de la ligne)
    nom = input("Nom : ").strip()
    prenom = input("Prénom : ").strip()
    courriel = input("Courriel : ").strip()
    password = input("Mot de passe (min 8 caractères) : ").strip()

    # len veut dire longueur donc ici le code veut dire : SI la longueur de la variable password est inférieur à 8
    # Alors affiche un message d'erreur et arrête ça là
    if len(password) < 8:
        print("Erreur : Le mot de passe doit contenir au moins 8 caractères.")
        return

    # any va vérifier si l'information qu'on lui donne existe deja. Ici on vérifie si le courriel entré est déjà dans
    # des courriels des clients. Si c'est le cas alors on met un message d'erreur et on arrête ça là
    if any(client.courriel == courriel for client in clients):
        print("Erreur : Le courriel doit être unique.")
        return

    # Si on a pas d'erreur alors on va créer une nouvelle entité Client() avec dedans les informations que l'on
    # aura entré plus haut. J'ai mis Non spécifié pour le sexe mais on pourrait modifier le code plus haut
    # pour demander cette information. Et j'avais mis une date bidon pour la date
    # le nouveau client que l'on va créer on va le stocker dans nouveau_client
    # et on va l'ajouter a la suite de tous nos autres clients dans le tableau clients
    # on finit par écrire que le client a été bien ajouté
    nouveau_client = Client(nom, prenom, "Non spécifié", "2024-11-26", courriel, password)
    clients.append(nouveau_client)
    print(f"Client {nom} {prenom} ajouté avec succès.")

# on créé la fonction modifier_client
def modifier_client():
    # La 1ere chose qu'on fait c'est d'afficher la liste des clients en appelant
    # la fonction afficher_clients
    afficher_clients()
     # on va créer des zones de textes dans lesquelles on va pouvoir écrire. Ca s'appelle des input
    # donc le input aura un intitulé qu'on va appeler choix et qu'on va stocker
    choix = input("\nEntrez le numéro du client à modifier (ou 'q' pour annuler) : ").strip()

    # si on rentre la lettre Q c'est que l'on souhaite quitter la modification du client
    if choix.lower() == 'q':
        return

    # on va essayer (d'où le mot TRY) de trouver l'index (l'endroit si tu veux) où se trouve le client
    # a modifier dans le tableau CLIENTS. On met d'ailleurs un -1 en avant de notre choix car
    # les tableaux commencent toujours par zéro donc Alice est à la position 0 et Bob à la position 1
    # Si on veut modifier Bob on aura rentré 2 comme choix vu que visuellement on a
    # 1 - Alice et 2 - Bob donc pour trouver leur place dans le tableau on va faire choix 2 moins 1
    # si on trouve rien (par exemple si on avait rentré le chiffre 5 comme choix) on aura un message d'erreur
    try:
        index = int(choix) - 1
        client = clients[index]
    except (ValueError, IndexError):
        print("Erreur : Numéro invalide.")
        return

    # on va aller chercher les informations du client selon le choix qu'on a fait juste au dessus on a
    # stocké les informations du client qu'on a trouvé dans la variable CLIENT
    # et on l'utilise juste en dessous
    print("\nModification du client sélectionné :")
    nom = input(f"Nom ({client.nom}) : ").strip() or client.nom
    prenom = input(f"Prénom ({client.prenom}) : ").strip() or client.prenom
    courriel = input(f"Courriel ({client.courriel}) : ").strip() or client.courriel

    # on vérifie si le nouveau courriel entré est déjà présent dans la base de données
    if any(c.courriel == courriel and c != client for c in clients):
        print("Erreur : Le courriel doit être unique.")
        return

    # on met à jour les informations du client
    client.nom = nom
    client.prenom = prenom
    client.courriel = courriel
    print("Les informations du client ont été mises à jour avec succès.")

# on créé la fonction supprimer_client
def supprimer_client():
    # La 1ere chose qu'on fait c'est d'afficher la liste des clients en appelant
    # la fonction afficher_clients
    afficher_clients()
    # Ensuite on stocke le choix que l'on a fait dans la liste dans une variable nommée CHOIX
    choix = input("\nEntrez le numéro du client à supprimer (ou 'q' pour annuler) : ").strip()

    # si on veut quitter on choisit Q
    if choix.lower() == 'q':
        return

    # même chose avec les choix invalides ici
    try:
        index = int(choix) - 1
        client = clients[index]
    except (ValueError, IndexError):
        print("Erreur : Numéro invalide.")
        return

    # On créé ici une question et on va stocker la réponse dans une variable CONFIRMATION
    confirmation = input(f"Êtes-vous sûr de vouloir supprimer {client.nom} {client.prenom} ? (o/n) : ").strip().lower()
    #si la réponse est O alors on supprimer l'entrée dans le tableau et on écrit un texte
    if confirmation == 'o':
        del clients[index]
        print("Client supprimé avec succès.")
    else:
        print("Suppression annulée.")

# on créé la fonction menu_principal
def menu_principal():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Afficher les clients")
        print("2. Ajouter un client")
        print("3. Modifier un client")
        print("4. Supprimer un client")
        print("5. Quitter")
        choix = input("Choisissez une option : ").strip()

        if choix == '1':
            afficher_clients()
        elif choix == '2':
            ajouter_client()
        elif choix == '3':
            modifier_client()
        elif choix == '4':
            supprimer_client()
        elif choix == '5':
            print("Au revoir !")
            break
        else:
            print("Erreur : Option invalide.")

# quand l'application est exécutée il n'y a rien qui est appelé hormis la fonction menu_principal
# et c'est dans cette fonction que tout se pass et qu'on appelle les différents choix d'action juste au dessus
if __name__ == "__main__":
    menu_principal()