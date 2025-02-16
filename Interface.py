import tkinter as tk
from tkinter import messagebox
from models import Client, Employe, Film, Categorie

# Données simulées
# Employés codés en dur
employes = [
    Employe("John", "Doe", "M", "2023-01-01", "admin123", "password123", "total"),
    Employe("Jane", "Smith", "F", "2022-05-15", "reader456", "securepass", "lecture"),
    Employe("John", "Brown", "M", "2024-02-01", "john_user", "johnpass123", "total"),
    Employe("Jane", "White", "F", "2024-03-15", "jane_user", "janepass456", "lecture")
]

# Clients codés en dur
clients = [
    Client("Alice", "Walker", "F", "2022-10-01", "alice@example.com", "alice1234"),
    Client("Bob", "Johnson", "M", "2023-06-15", "bob@example.com", "bobpass")
]

# Films codés en dur
films = [
    Film("Titanic", 120, "Un film d'action captivant."),
    Film("Avatar", 90, "Une comédie hilarante.")
]

# Catégories codées en dur
categories = [
    Categorie("Action", "Des films palpitants et intenses."),
    Categorie("Comédie", "Des films pour rire et se détendre.")
]


# Fonctions de validation
def ajouter_client(nom, prenom, courriel, password):
    if len(password) < 8:
        messagebox.showerror("Erreur", "Le mot de passe doit contenir au moins 8 caractères.")
        return
    for client in clients:
        if client.courriel == courriel:
            messagebox.showerror("Erreur", "Le courriel doit être unique.")
            return
    nouveau_client = Client(nom, prenom, "Non spécifié", "2024-11-26", courriel, password)
    clients.append(nouveau_client)
    messagebox.showinfo("Succès", f"Client {nom} {prenom} ajouté avec succès.")


# Interface graphique
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Système de gestion")
        self.geometry("800x900")
        self.configure(bg="#f7f7f7")
        self.client_list = None
        self.create_login_window()

    def create_login_window(self):
        self.clear_window()
        tk.Label(self, text="Code Utilisateur").pack(pady=10)
        code_utilisateur = tk.Entry(self)
        code_utilisateur.pack()
        tk.Label(self, text="Mot de Passe").pack(pady=10)
        password = tk.Entry(self, show="*")
        password.pack()
        tk.Button(self, text="Se Connecter", command=self.create_main_window).pack(pady=20)

    def create_main_window(self):
        self.clear_window()
        tk.Label(self, text="Gestion des clients et films", font=("Arial", 18)).pack(pady=20)

        # Liste des clients
        tk.Label(self, text="Liste des clients").pack(pady=10)
        self.client_list = tk.Listbox (self, width=40, height=5)
        for client in clients:
            self.client_list.insert(tk.END, f"{client.nom} {client.prenom} - {client.courriel} ")
        self.client_list.pack(pady=10)

        # Liste des films
        tk.Label(self, text="Liste des films").pack(pady=10)
        film_list = tk.Listbox(self, width=20, height=5)
        for film in films:
            film_list.insert(tk.END, f"{film.nom} ({film.duree} min)")
        film_list.pack(pady=10)

        # Boutons
        tk.Button(self, text="Créer un client", command=self.create_client_window).pack(pady=10)
        tk.Button(self, text="Modifier Client", command=self.modify_client_window).pack(pady=10)
        tk.Button(self, text="Supprimer Client", command=self.delete_client).pack(pady=10)
        tk.Button(self, text="Déconnexion", command=self.create_login_window).pack(pady=10)

    def create_client_window(self):
        self.clear_window()
        tk.Label(self, text="Création d'un client", font=("Arial", 18)).pack(pady=20)

        # Champs de saisie
        tk.Label(self, text="Nom").pack()
        nom_entry = tk.Entry(self)
        nom_entry.pack()
        tk.Label(self, text="Prénom").pack()
        prenom_entry = tk.Entry(self)
        prenom_entry.pack()
        tk.Label(self, text="Courriel").pack()
        courriel_entry = tk.Entry(self)
        courriel_entry.pack()
        tk.Label(self, text="Mot de Passe").pack()
        password_entry = tk.Entry(self, show="*")
        password_entry.pack()

        # Bouton de validation
        tk.Button(
            self,
            text="Créer",
            command=lambda: ajouter_client(
                nom_entry.get(),
                prenom_entry.get(),
                courriel_entry.get(),
                password_entry.get(),
            ),
        ).pack(pady=20)
        tk.Button(self, text="Retour", command=self.create_main_window).pack()

    def modify_client_window(self):
        selected_index = self.client_list.curselection()
        if not selected_index:
            messagebox.showerror("Erreur", "Veuillez sélectionner un client à modifier.")
            return

        client = clients[selected_index[0]]

        # Fenêtre de modification
        modif_window = tk.Toplevel(self)
        modif_window.title("Modifier Client")
        modif_window.geometry("400x300")

        # Champs de saisie avec valeurs actuelles
        tk.Label(modif_window, text="Nom").pack(pady=5)
        nom_var = tk.StringVar(value=client.nom)
        nom_entry = tk.Entry(modif_window, textvariable=nom_var)
        nom_entry.pack(pady=5)

        tk.Label(modif_window, text="Prénom").pack(pady=5)
        prenom_var = tk.StringVar(value=client.prenom)
        prenom_entry = tk.Entry(modif_window, textvariable=prenom_var)
        prenom_entry.pack(pady=5)

        tk.Label(modif_window, text="Courriel").pack(pady=5)
        courriel_var = tk.StringVar(value=client.courriel)
        courriel_entry = tk.Entry(modif_window, textvariable=courriel_var)
        courriel_entry.pack(pady=5)

        # Fonction pour sauvegarder les modifications
        def sauvegarder():
            nom = nom_var.get().strip()
            prenom = prenom_var.get().strip()
            courriel = courriel_var.get().strip()

            if not nom or not prenom or not courriel:
                messagebox.showerror("Erreur", "Tous les champs doivent être remplis.")
                return

            if any(c.courriel == courriel and c != client for c in clients):
                messagebox.showerror("Erreur", "Le courriel doit être unique.")
                return

            # Mise à jour des données
            client.nom = nom
            client.prenom = prenom
            client.courriel = courriel

            # Mise à jour de la liste des clients
            self.client_list.delete(selected_index)
            self.client_list.insert(selected_index, f"{client.nom} {client.prenom} - {client.courriel}")
            messagebox.showinfo("Succès", "Les informations du client ont été mises à jour.")
            modif_window.destroy()

        tk.Button(modif_window, text="Sauvegarder", command=sauvegarder).pack(pady=20)

    def delete_client(self):
        selected_index = self.client_list.curselection()
        if not selected_index:
            messagebox.showerror("Erreur", "Veuillez sélectionner un client à supprimer.")
            return

        client = clients[selected_index[0]]
        confirmation = messagebox.askyesno(
            "Confirmation", f"Êtes-vous sûr de vouloir supprimer {client.nom} {client.prenom} ?"
        )
        if confirmation:
            del clients[selected_index[0]]
            self.client_list.delete(selected_index)
            messagebox.showinfo("Succès", "Client supprimé avec succès.")

    def clear_window(self):
        for widget in self.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    app = Application()
    app.mainloop()