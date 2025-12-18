import re

#Dictionnaire de mots-clés pour le maquillage
ZONES = {
    "visage": ["visage", "teint", "fond de teint", "base"],
    "lèvres": ["lèvres", "rouge à lèvres", "gloss"],
    "joues": ["joues", "blush"],
    "yeux": ["yeux", "paupières", "fards", "palette"]
}

TEXTURES = ["crémeux", "liquide", "poudre"]
FINITIONS = ["mat", "brillant", "lumineux"]
OCCASIONS = ["quotidien", "soirée", "professionnel", "mariage"]

COULEURS = [
    "rouge", "rose", "nude", "bordeaux", "corail",
    "marron", "doré", "cuivré", "violet", "transparent", "pêche"
]

INTENTION_COUVRANCE = {
    "légère": ["léger", "discret", "naturel"],
    "moyenne": ["uniforme", "équilibré"],
    "forte": ["camoufler", "opaque", "couvrant"]
}

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    return text


def extract_attributes(text):
    text = clean_text(text)

    extracted = {
        "zone": None,
        "texture": [],
        "finition": [],
        "occasion": [],
        "couleur": [],
        "couvrance": None
    }

    # Zone du visage
    for zone, keywords in ZONES.items():
        if any(word in text for word in keywords):
            extracted["zone"] = zone
            break

    # Textures
    for texture in TEXTURES:
        if texture in text:
            extracted["texture"].append(texture)

    # Finitions
    for finition in FINITIONS:
        if finition in text:
            extracted["finition"].append(finition)

    # Occasions
    for occasion in OCCASIONS:
        if occasion in text:
            extracted["occasion"].append(occasion)

    # Couleurs
    for couleur in COULEURS:
        if couleur in text:
            extracted["couleur"].append(couleur)

    # Couvrance (via intention)
    for couvrance, keywords in INTENTION_COUVRANCE.items():
        if any(word in text for word in keywords):
            extracted["couvrance"] = couvrance
            break

    return extracted