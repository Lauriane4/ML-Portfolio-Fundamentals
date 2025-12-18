from src.recommender import score_product, recommend_product

def test_score_product_match():
    product = {
        "zone": "lèvres",
        "texture": ["crémeux"],
        "finition": ["mat"],
        "occasion": ["soirée"],
        "couvrance": "forte",
        "couleur": ["rouge"]
    }

    extracted = {
        "zone": "lèvres",
        "texture": ["crémeux"],
        "finition": ["mat"],
        "occasion": ["soirée"],
        "couvrance": "forte",
        "couleur": ["rouge"]
    }

    score = score_product(product, extracted)

    assert score > 0


def test_recommend_product():
    products = [
        {
            "nom": "Produit A",
            "zone": "visage",
            "texture": ["liquide"],
            "finition": ["mat"],
            "occasion": ["quotidien"],
            "couvrance": "moyenne",
            "couleur": []
        },
        {
            "nom": "Produit B",
            "zone": "lèvres",
            "texture": ["crémeux"],
            "finition": ["mat"],
            "occasion": ["soirée"],
            "couvrance": "forte",
            "couleur": ["rouge"]
        }
    ]

    extracted = {
        "zone": "lèvres",
        "texture": ["crémeux"],
        "finition": ["mat"],
        "occasion": ["soirée"],
        "couvrance": "forte",
        "couleur": ["rouge"]
    }

    product, score = recommend_product(products, extracted)

    assert product["nom"] == "Produit B"
