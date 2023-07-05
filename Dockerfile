# app flask pour gérer des utilisateurs associées à une base de données mongodb

# on part d'une image python
FROM python:3.8

# création d'un répertoire de travail
WORKDIR /app/flask

# copie des fichiers de dépendances
COPY requirements.txt .

# installation des dépendances
RUN pip install -r requirements.txt

# copie de l'application
COPY app.py .

# ouverture du port de l'application
EXPOSE 5000

# démarrage de l'application
CMD ["python", "app.py"]

