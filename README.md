# Portfolio de fondamentaux en Machine Learning 

Ce dépôt regroupe des projets clés en Machine Learning, démontrant la maîtrise des techniques de régression (prédiction de valeurs continues) et de classification (prédiction de catégories). L'accent est mis sur le nettoyage des données, l'ingénierie des caractéristiques et l'évaluation  des modèles.

# Projet 1 : Analyse comparative des prix immobiliers en Californie (Régression ML)

Ce projet de Machine Learning a pour objectif de prédire la valeur médiane des maisons dans différents districts de la Californie en utilisant un jeu de données standard. L'analyse se concentre sur la **comparaison de la performance** entre un modèle linéaire simple et un modèle non linéaire complexe.


## ⚙️ Méthodologie et Modèles
| Étape | Description | Objectif |
| :--- | :--- | :--- |
| **Jeu de Données** | California Housing (8 features, dont le revenu, l'âge et la densité). | |
| **Split** | Division Train/Test (80%/20%) avec `random_state` fixé pour la reproductibilité. | |
| **Modèle 1** | **Régression Linéaire** (`LinearRegression`). | Modèle de référence simple (linéaire). |
| **Modèle 2** | **Arbre de Décision** (`DecisionTreeRegressor`). | Modèle flexible (non linéaire) pour une meilleure capture de la complexité des données. |
| **Évaluation** | Métriques **RMSE, MSE, et R² Score** sur l'ensemble de test. | |

## 📊 Résultats et Conclusion

### 📈 Performance du Modèle

| Modèle | RMSE (en $100K USD) | MSE (Erreur) | R² Score (Explicabilité) |
| :--- | :--- | :--- | :--- |
| **Régression Linéaire** | `0.7454` | `0.5556` | `0.5843` |
| **Arbre de Décision** | **`0.6923`** | **`0.4793`** | **`0.6409`** |


# Projet 2 : Prédiction de survie des passagers du Titanic (Classification logistique)

L'objectif de ce projet est de prédire si un passager a survécu au naufrage du Titanic en fonction de différentes caractéristiques.

## Méthodologie et modèle

| Étape         | Description                                                 | Objectif                              |
| ------------- | ----------------------------------------------------------- | ------------------------------------- |
| **Nettoyage** | Imputation des âges manquants par la médiane.               | Gérer les données incomplètes         |
| **Encodage**  | Conversion du sexe (*male / female*) en valeurs numériques. | Préparer les données pour le modèle   |
| **Modèle**    | Régression logistique (*LogisticRegression*).               | Prédire une variable binaire (0 ou 1) |


## Résultats
| Modèle                    | Accuracy (précision globale) | F1-score (équilibre) | Statut        |
| ------------------------- | ---------------------------- | -------------------- | ------------- |
| **Régression logistique** | 0.8034                       | 0.7586               | Modèle validé |

# 💻 Installation et Utilisation

Ces projets utilisent un environnement Python standard.

### Prérequis
Assurez-vous d'avoir Git et Python 3.x installés.

### Installation des Dépendances
```bash
# 1. Cloner le dépôt
git clone https://github.com/Lauriane4/ML-Portfolio-Fundamentals.git
cd ML-Portfolio-Fundamentals

# 2. Installer les librairies (Pandas, Scikit-learn, etc.)
pip install -r requirements.txt

```
## Exécution de l'analyse 

L'analyse complète est disponible dans le notebook Jupyter : 
```bash 
jupyter notebook Jupyter_Notebooks/nom-du-fichier.ipynb 
```
## 🛠️ Technologies
Langage : Python

Machine Learning : scikit-learn

Analyse/Manipulation : pandas, numpy

Visualisation : matplotlib, seaborn

## 📄 Licence
Ce projet est sous licence Apache 2.0.
