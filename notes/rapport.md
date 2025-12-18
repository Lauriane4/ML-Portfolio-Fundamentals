# Observations et Justification – Projet Makeup Recommendation

## 1. Objectif du projet
L'objectif est de créer une application capable de recommander des produits de maquillage à partir d'une description textuelle fournie par l'utilisateur. L'application doit comprendre les intentions utilisateur, extraire les informations clés (zone du visage, type de produit, texture, finition, occasion, couleur, etc.) et fournir une recommandation adaptée.

---

## 2. Choix de conception

### 2.1 Interface utilisateur
- Utilisation de **Streamlit** pour créer l'interface.  
- `st.session_state` est utilisé pour mémoriser l'état de l'application et gérer l'affichage unique des recommandations.  
- Bouton **Réinitialiser** lié à un **callback** pour remettre à zéro l'interface et vider le champ texte de l'utilisateur.  
- Justification : Streamlit permet un prototypage rapide et une interactivité simple, tout en restant compatible avec des projets ML.

### 2.2 Base de données
- Utilisation d'un **fichier JSON** pour stocker les produits.  
- Justification :
  - Gestion des attributs multi-valeurs (couleur, texture, occasion).  
  - Facile à lire et à maintenir.  
  - Compatible avec le moteur de recommandation et le scoring basé sur NLP.  

### 2.3 Choix des attributs
- **Textures** : crémeux, liquide, poudre  
- **Finition** : mat, brillant, lumineux  
- **Occasion** : quotidien, soirée, professionnel, mariage  
- **Format** : stick, palette, flacon, pot  
- **Couvrance** : légère, moyenne, forte  
- **Gamme de prix** : abordable, moyenne, luxe  
- **Couleur** : utilisée uniquement pour les produits décoratifs (rouge, rose, nude, marron, doré, cuivré, violet, corail, transparent).  
- **Zones du visage** : visage, lèvres, joues, yeux

### 2.4 Gestion spécifique des couleurs
- Pour les produits de teint (fond de teint, anticernes), la couleur n'est pas utilisée comme feature, car il s'agit de gammes de teintes et non de couleurs expressives.  
- Pour les produits décoratifs (rouge à lèvres, gloss, palettes, blush), la couleur est une caractéristique clé pour la recommandation.  
- Les palettes avec plusieurs couleurs incluent toutes les couleurs disponibles dans l'attribut `couleur`.  

### 2.5 Couvrance et intentions utilisateur
- L’attribut **“naturel”” a été supprimé comme finition**, car il représente une intention plutôt qu’une propriété physique du produit.  
- Les mots-clés de l’utilisateur (naturel, camoufler, opaque, discret, uniforme) seront utilisés pour mapper l’intention vers la **couvrance** :  
  - naturel / discret → légère  
  - camoufler / opaque → forte  
  - uniforme → moyenne

---

## 3. Dataset test
- Création d’un dataset test de 5 produits couvrant toutes les zones du visage.  
- Les produits choisis sont représentatifs de différentes marques tendances et incluent diverses textures, occasions, finitions, formats et couleurs (quand pertinentes).  
- Exemple :  
```json
{
  "id": 2,
  "nom": "Lipstick Rouge Allure",
  "marque": "Chanel",
  "zone": "lèvres",
  "type": "rouge à lèvres",
  "texture": ["crémeux"],
  "finition": ["lumineux"],
  "occasion": ["soirée", "mariage"],
  "couvrance": "moyenne",
  "format": "stick",
  "gamme_prix": "luxe",
  "couleur": ["rouge"],
  "description": "Rouge à lèvres crémeux offrant confort et éclat intense.",
  "image": ""
}
```
## 4.Problèmes rencontrés et ajustements

- Ambiguïté du terme “naturel” : il ne correspond pas à une finition physique → solution : suppression de "naturel" de la liste des finitions et utilisation des mots-clés utilisateur pour déterminer la couvrance.

- Changement de certains attributs pour plus de cohérence :

    - Finition : conservé uniquement mat, brillant, lumineux

    - Format : clarifié pour différencier la texture du packaging (stick, palette, flacon, pot)

    - Couleur : appliquée uniquement pour les produits décoratifs, ignorée pour les fonds de teint et anticernes

- Gestion des états dans Streamlit : nécessité d’utiliser st.session_state et callbacks pour réinitialiser correctement les champs et les résultats.


## 5. Justification des choix

- JSON : structure flexible, facile à maintenir et adaptée au ML.
 
- Streamlit : prototypage rapide et contrôle de l’état utilisateur.

- Attributs produits : sélectionnés pour maximiser la pertinence des recommandations et la compatibilité avec un moteur de scoring basé sur NLP.

- Mapping intention → couvrance : permet de transformer les descriptions subjectives de l’utilisateur en attributs quantifiables.

- Gestion couleur : différenciation intelligente entre produits de teint et produits décoratifs, assurant la cohérence des recommandations.

## 6. Améliorations futures

- Ajouter un vrai moteur NLP (TF-IDF, embeddings, ou modèles pré-entraînés) pour calculer la similarité texte-produit.

- Gérer les teintes de peau pour les fonds de teint.

- Recommandations multiples avec scoring et pondération selon la correspondance.

- Extension du dataset à 50 produits minimum avec toutes les marques prévues.

- Export Markdown ou PDF automatisé pour le rapport final.