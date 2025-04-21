# Projet Python – Application Web avec FastAPI & Dash

Ce projet est une application web complète combinant deux frameworks : FastAPI pour la gestion du backend (API, routes, logique serveur) et Dash pour la visualisation interactive des données côté frontend.

# Objectif du projet

- Intégrer une API FastAPI avec une interface Dash dans une seule architecture
- Déployer une application performante pour servir à la fois des endpoints d’API et des dashboards dynamiques
- Structurer le code de manière claire et modulaire

# Technologies utilisées

- Python
- FastAPI
- Dash
- Uvicorn (serveur ASGI)
- Jinja2
- HTML/CSS/JavaScript (fichiers statiques)

# Structure du projet

```
├── fastapi_app/
│   ├── main.py              → Lancement du backend FastAPI
│   ├── templates/           → Templates HTML
│   └── static/              → Fichiers CSS/JS statiques
│
├── dash_app/                → Composants Dash
│
├── env/                     → Environnement virtuel
├── startup.sh               → Script de démarrage
├── requirements.txt         → Dépendances Python
├── .gitignore               → Exclusion des fichiers sensibles
├── LICENSE                  → Licence du projet
└── README.md                → Présentation du projet
```

# Fonctionnalités principales

- API REST exposée via FastAPI (routes définies dans `main.py`)
- Interface utilisateur interactive créée avec Dash
- Intégration possible via montage d’application Dash dans FastAPI
- Serveur unifié avec Uvicorn pour gestion ASGI

# Lancer l’application localement

1. Installer les dépendances :

```bash
pip install -r requirements.txt
```

2. Lancer le serveur :

```bash
sh startup.sh
```

Ou alternativement :

```bash
uvicorn fastapi_app.main:app --reload
```

3. Accéder à l’interface :

- API FastAPI : `http://localhost:8000`
- Dash : `http://localhost:8000/dash`

# Auteur

Projet réalisé par BOMO MEKA JOSPIN MARIEL, combinant FastAPI et Dash dans un environnement Python professionnel.
