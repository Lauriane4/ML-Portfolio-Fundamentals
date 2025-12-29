import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report
from .nlp import extract_attributes
from .recommender import recommend_product
import json

# Charger les données des produits
with open("makeup_app/data/makeup_dataset.json", "r", encoding="utf-8") as f:
    PRODUCTS = json.load(f)

# Données de test : liste de tuples (description, true_product_id)
test_data = [
    ("Je cherche un fond de teint liquide à forte couvrance, fini mat, pour un usage quotidien ou professionnel, à prix moyen.", 1),

    ("Je veux un rouge à lèvres mat et crémeux, très couvrant, pour une soirée ou un mariage, de gamme luxe.", 2),

    ("Je cherche un blush liquide lumineux, à couvrance moyenne, pour un look frais au quotidien ou en soirée.", 3),

    ("Je veux une palette de fards à paupières aux tons chauds, avec des finis mats et lumineux, pour le quotidien et les soirées.", 4),

    ("Je cherche un gloss brillant, léger, non collant, pour un usage quotidien et à petit prix.", 5),

    ("Je veux un fond de teint liquide à couvrance moyenne, fini lumineux, confortable pour le quotidien et abordable.", 6),

    ("Je cherche un gloss universel très brillant, léger, pour le quotidien ou les soirées, à prix moyen.", 7),

    ("Je veux un blush poudre mat, élégant, à couvrance moyenne, pour le travail ou le quotidien, en gamme luxe.", 8),

    ("Je cherche une petite palette de fards très pigmentés pour une soirée, avec des finis mats et brillants.", 9),

    ("Je veux une base de maquillage illuminatrice, légère, pour un teint lumineux au quotidien ou pour un mariage.", 10),

    ("Je cherche un fond de teint liquide haute couvrance, fini mat, longue tenue, pour un usage professionnel ou en soirée, luxe.", 11),

    ("Je veux un fond de teint mat, léger à couvrance moyenne, idéal pour le quotidien et à petit prix.", 12),

    ("Je cherche un fond de teint lumineux à couvrance moyenne, effet naturel, pour le quotidien ou le travail, gamme luxe.", 13),

    ("Je veux un rouge à lèvres crémeux et satiné, très couvrant, élégant pour le quotidien ou le travail, luxe.", 14),

    ("Je cherche un rouge à lèvres mat intense, très couvrant, parfait pour une soirée, à prix moyen.", 15),

    ("Je veux un rouge à lèvres liquide ultra mat, très longue tenue, pour une soirée, abordable.", 16),

    ("Je cherche un blush poudre lumineux, à couvrance moyenne, iconique, pour le quotidien ou les soirées, luxe.", 17),

    ("Je veux un blush crème léger, effet bonne mine, facile à porter au quotidien et à petit prix.", 18),

    ("Je cherche un blush poudre mat, professionnel et élégant, à couvrance moyenne, de gamme luxe.", 19),

    ("Je veux un highlighter poudre très lumineux pour une soirée, avec un effet glow intense, abordable.", 20),

    ("Je cherche une palette de fards à paupières luxe, très pigmentée, aux tons neutres, pour le travail ou les soirées.", 21),

    ("Je veux une palette de fards à paupières aux teintes chocolatées, facile à porter au quotidien, luxe.", 22),

    ("Je cherche un eyeliner liquide noir très précis, longue tenue, pour un usage professionnel ou en soirée.", 23),

    ("Je veux un mascara naturel, allongeant, pour le quotidien et à petit prix.", 24),

    ("Je cherche une palette de fards neutres et chauds, polyvalente pour le quotidien et les soirées, luxe.", 25),

    ("Je veux un bronzer poudre mat, à couvrance moyenne, pour un effet bonne mine au quotidien.", 26),

    ("Je cherche une palette de fards très pigmentée, aux tons chauds et neutres, pour le quotidien et les soirées, luxe.", 27),

    ("Je veux un fond de teint liquide léger, fini lumineux, très naturel, pour le quotidien, luxe.", 28),

    ("Je cherche un spray fixant léger, fini lumineux, pour un maquillage frais au quotidien.", 29),

    ("Je veux un rouge à lèvres crémeux à finition satinée, couvrance moyenne, pour le quotidien.", 30),

    ("Je cherche un fond de teint mat à très forte couvrance, idéal pour une soirée, en gamme luxe.", 31),

    ("Je veux un blush liquide lumineux, modulable, pour un éclat naturel au quotidien.", 32),

    ("Je cherche un rouge à lèvres liquide ultra mat, très couvrant, longue tenue, pour une soirée et à petit prix.", 33),

    ("Je veux un crayon à sourcils fin, naturel, facile à utiliser au quotidien.", 34),

    ("Je cherche un eyeliner liquide coloré, très couvrant, longue tenue, pour une soirée, abordable.", 35),

    ("Je veux un rouge à lèvres liquide mat, très couvrant, confortable pour le quotidien, à petit prix.", 36),

    ("Je cherche une palette de fards bleus très pigmentés, avec des finis mats et brillants, pour une soirée, luxe.", 37),

    ("Je veux un blush poudre lumineux original, à couvrance moyenne, pour un look frais au quotidien.", 38),

    ("Je cherche un rouge à lèvres mat très couvrant, couleur orange vive, pour le quotidien et à petit prix.", 39),

    ("Je veux une palette de fards colorée, très pigmentée, pour des looks fun au quotidien et en soirée.", 40)
]

