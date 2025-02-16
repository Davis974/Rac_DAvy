class Personne:
    def __init__(self, nom, prenom, sexe):
        self.nom = nom
        self.prenom = prenom
        self.sexe = sexe


class Client(Personne):
    def __init__(self, nom, prenom, sexe, date_inscription, courriel, password):
        super().__init__(nom, prenom, sexe)
        self.date_inscription = date_inscription
        self.courriel = courriel
        self.password = password
        self.cartes_credit = []  # Liste de cartes de crédit


class Employe(Personne):
    def __init__(self, nom, prenom, sexe, date_embauche, code_utilisateur, password, type_acces):
        super().__init__(nom, prenom, sexe)
        self.date_embauche = date_embauche
        self.code_utilisateur = code_utilisateur
        self.password = password
        self.type_acces = type_acces


class CarteCredit:
    def __init__(self, numero, date_expiration, code_secret):
        self.numero = numero
        self.date_expiration = date_expiration
        self.code_secret = code_secret


class Film:
    def __init__(self, nom, duree, description):
        self.nom = nom
        self.duree = duree
        self.description = description
        self.categories = []  # Liste de catégories
        self.acteurs = []  # Liste d'acteurs


class Categorie:
    def __init__(self, nom, description):
        self.nom = nom
        self.description = description