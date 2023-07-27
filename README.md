# TP Docker Flask

## Description

Exercice consistant à créer une application CRUD avec Flask sur python et à la déployer sur un serveur MongoDB via docker. Exercice effectué sur une après-midi durant une formation data chez M2I.

## Prérequis

- Python 3.8
- Docker
- Docker-compose
- Git

## Installation

- Clonez le projet
- Créez un environnement virtuel

    ```bash
    # Linux
    python -m venv .venv
    # Windows
    py -m venv .venv
    ```

- Activez l'environnement virtuel

    ```bash
    # Linux
    source venv/bin/activate
    # Windows batch/cmd.exe
    venv\Scripts\activate.bat

    #windows powershell
    venv\Scripts\Activate.ps1
    ```

- démarrer la base de données et installer les requirements

```bash
docker-compose up
```

