import streamlit as st
import json
from src.nlp import extract_attributes
from src.recommender import recommend_product

# ----------------------------
# CONFIG PAGE
# ----------------------------
st.set_page_config(
    page_title="Makeup Recommendation",
    page_icon="💄",
    layout="wide"
)

st.title("💄 Makeup Recommendation App")
st.write(
    "Décrivez le produit de maquillage que vous recherchez "
    "(texture, couleur, zone du visage, occasion, etc.)"
)

# ----------------------------
# LOAD DATA
# ----------------------------
with open("data/makeup_dataset.json", "r", encoding="utf-8") as f:
    PRODUCTS = json.load(f)

# ----------------------------
# SESSION STATE
# ----------------------------
if "answered" not in st.session_state:
    st.session_state.answered = False

if "result" not in st.session_state:
    st.session_state.result = None

if "extracted" not in st.session_state:
    st.session_state.extracted = None

# ----------------------------
# INPUT USER
# ----------------------------
user_input = st.text_area(
    "Description",
    key="user_input",
    height=150,
    placeholder="Ex : Je cherche un rouge à lèvres mat rouge pour une soirée."
)

# ----------------------------
# CALLBACK RESET
# ----------------------------
def reset_app():
    st.session_state.answered = False
    st.session_state.user_input = ""
    st.session_state.result = None
    st.session_state.extracted = None

# ----------------------------
# BUTTON RECOMMENDER
# ----------------------------
if st.button("Recommander") and user_input.strip():
    st.session_state.extracted = extract_attributes(user_input)
    st.session_state.result = recommend_product(
        PRODUCTS,
        st.session_state.extracted
    )
    st.session_state.answered = True

# ----------------------------
# DISPLAY RESULT
# ----------------------------
if st.session_state.answered and st.session_state.result:
    product, score = st.session_state.result

    st.subheader("✨ Produit recommandé")

    st.markdown(f"""
    **{product['nom']}**  
    *{product['marque']}*  

    **Zone** : {product['zone']}  
    **Texture** : {", ".join(product['texture'])}  
    **Finition** : {", ".join(product['finition'])}  
    **Occasion** : {", ".join(product['occasion'])}  
    **Couvrance** : {product['couvrance']}  
    **Couleurs** : {", ".join(product['couleur']) if product['couleur'] else "—"}  
    **Gamme de prix** : {product['gamme_prix']}
    """)

    if st.checkbox("Afficher le debug NLP"):
        st.json(st.session_state.extracted)

    st.button("Réinitialiser", on_click=reset_app)
