import re

#Dictionnaire de mots-clés pour le maquillage
ZONES = {
    "visage": ["visage", "teint", "fond de teint", "base", "bb crème", "cc crème"],
    "lèvres": ["lèvres", "rouge à lèvres", "gloss", "lipstick", "lip", "lip gloss", "lip balm"],
    "joues": ["joues", "blush", "fard à joues", "highlighter", "illuminateur", "contour", "bronzer", "sculpter", "contouring"],
    "yeux": ["yeux", "paupières", "fards", "palette", "eyeliner", "mascara", "cils", "sourcils", "brows", "ombre à paupières", "eyeshadow"]
}

TYPES = {
    "fond de teint": ["fond de teint", "base", "bb crème", "cc crème"],
    "rouge à lèvres": ["rouge à lèvres", "lipstick", "RAL"],
    "gloss": ["gloss", "lip gloss"],
    "blush": ["blush", "fard à joues"],
    "highlighter": ["highlighter", "illuminateur"],
    "eyeliner": ["eyeliner", "crayon yeux"],
    "mascara": ["mascara", "cils"],
    "palette": ["palette", "fards à paupières", "eyeshadow palette", "eye shadow"],
    "sourcils": ["sourcils", "brows", "crayon sourcils"],
    "bronzer": ["bronzer", "poudre bronzante"],
    "base": ["base", "primer"],
    "spray fixant": ["spray fixant", "fixateur de maquillage"]
}

TEXTURES = {
    "liquide": ["liquide", "fluide"],
    "crémeux": ["crémeux", "crème"],
    "poudre": ["poudre", "compact", "minérale"],
    "gel": ["gel", "gélifié"],
}

FINITION = {
    "mat": ["mat", "mate", "sans brillance", "velouté", "veloutée"],
    "brillant": ["brillant", "glossy", "lustré", "lustrée", "shiny", "scintillant", "scintillante", "irisé", "irisée","satiné", "satinée"],
    "lumineux": ["lumineux", "éclat", "glowy", "radieux", "radieuse", "illuminé", "illuminée", "glow"]
}

OCCASION = {
    "mariage": ["mariage", "noces", "cérémonie", "bridal", "wedding"],
    "professionnel": ["travail", "professionnel", "bureau", "réunion", "interview", "job"],
    "soirée": ["soirée", "nuit", "fête", "party", "événement"],
    "quotidien": ["quotidien", "tous les jours", "décontracté", "casual", "everyday"]
}

COULEURS = [
    "rouge", "rose", "nude", "bordeaux", "corail",
    "marron", "doré", "cuivré", "violet", "transparent", "pêche", "mauve",
    "framboise", "prune", "abricot", "fuchsia", "magenta", "cerise", "grenat",
    "saumon", "terracotta", "champagne", "bronze", "argenté", "platine", "bleu",
    "vert", "turquoise", "émeraude", "jaune", "orange", "lavande", "indigo","vert", "noir","blanc", "gris"
]

INTENTION_COUVRANCE = { # Mots-clés associés à chaque niveau de couvrance du plus fort au plus léger
    "forte": ["camoufler", "opaque", "couvrant", "très couvrant", "forte couvrance", "haute couvrance", "couvrance maximale", "couvrance forte"],
    "moyenne": ["uniforme", "équilibré", "moyenne couvrance", "couvrance moyenne", "modérée", "couvrance modérée", "couvrance normale", "normale", "standard", "couvrance standard"],
    "légère": ["léger", "discret", "naturel", "légère couvrance", "couvrance légère", "faible", "couvrance faible"]
}

GAMME_PRIX = {
    "abordable": [
        "pas cher", "bas prix", "petit prix", "cheap",
        "bon marché", "low cost", "discount",
        "budget", "budget-friendly", "peu coûteux", "économique"
    ],
    "moyenne": [
        "prix moyen", "milieu de gamme", "intermédiaire",
        "modéré", "standard", "mid-range", "mid tier"
    ],
    "luxe": [
        "luxe", "haut de gamme", "premium", "très cher"
    ]
}

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    return text


def extract_attributes(text):
    text = clean_text(text)

    extracted = {
        "zone": None,
        "type": None,
        "texture": [],
        "finition": [],
        "occasion": [],
        "couleur": [],
        "couvrance": None,
        "gamme_prix": None
    }

    # -----------------------------
    # Zone du visage (une seule)
    # -----------------------------
    for zone, keywords in ZONES.items():
        if any(word in text for word in keywords):
            extracted["zone"] = zone
            break

    # -----------------------------
    # Type de produit (un seul)
    # -----------------------------
    for type_produit, keywords in TYPES.items():
        if any(word in text for word in keywords):
            extracted["type"] = type_produit
            break

    # -----------------------------
    # Textures (plusieurs possibles)
    # -----------------------------
    for texture, keywords in TEXTURES.items():
        if any(word in text for word in keywords):
            extracted["texture"].append(texture)

    # -----------------------------
    # Finition (plusieurs possibles)
    # -----------------------------
    for finition, keywords in FINITION.items():
        if any(word in text for word in keywords):
            extracted["finition"].append(finition)

    # -----------------------------
    # Occasion (plusieurs possibles)
    # -----------------------------
    for occasion, keywords in OCCASION.items():
        if any(word in text for word in keywords):
            extracted["occasion"].append(occasion)

    # -----------------------------
    # Couleurs (liste simple)
    # -----------------------------
    for couleur in COULEURS:
        if couleur in text:
            extracted["couleur"].append(couleur)

    # -----------------------------
    # Couvrance (intention priorisée)
    # -----------------------------
    for couvrance, keywords in INTENTION_COUVRANCE.items():
        if any(word in text for word in keywords):
            extracted["couvrance"] = couvrance
            break
    # -----------------------------
    # Gamme de prix (intention priorisée)
    for gamme_prix, keywords in GAMME_PRIX.items():
        if any(word in text for word in keywords):
            extracted["gamme_prix"] = gamme_prix
            break

    return extracted
