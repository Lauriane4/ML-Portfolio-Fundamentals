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

    ("Je veux un mascara volumisant, très couvrant, pour un effet dramatique au quotidien ou en soirée.", 30),

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

# -----------------------------
# Évaluation Ranking
# -----------------------------
def evaluate_ranking(test_data, products, top_k=5):
    ranks = []
    hits_at_1 = 0
    hits_at_k = 0

    for text, true_id in test_data:
        extracted = extract_attributes(text)
        recommendations = recommend_product(products, extracted, top_k=top_k)

        recommended_ids = [prod["id"] for _, prod in recommendations]

        if true_id in recommended_ids:
            rank = recommended_ids.index(true_id) + 1
            ranks.append(rank)

            if rank == 1:
                hits_at_1 += 1
            hits_at_k += 1
        else:
            ranks.append(None)

    return ranks, hits_at_1, hits_at_k


# -----------------------------
# Métriques Ranking
# -----------------------------
def compute_ranking_metrics(ranks, hits_at_1, hits_at_k, total):
    valid_ranks = [r for r in ranks if r is not None]

    top1_accuracy = hits_at_1 / total
    topk_accuracy = hits_at_k / total

    mrr = np.mean([1 / r for r in valid_ranks]) if valid_ranks else 0
    mean_rank = np.mean(valid_ranks) if valid_ranks else None

    return {
        "top1_accuracy": top1_accuracy,
        "topk_accuracy": topk_accuracy,
        "mrr": mrr,
        "mean_rank": mean_rank
    }


# -----------------------------
# Affichage
# -----------------------------
def display_metrics(metrics):
    print("\n=== Évaluation du Système de Recommandation ===\n")
    print(f"Top-1 Accuracy : {metrics['top1_accuracy']:.2f}")
    print(f"Top-K Accuracy (K=5): {metrics['topk_accuracy']:.2f}")
    print(f"MRR            : {metrics['mrr']:.2f}")
    print(f"Mean Rank     : {metrics['mean_rank']:.2f}")


# -----------------------------
# Main
# -----------------------------
if __name__ == "__main__":
    ranks, hits1, hitsk = evaluate_ranking(test_data, PRODUCTS, top_k=5)
    metrics = compute_ranking_metrics(ranks, hits1, hitsk, total=len(test_data))
    display_metrics(metrics)