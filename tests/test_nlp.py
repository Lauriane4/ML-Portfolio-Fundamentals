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