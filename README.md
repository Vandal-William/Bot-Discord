# Manga-Quest

![image](./images/mangas2.jpeg)

## Le but du jeu :

Manga-Quest est un bot discord qui propose à l'utilisateur de résoudre des énigmes liés aux mangas.

Chaque énigme possède un niveau de difficulté il va de facile à difficile. Il existe pour le moment 3 niveau de difficulté, facile, normal et difficile. Chaque niveau se compose de 5 questions, les quatre premières sont des indices liés à l'univers du manga, à la cinquième question il faut donner le nom du manga.

Chaque niveau est notée sur 10 points, il faut un minimum de 5 sur 10 pour valider un niveau. Chaque question rapporte donc 2 points. Vous avez la possibilité de demander un indice à chaque question, mais cela ne vous rapportera que 1,5 point au lieu de 2.

## Les commandes:

- ' start ' pour lancer les énigmes
- ' indice ' pour demander un Indice sur une question.

## Les Futurs:

le bot discord est encore un MVP voici les fonctionnalités futures :

- Mise en ligne du bots discord pour qu'il tourne 24 heures sur 24, 7 jours sur 7
- Permettre aux joueurs de renseigner son nom au début de la partie
- Etablir un système de ranking
- Permettent aux joueurs de choisir le niveau de difficulté
- Ajouter plus de questions à chaque niveau, et en pose 5 de manière aléatoire
- Mettre en place le passage au niveau supérieur selon le score obtenu (pour le moment les niveaux s'enchaînent les uns après les autres sans vérifier le score)

## Le channel discorde du jeu :

> https://discord.gg/tN3C9vjv

# Dev

## Installation d'un environement virtuel

> sudo apt install virtualenv

## création d'un dossier .envsp

> python -m virtualenv envsp

## installation des librairies dans l'environement virtuel

aller dans l'environnement virtuel:

> source envsp/bin/activate

Installation des librairie:

> pip install discord.py

##

> pip install asyncio

##

> pip install python-dotenv

##
