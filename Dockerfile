# Image de base
FROM python:3.9-slim

# Variables pour pip et cache
ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# Répertoire de travail
WORKDIR /app

# Copier uniquement les requirements 
COPY requirements.txt .

# Installer les dépendances
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copier le reste de l'application
COPY . .

# Exposer le port de Streamlit
EXPOSE 8501

# Commande par défaut
CMD ["streamlit", "run", "makeup_app/app.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.enableCORS=false", "--server.headless=true"]
