from src.nlp import extract_attributes

def test_extract_zone_levres():
    text = "Je cherche un rouge à lèvres mat"
    extracted = extract_attributes(text)

    assert extracted["zone"] == "lèvres"

def test_extract_finition_mat():
    text = "Je veux un maquillage mat"
    extracted = extract_attributes(text)

    assert "mat" in extracted["finition"]

def test_extract_couleur_rouge():
    text = "Je cherche un rouge à lèvres rouge"
    extracted = extract_attributes(text)

    assert "rouge" in extracted["couleur"]

def test_extract_couvrance_forte1():
    text = "Je veux un produit très couvrant pour camoufler"
    extracted = extract_attributes(text)

    assert extracted["couvrance"] == "forte"


def test_extract_couvrance_forte2():
    text = "Je souhaite une couvrance forte pour mon fond de teint"
    extracted = extract_attributes(text)

    assert extracted["couvrance"] == "forte"

def test_extract_multiple_attributes():
    text = "Je cherche un rouge à lèvres liquide rouge pour une soirée"
    extracted = extract_attributes(text)

    assert extracted["zone"] == "lèvres"
    assert "liquide" in extracted["texture"]
    assert "rouge" in extracted["couleur"]
    assert "soirée" in extracted["occasion"]

def test_detect_couvrance_forte():
    text = "je veux une couvrance forte"
    extracted = extract_attributes(text)
    assert extracted["couvrance"] == "forte"

def test_detect_couvrance_legere():
    text = "effet naturel et discret"
    extracted = extract_attributes(text)
    assert extracted["couvrance"] == "légère"

def test_detect_couvrance_moyenne():
    text = "couvrance moyenne pour un effet équilibré"
    extracted = extract_attributes(text)
    assert extracted["couvrance"] == "moyenne"


def test_mixed_coouvrance_keywords():
    text = "Je veux un fond de teint avec couvrance moyenne mais très couvrant"
    extracted = extract_attributes(text)
    assert extracted["couvrance"] == "forte"

def test_gamme_prix_abordable():
    text = "Je cherche un produit pas cher et économique"
    extracted = extract_attributes(text)
    assert extracted["gamme_prix"] == "abordable"

def test_gamme_prix_luxe():
    text = "Je veux un produit de luxe et haut de gamme"
    extracted = extract_attributes(text)
    assert extracted["gamme_prix"] == "luxe"

def test_gamme_prix_moyenne():
    text = "Je cherche un produit de prix moyen et modéré."
    extracted = extract_attributes(text)
    assert extracted["gamme_prix"] == "moyenne"

def test_no_gamme_prix():
    text = "Je veux un rouge à lèvres rouge mat"
    extracted = extract_attributes(text)
    assert extracted["gamme_prix"] is None