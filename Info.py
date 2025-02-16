from models import Client, Employe, Film, Categorie
r la liste des clients en appelant
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
