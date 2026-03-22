import streamlit as st
import joblib

# config
st.set_page_config(page_title="CVRIE - Redirection en fonction des symptomes", page_icon="🏥", layout="centered")

# model loading
@st.cache_resource
def load_models():
    vectoriseur = joblib.load('vectoriseur_kmeans.pkl')
    svd = joblib.load('svd_kmeans.pkl')
    kmeans = joblib.load('kmeans_cvrie.pkl')
    return vectoriseur, svd, kmeans

vectoriseur, svd, kmeans = load_models()

SERVICES_HOPITAL = {
    0: "💪 Service Orthopédique - (Douleurs membres supérieurs)",
    1: "🦵 Service Orthopédique - (Douleurs membres inférieurs)",
    2: "🩸 Service Diabétologie / Endocrinologie",
    3: "🫀 Service Cardiologie / Unité de Syncope / Hypotension",
    4: "👂 Service ORL (Infection de l'oreille)",
    5: "🔥 Service Dermatologie (Inflammation/Brûlure)",
    6: "🩺 Service Médecine Générale (Rhume/Infection virale)",
    7: "🧠 Service Neurologie (Migraines)",
    8: "🚨 Urgences Respiratoires / Asthme",
    9: "🤧 Service Allergologie / Dermatologie"
}

# form of the page
st.title("CVRIE - (model K-Means)")
st.write("Décrivez vos symptômes ci-dessous (en anglais). L'algorithme CVRIE vous orientera.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if user_input := st.chat_input("I have a sharp pain in my shoulder when lifting..."):
    
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # 1. Clean
    input_tfidf = vectoriseur.transform([user_input])
    input_svd = svd.transform(input_tfidf)
    # 2. Prediction (K-Means find the nearest center)
    prediction = kmeans.predict(input_svd)[0]
    
    service_recommande = SERVICES_HOPITAL.get(prediction, "Service d'Accueil Général")
    
    bot_response = f"**Analyse de notre IA CVRIE :** D'après vos symptômes, je vous recommande de vous diriger vers le **{service_recommande}**."
    
    with st.chat_message("assistant"):
        st.markdown(bot_response)
    st.session_state.messages.append({"role": "assistant", "content": bot_response})