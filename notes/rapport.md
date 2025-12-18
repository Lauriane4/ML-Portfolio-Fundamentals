# Observations et Justification – Projet Makeup Recommendation

(17/12/2025)
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


(18/12/2025)
## 7. Analyse du texte et extraction des attributs (NLP)

Afin de transformer une description textuelle libre en informations exploitables par le système de recommandation, j’ai mis en place une première approche de traitement automatique du langage naturel basée sur des règles. Cette approche constitue une baseline NLP simple, interprétable et adaptée à un projet de première implémentation.

### 7.1 Approche rule-based NLP (baseline)

Le système repose sur des dictionnaires de mots-clés associés à des catégories prédéfinies telles que la zone du visage, la texture, la finition, l’occasion, la couleur et la couvrance. L’objectif est d’identifier dans le texte utilisateur la présence de certains termes afin d’en déduire les attributs recherchés.

Cette approche est dite *rule-based* car elle ne fait pas appel à un modèle statistique ou à un apprentissage automatique, mais à des règles explicites définies manuellement. Elle permet une compréhension claire du fonctionnement du système et facilite le débogage.

---

### 7.2 Nettoyage du texte

Avant toute analyse, le texte fourni par l’utilisateur est nettoyé :
- conversion en minuscules afin d’éviter les erreurs liées à la casse,
- suppression de la ponctuation et des caractères spéciaux.

Cette étape est essentielle pour garantir la cohérence des comparaisons entre le texte et les mots-clés définis.

---

### 7.3 Extraction des attributs

À partir du texte nettoyé, les attributs suivants sont extraits :

- **Zone du visage** : visage, lèvres, joues, yeux  
- **Texture** : crémeux, liquide, poudre  
- **Finition** : mat, brillant, lumineux  
- **Occasion** : quotidien, soirée, professionnel, mariage  
- **Couleur** : uniquement pour les produits décoratifs  
- **Couvrance** : déduite à partir de l’intention de l’utilisateur  

La zone du visage est déterminée en priorité, car elle constitue une information discriminante majeure pour la recommandation.

---

### 7.4 Gestion de l’intention utilisateur et de la couvrance

L’utilisateur n’exprime pas toujours directement la couvrance souhaitée. Il utilise plutôt des termes subjectifs tels que « naturel », « camoufler » ou « discret ». Ces termes sont interprétés comme des intentions et mappés vers une valeur de couvrance :

- naturel, discret → couvrance légère  
- uniforme → couvrance moyenne  
- camoufler, opaque → couvrance forte  

Ce choix permet de transformer une information qualitative en une variable exploitable par le système.

---

## 8. Système de recommandation par scoring

Une fois les attributs extraits, chaque produit de la base de données est comparé à la description utilisateur à l’aide d’un système de scoring.

### 8.1 Principe du scoring

Chaque produit reçoit un score calculé à partir des correspondances entre ses attributs et ceux extraits du texte utilisateur :

- correspondance de la zone du visage : poids élevé  
- correspondance des textures, finitions et occasions : +1 par match  
- correspondance de la couleur (si applicable)  
- correspondance de la couvrance  

Le produit ayant le score le plus élevé est recommandé à l’utilisateur.

---

### 8.2 Feature matching

Cette méthode repose sur le *feature matching*, c’est-à-dire la comparaison directe entre les caractéristiques extraites du texte et celles des produits. Chaque correspondance augmente le score du produit, ce qui permet de quantifier la pertinence de la recommandation.

Cette approche est simple, efficace et parfaitement interprétable, ce qui en fait un bon choix pour une première version du système.

---

## 9. Limites et perspectives d’amélioration

L’approche rule-based présente certaines limites, notamment sa dépendance aux mots-clés définis manuellement et sa difficulté à gérer des formulations complexes ou implicites.

### 9.1 TF-IDF

Une amélioration possible serait l’utilisation de la méthode TF-IDF (Term Frequency – Inverse Document Frequency), qui permet de représenter les textes sous forme de vecteurs numériques en fonction de l’importance des mots. Cette approche permettrait une comparaison plus automatique des descriptions utilisateur et des descriptions produits.

Cependant, TF-IDF reste sensible au vocabulaire exact utilisé et ne capture pas pleinement le sens des mots.

---

### 9.2 Embeddings

Une approche plus avancée consisterait à utiliser des embeddings de mots ou de phrases, qui représentent le texte dans un espace vectoriel sémantique. Cette méthode permettrait de reconnaître des synonymes ou des formulations proches (par exemple « camoufler » et « couvrant »), améliorant ainsi la qualité des recommandations.

Cette solution est envisagée comme une amélioration future du projet.

---

## 10. Conclusion intermédiaire

La mise en place d’une baseline NLP rule-based associée à un système de recommandation par scoring constitue une première version fonctionnelle, compréhensible et évolutive du système. Elle permet de valider la structure des données, la logique de recommandation et le comportement global de l’application avant l’intégration de modèles plus complexes.

