# tests/test_recommender.py
import pytest
from src.recommender import score_single_product, recommend_product

def test_score_single_product_match():
    product = {
        "zone": "lèvres",
        "texture": ["crémeux"],
        "finition": ["mat"],
        "occasion": ["soirée"],
        "couvrance": "forte",
        "couleur": ["rouge"],
        "gamme_prix": "luxe"
    }

    extracted = {
        "zone": "lèvres",
        "texture": ["crémeux"],
        "finition": ["mat"],
        "occasion": ["soirée"],
        "couvrance": "forte",
        "couleur": ["rouge"],
        "gamme_prix": "luxe"
    }

    score = score_single_product(product, extracted)
    assert score > 0
    assert score >= 10  # Vérifie que la pondération a été appliquée

def test_recommend_products_top6():
    products = [
        {
            "nom": "Produit A",
            "zone": "visage",
            "texture": ["liquide"],
            "finition": ["mat"],
            "occasion": ["quotidien"],
            "couvrance": "moyenne",
            "couleur": [],
            "gamme_prix": "moyenne"
        },
        {
            "nom": "Produit B",
            "zone": "lèvres",
            "texture": ["crémeux"],
            "finition": ["mat"],
            "occasion": ["soirée"],
            "couvrance": "forte",
            "couleur": ["rouge"],
            "gamme_prix": "luxe"
        },
        {
            "nom": "Produit C",
            "zone": "lèvres",
            "texture": ["liquide"],
            "finition": ["brillant"],
            "occasion": ["quotidien"],
            "couvrance": "légère",
            "couleur": ["rose"],
            "gamme_prix": "abordable"
        }
    ]

    extracted = {
        "zone": "lèvres",
        "texture": ["crémeux"],
        "finition": ["mat"],
        "occasion": ["soirée"],
        "couvrance": "forte",
        "couleur": ["rouge"],
        "gamme_prix": "luxe"
    }

    top_products = recommend_product(products, extracted, top_k=2)

    assert isinstance(top_products, list)
    assert isinstance(top_products[0], tuple)  # chaque élément = (score, produit)
    assert top_products[0][1]["nom"] == "Produit B"  # Produit B devrait être le mieux noté