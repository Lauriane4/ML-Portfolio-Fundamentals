import streamlit as st

st.set_page_config(page_title="Makeup Recommendation", page_icon="💄", layout="wide")
st.title("💄 Makeup Recommendation App")
st.write("Décrivez le produit de maquillage que vous recherchez (texture, couleur, zone du visage, occasion, etc.), et nous vous aiderons à le trouver !")


#Zone de saisie utilisateur
user_input=st.text_area("Description",key="user_input", height=150, placeholder="Ex : Je cherche un rouge à lèvres mat de couleur rouge vif pour une soirée spéciale.")

#Etat pour afficher les résultats
if "answered" not in st.session_state:
    st.session_state.answered = False

if "user_input" not in st.session_state:
    st.session_state.user_input = ""

# Fonction de réinitialisation (CALLBACK)
def reset_app():
    st.session_state.answered = False
    st.session_state.user_input = ""

# Bouton recommander
if st.button("Recommander") and user_input.strip() != "":
    st.session_state.answered = True

# Affichage des résultats
if st.session_state.answered:
    with st.spinner("Recherche des recommandations..."):
        # Simuler une recherche de recommandations
        import time
        time.sleep(2)  # Simuler un délai de traitement

        # Afficher les recommandations (exemples fictifs)
        st.subheader("Recommandations de produits de maquillage :")
        st.markdown("""
        1. **Rouge à lèvres mat "Rouge Passion"** - Couleur rouge vif, texture mate, parfait pour les soirées spéciales.
        2. **Fond de teint "Lisse et Lumineux"** - Texture légère, couvrance moyenne, idéal pour un look naturel.
        3. **Palette d'ombres à paupières "Nuit Étoilée"** - Couleurs riches et pigmentées, parfaites pour un maquillage de soirée.
        """)

        # Bouton réinitialiser
        st.button("Réinitialiser", on_click=reset_app)