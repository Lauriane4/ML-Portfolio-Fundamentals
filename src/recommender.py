def score_product(product, extracted):
    score = 0

    # Zone (prioritaire)
    if extracted["zone"] == product["zone"]:
        score += 2

    # Texture
    score += len(set(extracted["texture"]) & set(product["texture"]))

    # Finition
    score += len(set(extracted["finition"]) & set(product["finition"]))

    # Occasion
    score += len(set(extracted["occasion"]) & set(product["occasion"]))

    # Couleur (uniquement si le produit en a)
    if product["couleur"]:
        score += len(set(extracted["couleur"]) & set(product["couleur"]))

    # Couvrance
    if extracted["couvrance"] == product["couvrance"]:
        score += 1

    return score


def recommend_product(products, extracted):
    best_product = None
    best_score = -1

    for product in products:
        score = score_product(product, extracted)
        if score > best_score:
            best_score = score
            best_product = product

    return best_product, best_score
