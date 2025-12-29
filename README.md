# Portfolio de fondamentaux en Machine Learning

Ce dépôt regroupe plusieurs projets clés en Machine Learning, illustrant la maîtrise des concepts fondamentaux de la discipline, allant de la régression et de la classification supervisée jusqu’à la conception d’un système de recommandation. L’accent est mis sur le nettoyage des données, l’ingénierie des caractéristiques, l’évaluation des modèles ainsi que sur les bonnes pratiques de déploiement.

---

## 🔹 Projet 1 : Analyse comparative des prix immobiliers en Californie  
*(Régression supervisée)*

Ce projet de Machine Learning a pour objectif de prédire la valeur médiane des maisons dans différents districts de la Californie à partir d’un jeu de données standard. L’analyse se concentre sur la comparaison des performances entre un modèle linéaire simple et un modèle non linéaire plus complexe.

### ⚙️ Méthodologie et modèles

| Étape | Description | Objectif |
|------|------------|----------|
| Jeu de données | California Housing (8 variables explicatives) | Modéliser la valeur immobilière |
| Split | Division Train/Test (80 % / 20 %) | Évaluer la généralisation |
| Modèle 1 | Régression linéaire | Modèle de référence |
| Modèle 2 | Arbre de décision | Capturer la non-linéarité |
| Évaluation | RMSE, MSE, R² | Comparer les performances |

### 📊 Résultats

| Modèle | RMSE | MSE | R² |
|------|------|-----|----|
| Régression linéaire | 0.7454 | 0.5556 | 0.5843 |
| Arbre de décision | 0.6923 | 0.4793 | 0.6409 |

---

## 🔹 Projet 2 : Prédiction de survie des passagers du Titanic  
*(Classification supervisée)*

L’objectif de ce projet est de prédire la survie des passagers du Titanic à partir de caractéristiques socio-démographiques.

### ⚙️ Méthodologie

| Étape | Description | Objectif |
|------|------------|----------|
| Nettoyage | Imputation des âges manquants par la médiane | Gérer les données incomplètes |
| Encodage | Transformation des variables catégorielles | Préparer les données |
| Modèle | Régression logistique | Classification binaire |

### 📊 Résultats

| Modèle | Accuracy | F1-score | Statut |
|------|----------|----------|--------|
| Régression logistique | 0.8034 | 0.7586 | Modèle validé |

---

## 🔹 Projet 3 : Système de recommandation de produits cosmétiques  
*(NLP & Ranking)*

Ce projet vise à concevoir un système de recommandation capable de suggérer le produit cosmétique le plus pertinent à partir d’une description textuelle en langage naturel fournie par l’utilisateur.

### 🧠 Approche

- Extraction d’attributs à partir du texte (zone du visage, texture, finition, couvrance, occasion, gamme de prix, couleur)
- Calcul d’un score de similarité basé sur un système de pondération
- Classement des produits par ordre de pertinence (ranking)

### 📏 Évaluation du système

- **Top-1 Accuracy** : 0.60  
- **Top-K Accuracy** : 0.93  
- **Mean Reciprocal Rank (MRR)** : 0.80  
- **Mean Rank** : 1.54  

Ces métriques montrent que le produit attendu apparaît majoritairement parmi les premières recommandations.

### 💻 Application et déploiement

Une application interactive a été développée avec **Streamlit**, puis entièrement **dockerisée**, garantissant la portabilité et la reproductibilité de l’environnement.

---

## 🐳 Docker – Exécution du projet 3

### Construction de l’image Docker

```bash
docker build -t makeup-app .
```
### Lancement du conteneur

```bash
docker run -p 8501:8501 makeup-app
```

L’application est accessible à l’adresse suivante :

http://localhost:8501

--- 
## 💻 Installation et utilisation (hors Docker)
### Prérequis

- Git

- Python 3.x

### Installation

```bash
git clone https://github.com/Lauriane4/ML-Portfolio-Fundamentals.git
cd ML-Portfolio-Fundamentals
pip install -r requirements.txt
```
---
## 🛠️ Technologies

- Langage : Python

- Machine Learning : scikit-learn

- Analyse de données : pandas, numpy

- Visualisation : matplotlib, seaborn

- NLP & Recommandation : règles métier, scoring, ranking

- Application web : Streamlit

- Déploiement : Docker

---

## 📄 Licence

Ce projet est sous licence Apache 2.0.

