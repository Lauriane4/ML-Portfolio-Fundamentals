# Scorer un produit unique
def score_single_product(product, extracted):
    score = 0

    # Zone (prioritaire)
    if extracted["zone"] == product["zone"]:
        score += 5

    # Type de produit (prioritaire)
    if extracted["type"] == product["type"]:
        score += 5

    # Texture
    score += len(set(extracted["texture"]) & set(product["texture"]))

    # Finition
    score += len(set(extracted["finition"]) & set(product["finition"]))

    # Occasion
    score += len(set(extracted["occasion"]) & set(product["occasion"]))

    # Couleur
    if product["couleur"]:
        score += 3*len(set(extracted["couleur"]) & set(product["couleur"]))

    # Couvrance
    if extracted["couvrance"] == product["couvrance"]:
        score += 2

    # Gamme de prix
    if extracted["gamme_prix"] == product["gamme_prix"]:
        score += 3

    return score

# Recommender top N
def recommend_product(products, extracted, top_k=3):
    scored_products = []

    for product in products:
        score = score_single_product(product, extracted)
        scored_products.append((score, product))

    # Trier par score décroissant
    scored_products.sort(key=lambda x: x[0], reverse=True)

    # Retourner top_k
    return scored_products[:top_k]
