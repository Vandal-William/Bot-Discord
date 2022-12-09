# Enigme

le jeu consiste a trouver le nom d'un manga a traver 5 question.
les questions donnerons des indices en rapport avec l'univer du manga.

Le jeu comporte 3 niveaux de difficulter :

- facile
- normal
- difficile

Chaque niveau est noté sur 10 :

- Répondre a une question sans indice rapporte 1.5 point
- Repondre a une question avec un indice rapporte 1 point
- la 5eme question sans indice rapporte 4 point
- la 5eme question avec indice rapporte 3.5 point
- il faut avoir 5/10 pour valider un niveau

# En ligne de commande :

### Installation d'un environement virtuel

> sudo apt install virtualenv

### création d'un dossier .envsp

> python -m virtualenv envsp

### installation des librairies dans l'environement virtuel

aller dans l'environnement virtuel:

> source envsp/bin/activate

Installation des librairie:

> pip install discord.py
> pip install asyncio
> pip install python-dotenv