## Tests unitaires

J'ai ajouté un premier lot de tests unitaires simples pour valider mon modèle.

Les tests unitaires ont permis d’identifier certaines limites de l’approche rule-based, notamment dans l’interprétation de la couvrance. Un premier ensemble de règles ne permettait pas de détecter explicitement des formulations telles que « couvrance forte ». L’ajout de mots-clés supplémentaires a permis d’améliorer la robustesse du système face à des variations linguistiques tout en conservant une approche interprétable.

La fonction d’extraction des attributs a été refactorisée afin d’exploiter pleinement les dictionnaires de mots-clés définis pour chaque catégorie. Chaque attribut est détecté à partir d’une liste de synonymes, ce qui permet de mieux prendre en compte la diversité des formulations utilisateur. Les couleurs constituent une exception volontaire, étant traitées comme des mots-clés directs.


## 11. Changements et améliorations du système de recommandation

### 11.1 Problème initial

Lors de nos premiers tests, le système de recommandation ne prenait en compte qu’un seul produit à la fois et ne considérait pas certains critères essentiels pour l’utilisateur, comme la **gamme de prix**.  

Exemple avec le prompt : "Je cherche une palette verte et bleue à bas prix"


Le système renvoyait les produits suivants :

1. Palette Naked Heat - Urban Decay  
   Score : 2  
   Zone : yeux  
   Texture : poudre  
   Finition : mat, lumineux  
   Couleurs : marron, cuivré, doré  
   Gamme de prix : moyenne  

2. Mini Eyeshadow Palette - Huda Beauty  
   Score : 2  
   Zone : yeux  
   Texture : poudre  
   Finition : mat, brillant  
   Couleurs : violet, rose, doré  
   Gamme de prix : moyenne  

… et ainsi de suite pour 6 produits.  

Problème constaté :  

- Le score était très bas (2) et ne reflétait pas correctement la pertinence par rapport à la description de l’utilisateur (vert et bleu, bas prix).  
- Les critères de **prix** n’étaient pas pris en compte dans le scoring.  
- Les recommandations étaient peu pertinentes, et le modèle ne priorisait pas correctement les produits correspondant aux couleurs demandées.

---

### 11.2 Changements apportés

#### a. Ajout de la **gamme de prix** dans le scoring

- Chaque produit dispose désormais d’un attribut `gamme_prix` : `abordable`, `moyenne`, `luxe`.  
- Le score est augmenté si la gamme de prix correspond à la demande implicite ou explicite de l’utilisateur.  
- Cela permet de mieux prioriser les produits en fonction du budget.

#### b. Passage à un système **top-N produits**

- Au lieu de renvoyer un seul produit, le recommender retourne désormais les **6 meilleurs produits** triés par score décroissant.  
- Chaque produit conserve son score pour transparence et debug.

#### c. Séparation du scoring produit et du recommender

- Fonction `score_single_product(product, extracted)` pour scorer un produit individuel.  
- Fonction `recommend_products(products, extracted, top_k=6)` pour obtenir le top 6 des produits.  
- Cela évite les erreurs de type `int object is not subscriptable` et rend le code plus clair.

---

#### d. Nouveau scoring pondéré

Le scoring a été modifié pour donner plus de poids aux critères essentiels.

Changements clés :

- Zone : priorité maximale (+5) car c’est le critère principal.

- Couleur : pondération triple (*3) pour bien valoriser les produits correspondant à la couleur demandée.

- Couvrance : pondération intermédiaire (+2).

- Gamme de prix : pondération importante (+3) pour mieux refléter la préférence budget de l’utilisateur.

- Les autres attributs (texture, finition, occasion) sont cumulés normalement (+1 par correspondance).

### 11.3 Résultats après changements

Prompt utilisateur : "Je cherche une palette verte et bleue à bas prix"


Nouveau résultat :

1. **Lash Sensational Mascara** - Maybelline  
   Score : 8  
   Zone : yeux  
   Texture : crémeux  
   Finition : naturel  
   Occasion : quotidien  
   Couleurs : noir  
   Gamme de prix : abordable  

2. **Palette Naked Heat** - Urban Decay  
   Score : 5  
   Zone : yeux  
   Texture : poudre  
   Finition : mat, lumineux  
   Occasion : quotidien, soirée  
   Couleurs : marron, cuivré, doré  
   Gamme de prix : moyenne  

3. **Mini Eyeshadow Palette** - Huda Beauty  
   Score : 5  
   Zone : yeux  
   Texture : poudre  
   Finition : mat, brillant  
   Occasion : soirée  
   Couleurs : violet, rose, doré  
   Gamme de prix : moyenne  

> On constate une meilleure adéquation entre le **score** et la pertinence pour l’utilisateur, notamment grâce à la prise en compte de la **gamme de prix** et au système **top-N**.

---