def evaluate_model(test_data, products, top_k=1):
    """
    Évalue le modèle de recommandation sur les données de test.
    Pour chaque description, recommande le top produit et compare au vrai produit.
    Retourne les vraies étiquettes et les prédictions pour calcul des métriques.
    """
    y_true = []
    y_pred = []

    for description, true_id in test_data:
        extracted = extract_attributes(description)
        recommendations = recommend_product(products, extracted, top_k=top_k)
        if recommendations:
            pred_id = recommendations[0][1]['id']  # ID du produit recommandé (top 1)
        else:
            pred_id = None  # Aucun recommandé

        y_true.append(true_id)
        y_pred.append(pred_id)

    return y_true, y_pred

def compute_metrics(y_true, y_pred):
    """
    Calcule les métriques : accuracy, precision, recall, F1, et matrice de confusion.
    """
    # Filtrer les None si nécessaire, mais pour simplicité, assumons toujours une prédiction
    y_pred = [p if p is not None else -1 for p in y_pred]  # -1 pour aucun

    # Accuracy
    accuracy = accuracy_score(y_true, y_pred)

    # Precision, Recall, F1-Score 
    precision = precision_score(y_true, y_pred, average='macro', zero_division=0)
    recall = recall_score(y_true, y_pred, average='macro', zero_division=0)
    f1 = f1_score(y_true, y_pred, average='macro', zero_division=0)

    # Matrice de confusion
    cm = confusion_matrix(y_true, y_pred)

    # Rapport de classification
    report = classification_report(y_true, y_pred, zero_division=0)

    return {
        'accuracy': accuracy,
        'precision': precision,
        'recall': recall,
        'f1_score': f1,
        'confusion_matrix': cm,
        'classification_report': report
    }

def display_metrics(metrics):
    """
    Affiche les métriques de manière lisible.
    """
    print("=== Évaluation du Modèle de Recommandation ===\n")
    print(f"Accuracy: {metrics['accuracy']:.4f}")
    print(f"Precision (macro): {metrics['precision']:.4f}")
    print(f"Recall (macro): {metrics['recall']:.4f}")
    print(f"F1-Score (macro): {metrics['f1_score']:.4f}")
    print("\nMatrice de Confusion:")
    print(metrics['confusion_matrix'])
    print("\nRapport de Classification:")
    print(metrics['classification_report'])

if __name__ == "__main__":
    # Évaluer le modèle
    y_true, y_pred = evaluate_model(test_data, PRODUCTS, top_k=1)
    metrics = compute_metrics(y_true, y_pred)
    display_metrics(metrics)