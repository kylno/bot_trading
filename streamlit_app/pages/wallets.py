import streamlit as st

st.set_page_config(page_title="Simulation Financière", layout="wide")

page = st.sidebar.radio("📂 Navigation", ["Dashboard", "Wallets"])

if page == "Dashboard":
    st.title("🧠 Dashboard de Simulation Financière")

    col_main, col_right = st.columns([2, 1])

    with col_right:
        st.markdown("### 💰 Capital de départ")
        st.write(f"{st.session_state.capital} €")

        st.markdown("### 📊 Bénéfices / Pertes par cerveau")
        for nom, valeur in st.session_state.cerveaux.items():
            couleur = "green" if valeur >= 0 else "red"
            st.markdown(f"<span style='color:{couleur}'>{nom} : {valeur} €</span>", unsafe_allow_html=True)

            col_plus, col_moins = st.columns(2)
            with col_plus:
                if st.button(f"➕ Ajouter 100 à {nom}"):
                    st.session_state.cerveaux[nom] += 100
            with col_moins:
                if st.button(f"➖ Retirer 100 à {nom}"):
                    st.session_state.cerveaux[nom] -= 100

    st.markdown("---")

    col_gauche, col_droite = st.columns([2, 1])
    with col_droite:
        st.markdown("### 🧳 Portefeuille de secours")
        for actif, montant in st.session_state.secours.items():
            st.write(f"{actif} : {montant} €")

            col_add, col_sub = st.columns(2)
            with col_add:
                if st.button(f"➕ Ajouter 50 à {actif}"):
                    st.session_state.secours[actif] += 50
            with col_sub:
                if st.button(f"➖ Retirer 50 à {actif}"):
                    st.session_state.secours[actif] -= 50

elif page == "Wallets":
    st.title("🧳 Wallets")

    wallets = {
        "Wallet Global": {"investi": 20000, "perte": 1500, "gain": 3000},
        "Wallet Casa de papel": {"investi": 15000, "perte": 800, "gain": 2000},
        "Wallet berzerk+": {"investi": 10000, "perte": 1200, "gain": 1500},
        "Wallet Micro Cap 1": {"investi": 15000, "perte": 800, "gain": 2000},
        "Wallet Micro Cap 2": {"investi": 10000, "perte": 1200, "gain": 1500},
    }

    for nom, data in wallets.items():
        with st.container():
            st.markdown(f"### {nom}")
            col1, col2, col3 = st.columns(3)
            col1.metric("💰 Capital investi", f"{data['investi']} €")
            col2.metric("📉 Perte", f"{data['perte']} €", delta=f"-{data['perte']} €")
            col3.metric("📈 Gain", f"{data['gain']} €", delta=f"+{data['gain']} €")
            
if "capital" not in st.session_state:
    st.session_state.capital = 10000

if "cerveaux" not in st.session_state:
    st.session_state.cerveaux = {
        "Cerveau A": 500,
        "Cerveau B": -200,
        "Cerveau C": 0,
    }

if "secours" not in st.session_state:
    st.session_state.secours = {
        "Crypto": 300,
        "Actions": 700,
        "Or": 500,
    }