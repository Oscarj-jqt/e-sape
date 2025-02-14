## Table des matières

- [Contexte](#contexte)
- [Installation](#installation)
  - [Création d'un environnement virtuel](#création-dun-environnement-virtuel)
  - [Activation de l'environnement virtuel](#activation-de-lenvironnement-virtuel)
  - [Installation des dépendances](#installation-des-dépendances)
  - [Comment lancer le projet](#comment-lancer-le-projet)
- [Participants](#participants)
- [Auteur](#auteur)

## Contexte

E-sape est une application de boutique en ligne développée en utilisant Flask pour le backend et React pour le frontend. Le projet permet aux utilisateurs de consulter des produits, de les afficher en détails, et de les ajouter à leur panier. Il inclut une gestion de produits via une API REST et GraphQL, ainsi qu'une authentification basée sur JWT.

![demo page](/documentation/home.png)

## Installation

### Création d'un environnement virtuel

```bash
python3 -m venv venv

# Depuis la racine

source venv/bin/activate # sur macOS/Linux
source venv\Scripts\activate # sur Windows

# Pour désactiver votre environnement virtuel

deactivate
```

Installation des dépendances

# Depuis la racine

pip install -r requirements.txt

Lancer le projet 
# Depuis la racine

```bash
python3 app.py

```



