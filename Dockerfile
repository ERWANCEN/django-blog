# Image de base : Python 3.14 en version allégée
FROM python:3.14-slim

# Pas de fichiers .pyc, et des logs affichés immédiatement
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Dossier de travail dans le conteneur
WORKDIR /app

# On copie d'abord requirements.txt SEUL pour profiter du cache Docker :
# tant que ce fichier ne change pas, pip install n'est pas relancé.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Puis le reste du code
COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]