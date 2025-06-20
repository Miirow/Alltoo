# 🧾 Gestion – Application Django de gestion de produits et de factures

Ce projet est une application Django permettant :
- de gérer une liste de produits (CRUD),
- de générer des factures à partir des produits,
- d'afficher les factures avec pagination,
- d'utiliser une interface simple avec navigation.

## 🚀 Fonctionnalités

- Ajout, modification et suppression de produits
- Création automatique de factures
- Détail de facture avec total calculé
- Navigation intuitive
- Pagination des listes
- Interface stylisée avec CSS

---

## 📦 Installation

1. Cloner le dépôt :Créer un environnement virtuel (optionnel mais recommandé) :
git clone https://github.com/ton-utilisateur/ton-projet.git
cd ton-projet



2. Créer un environnement virtuel (optionnel mais recommandé) :
python -m venv env
source env/bin/activate     # sous Linux/macOS
env\Scripts\activate.bat    # sous Windows


3. Installer les dépendances :
pip install -r requirements.txt

Si le fichier requirements.txt n’existe pas, tu peux faire :
pip install django


4. Appliquer les migrations :
python manage.py migrate

5. Lancer le serveur local :
python manage.py runserver

6. Accéder à l'application :
Ouvre ton navigateur et va sur : http://127.0.0.1:8000
