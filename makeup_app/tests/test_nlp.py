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

def test_extract_type_produit():
    text = "Je cherche un fond de teint liquide"
    text2 = "Je veux un rouge à lèvres mat"
    text3 = "Je souhaite un mascara volumisant"
    text4 = "Je désire un eyeliner liquide"
    text5 = "Je veux un blush poudre lumineux"
    text6 = "Je cherche un crayon à sourcils fin"
    text7 = "Je souhaite une palette de fards colorée"
    text8 = "Je désire un spray fixant léger"

    extracted = extract_attributes(text)
    extracted2 = extract_attributes(text2)
    extracted3 = extract_attributes(text3)
    extracted4 = extract_attributes(text4)  
    extracted5 = extract_attributes(text5)
    extracted6 = extract_attributes(text6)
    extracted7 = extract_attributes(text7)
    extracted8 = extract_attributes(text8)

    assert extracted["type"] == "fond de teint"
    assert extracted2["type"] == "rouge à lèvres"
    assert extracted3["type"] == "mascara"
    assert extracted4["type"] == "eyeliner"
    assert extracted5["type"] == "blush"
    assert extracted6["type"] == "sourcils"
    assert extracted7["type"] == "palette"
    assert extracted8["type"] == "spray fixant"