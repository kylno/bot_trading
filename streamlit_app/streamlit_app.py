import streamlit as st
import pandas as pd
import uuid

st.set_page_config(page_title="Cockpit IA", layout="wide")

# Menu latéral
st.sidebar.title("🧭 Menu principal")
page = st.sidebar.radio("Navigation", [
    "Gestion des cerveaux",
    "Alertes & Historique",
    "État de santé du bot",
    "Centre de mission IA",
    "Cockpit IA",
    "Diagnostic global",
    "Pannes & Anomalies",
    "Valise Cockpit IA",
    "Génération d'ID",
    "Historique des activités",
    "Plateau cockpit IA",
    "Aperçu des animations cockpit IA",
    "Statistiques cockpit IA"
])

# ------------------ PAGE 1 : GESTION DES CERVEAUX ------------------
if page == "Gestion des cerveaux":
    st.title("🧠 Gestion des cerveaux")
    cerveaux = ["Cerveau Global", "Casa de Papel", "Berzerk Plus", "Microcap 1", "Microcap 2"]
    selected = st.selectbox("🧠 Choisis un cerveau :", cerveaux)

    st.subheader("📈 Volume")
    volume = st.slider("Seuil du volume (K)", 0, 10000, 5000, step=500)
    st.line_chart([volume * 0.8, volume, volume * 1.2])

    st.subheader("📉 Chute de prix (%)")
    drop = st.slider("Seuil de chute", 0, 100, 20, step=5)
    st.line_chart([drop * 0.5, drop, drop * 1.5])

    st.subheader("🔄 Rebond (%)")
    rebound = st.slider("Seuil de rebond", 0, 100, 15, step=5)
    st.line_chart([rebound * 0.5, rebound, rebound * 1.5])

    st.subheader("📊 Tendance globale (%)")
    trend = st.slider("Seuil de tendance", 0, 100, 10, step=5)
    st.line_chart([trend * 0.5, trend, trend * 1.5])

    col1, col2 = st.columns(2)
    with col1:
        if st.button("💾 Sauvegarder les paramètres"):
            st.success(f"Paramètres du cerveau '{selected}' sauvegardés.")
    with col2:
        if st.button("🔄 Relancer le cerveau"):
            st.warning(f"Cerveau '{selected}' relancé.")

# ------------------ PAGE 2 : ALERTES & HISTORIQUE ------------------
elif page == "Alertes & Historique":
    st.title("📊 Alertes & Historique")
    uploaded_file = st.file_uploader("Importer un fichier d'alertes :", type=["csv", "txt"])
    if uploaded_file:
        try:
            df = pd.read_csv(uploaded_file)
            st.success("Fichier importé avec succès.")
            st.dataframe(df)
        except Exception as e:
            st.error(f"Erreur : {e}")

    st.subheader("📜 Historique des alertes")
    alertes = [
        {"date": "2025-09-01", "type": "Telegram", "message": "Chute détectée sur BTC"},
        {"date": "2025-09-02", "type": "Système", "message": "Erreur API Binance"},
        {"date": "2025-09-03", "type": "Telegram", "message": "Rebond confirmé sur ETH"},
    ]
    for a in alertes:
        st.markdown(f"🕒 **{a['date']}** – *{a['type']}* : {a['message']}")

# ------------------ PAGE 3 : ÉTAT DE SANTÉ DU BOT ------------------
elif page == "État de santé du bot":
    st.title("❤️ État de santé du bot")
    st.metric("Uptime", "99.97%")
    st.metric("Erreurs critiques", "0")
    st.metric("Latence API", "320 ms")
    st.success("Tous les modules sont opérationnels.")

# ------------------ PAGE 4 : CENTRE DE MISSION IA ------------------
elif page == "Centre de mission IA":
    st.title("🎯 Centre de mission IA")
    st.markdown("Bienvenue dans ton centre de mission personnalisé.")
    missions = ["Améliorer les performances de ton IA", "Créer une campagne de remarketing"]
    for m in missions:
        st.checkbox(m)
    st.metric("Missions complétées", "12")
    st.metric("Niveau IA", "Expert")

# ------------------ PAGE 5 : COCKPIT IA ------------------
elif page == "Cockpit IA":
    st.title("🛠️ Cockpit IA – Configuration")
    st.toggle("Activer le diagnostic", value=True)
    st.selectbox("Mode de diagnostic :", ["Standard", "Avancé"])
    st.checkbox("Envoyer un email d’erreur")
    st.checkbox("Blocage des erreurs critiques")

# ------------------ PAGE 6 : DIAGNOSTIC GLOBAL ------------------
elif page == "Diagnostic global":
    st.title("🧪 Diagnostic global")
    st.progress(20)
    st.success("✅ Aucun module/API ne plante")
    st.progress(70)
    st.caption("Score cockpit IA = 0.0")
    st.download_button("📥 Télécharger le rapport", data="Rapport fictif", file_name="rapport.txt")

# ------------------ PAGE 7 : PANNES & ANOMALIES ------------------
elif page == "Pannes & Anomalies":
    st.title("⚠️ Pannes & Anomalies")
    st.success("✅ Aucun module défectueux")
    st.success("✅ Aucune API non connectée")
    st.success("🟢 Système stable – pas d'anomalie détectée")

# ------------------ PAGE 8 : VALISE COCKPIT IA ------------------
elif page == "Valise Cockpit IA":
    st.title("📘 Valise Cockpit IA – Export & Partage")
    col1, col2, col3 = st.columns(3)
    col1.button("📁 Exporter les données")
    col2.button("📁 Partager la valise")
    col3.button("📁 Historique des exports")
    st.image("https://api.qrserver.com/v1/create-qr-code/?data=ExportID12345&size=150x150", caption="QR Code export")

# ------------------ PAGE 9 : GÉNÉRATION D'ID ------------------
elif page == "Génération d'ID":
    st.title("🆔 Génération d’identifiants cockpit IA")
    new_id = str(uuid.uuid4())
    st.code(new_id)
    st.text("Historique :\nID-2025-09-03-001\nID-2025-09-03-002")

# ------------------ PAGE 10 : HISTORIQUE DES ACTIVITÉS ------------------
elif page == "Historique des activités":
    st.title("📘 Historique des activités cockpit IA")
    st.info("Aucune sauvegarde pour le moment")
    st.info("Aucun export enregistré pour le moment")

# ------------------ PAGE 11 : PLATEAU COCKPIT IA ------------------
elif page == "Plateau cockpit IA":
    st.title("🧭 Plateau cockpit IA – Coordination")
    st.info("Espace de visualisation stratégique en attente de données.")

# ------------------ PAGE 12 : APERÇU DES ANIMATIONS ------------------
elif page == "Aperçu des animations cockpit IA":
    st.title("🖼️ Aperçu des animations cockpit IA")
    st.warning("✅ Check (validation système) – Aucune ressource image trouvée")
    st.warning("❌ Error (panne détectée) – Aucune ressource image trouvée")
    st.warning("🚀 Succès cockpit – Aucune ressource image trouvée")
    st.warning("⏳ Loading – Aucune ressource image trouvée")

# ------------------ PAGE 13 : STATISTIQUES COCKPIT IA ------------------
elif page == "Statistiques cockpit IA":
    st.title("📈 Statistiques cockpit IA")
    st.line_chart([100, 200, 150, 300, 250])
    st.bar_chart([50, 80, 60, 90])
    
elif page == "État de santé du bot":
    st.title("❤️ État de santé du bot")

    st.subheader("📊 Indicateurs système")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Uptime", "99.97%", delta="+0.02%")
    with col2:
        st.metric("Erreurs critiques", "0", delta="-1")
    with col3:
        st.metric("Latence API", "320 ms", delta="-15 ms")

    st.markdown("---")
    st.subheader("📋 Modules actifs")
    modules = {
        "Binance API": True,
        "CoinMarketCap API": True,
        "Analyseur de tendance": True,
        "Détecteur de rebond": True,
        "Logger système": True
    }

    for name, status in modules.items():
        if status:
            st.success(f"✅ {name} : opérationnel")
        else:
            st.error(f"❌ {name} : en panne")

    st.markdown("---")
    st.subheader("🧠 Santé cognitive des cerveaux")
    st.progress(90)
    st.caption("Cerveaux IA stables et synchronisés")
    
elif page == "Centre de mission IA":
    st.title("🎯 Centre de mission IA")

    st.subheader("📋 Missions IA en cours")
    missions = {
        "Optimiser les performances du cerveau Global": False,
        "Analyser les signaux de rebond sur ETH": True,
        "Détecter les anomalies de volume sur BTC": False,
        "Synchroniser les modules API": True
    }

    for mission, status in missions.items():
        st.checkbox(mission, value=status)

    st.markdown("---")
    st.subheader("📈 Progression globale")
    progression = 75  # valeur fictive
    st.progress(progression)
    st.caption(f"Progression IA : {progression}%")

    st.subheader("🧠 Niveau IA")
    niveau = "Expert"
    st.success(f"Niveau actuel : {niveau}")

    st.markdown("---")
    st.subheader("🚀 Déclencher une mission")
    if st.button("Lancer une nouvelle mission IA"):
        st.info("Nouvelle mission lancée avec succès.")
        
elif page == "Cockpit IA":  
    st.title("🛠️ Cockpit IA – Configuration système")

    st.subheader("🔧 Paramètres de diagnostic")
    activer_diag = st.toggle("Activer le diagnostic automatique", value=True)
    mode_diag = st.selectbox("Mode de diagnostic :", ["Standard", "Avancé", "Personnalisé"])
    blocage_erreurs = st.checkbox("Blocage des erreurs critiques")
    envoi_email = st.checkbox("Envoyer un email en cas d’anomalie")

    st.markdown("---")
    st.subheader("📡 Surveillance des modules")
    modules = {
        "Logger système": True,
        "Synchroniseur API": True,
        "Détecteur de panne": False,
        "Analyseur de tendance": True
    }

    for nom, actif in modules.items():
        if actif:
            st.success(f"✅ {nom} : actif")
        else:
            st.error(f"❌ {nom} : inactif")

    st.markdown("---")
    st.subheader("⚙️ Actions système")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("💾 Sauvegarder la configuration"):
            st.success("Configuration sauvegardée avec succès.")
    with col2:
        if st.button("🔄 Réinitialiser le cockpit"):
            st.warning("Réinitialisation en cours...")   
            
elif page == "Diagnostic global":
    st.title("🧪 Diagnostic global du cockpit IA")

    st.subheader("📊 Score de stabilité")
    score = 87  # valeur fictive
    st.metric("Score cockpit IA", f"{score}/100", delta="+3")

    st.progress(score)
    st.caption("Analyse basée sur les modules, APIs et latence système.")

    st.markdown("---")
    st.subheader("🔍 Modules analysés")
    modules = {
        "Logger système": "OK",
        "Synchroniseur API": "OK",
        "Détecteur de panne": "OK",
        "Analyseur de tendance": "OK",
        "Exportateur CSV": "OK"
    }

    for nom, statut in modules.items():
        st.success(f"✅ {nom} : {statut}")

    st.markdown("---")
    st.subheader("📥 Rapport de diagnostic")
    rapport = "Diagnostic cockpit IA : tous les modules sont stables.\nScore : 87/100"
    st.download_button("📥 Télécharger le rapport", data=rapport, file_name="diagnostic_cockpit.txt")
    
elif page == "Pannes & Anomalies":
    st.title("⚠️ Pannes et anomalies détectées")

    st.subheader("🧩 Modules en erreur")
    modules_en_erreur = []
    if modules_en_erreur:
        for module in modules_en_erreur:
            st.error(f"❌ Module défectueux : {module}")
    else:
        st.success("✅ Aucun module défectueux")

    st.subheader("🔌 APIs non connectées")
    apis_non_connectees = []
    if apis_non_connectees:
        for api in apis_non_connectees:
            st.warning(f"⚠️ API non connectée : {api}")
    else:
        st.success("✅ Aucune API non connectée")

    st.subheader("📊 État global du cockpit IA")
    stable = True
    if stable:
        st.success("🟢 Système stable – tous les modules sont fonctionnels")
    else:
        st.error("🔴 Anomalies détectées – intervention requise")

    st.markdown("---")
    st.caption("📸 Capture d’écran enregistrée automatiquement")
    
elif page == "Valise Cockpit IA":
    st.title("📘 Valise Cockpit IA – Export & Partage")

    st.subheader("📦 Contenu de la valise IA")
    st.write("Modules actifs, paramètres sauvegardés, logs système, identifiants cockpit...")

    st.markdown("---")
    st.subheader("📤 Actions disponibles")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("📁 Exporter les données"):
            st.success("Export effectué avec succès.")
    with col2:
        if st.button("🔗 Partager la valise"):
            st.info("Lien de partage généré : https://cockpit.local/share/valise123")
    with col3:
        if st.button("📜 Historique des exports"):
            st.warning("Aucun export enregistré pour le moment.")

    st.markdown("---")
    st.subheader("📸 QR Code de la valise")
    st.image("https://api.qrserver.com/v1/create-qr-code/?data=ValiseIA123&size=150x150", caption="QR Code export")

    st.caption("📁 La valise IA contient les éléments essentiels pour redémarrer ou transférer le cockpit.")
    
elif page == "Génération d'ID":
    st.title("🆔 Génération d’identifiants cockpit IA")

    st.subheader("🔧 Générer un nouvel ID")
    new_id = str(uuid.uuid4())
    st.code(new_id, language="text")

    st.markdown("---")
    st.subheader("📋 Historique des ID générés")
    historique_ids = [
        "ID-2025-09-03-001",
        "ID-2025-09-03-002",
        "ID-2025-09-03-003"
    ]
    for id in historique_ids:
        st.markdown(f"🧾 {id}")

    st.markdown("---")
    st.subheader("📤 Exporter ou copier l’ID")
    col1, col2 = st.columns(2)
    with col1:
        st.button("📋 Copier dans le presse-papiers")
    with col2:
        st.button("📁 Exporter l’ID")
        
elif page == "Historique des activités":
    st.title("📘 Historique des activités cockpit IA")

    st.subheader("🗂️ Sauvegardes de configuration")
    sauvegardes = [
        {"date": "2025-08-30", "nom": "config_global_v1.json"},
        {"date": "2025-09-01", "nom": "config_microcap2.json"}
    ]
    if sauvegardes:
        for s in sauvegardes:
            st.markdown(f"📁 **{s['nom']}** – sauvegardé le *{s['date']}*")
    else:
        st.info("Aucune sauvegarde pour le moment.")

    st.markdown("---")
    st.subheader("📦 Exports de valise IA")
    exports = [
        {"date": "2025-09-02", "nom": "valise_BTC_export.zip"},
        {"date": "2025-09-03", "nom": "valise_ETH_export.zip"}
    ]
    if exports:
        for e in exports:
            st.markdown(f"📦 **{e['nom']}** – exporté le *{e['date']}*")
    else:
        st.info("Aucun export enregistré pour le moment.")

    st.markdown("---")
    st.subheader("📤 Actions")
    col1, col2 = st.columns(2)
    with col1:
        st.button("🔄 Restaurer une configuration")
    with col2:
        st.button("📁 Télécharger l’historique complet")
        
elif page == "Plateau cockpit IA":
    st.title("🧭 Plateau cockpit IA – Coordination & Déploiement")

    st.subheader("📍 Carte stratégique des modules")
    modules = {
        "Binance API": "Déployé",
        "Analyseur de tendance": "En attente",
        "Détecteur de rebond": "Déployé",
        "Logger système": "Déployé",
        "Synchroniseur Telegram": "Non déployé"
    }

    for nom, statut in modules.items():
        if statut == "Déployé":
            st.success(f"✅ {nom} : {statut}")
        elif statut == "En attente":
            st.warning(f"⏳ {nom} : {statut}")
        else:
            st.error(f"❌ {nom} : {statut}")

    st.markdown("---")
    st.subheader("🚀 Déploiement manuel")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 Déployer tous les modules"):
            st.success("Tous les modules ont été déployés.")
    with col2:
        if st.button("🧹 Nettoyer le plateau"):
            st.info("Plateau réinitialisé.")

    st.markdown("---")
    st.subheader("📡 Visualisation en temps réel")
    st.caption("Module JS en attente d’intégration pour affichage dynamique.")
    
elif page == "Aperçu des animations cockpit IA":
    st.title("🖼️ Aperçu des animations cockpit IA")

    st.subheader("✅ Check – Validation système")
    st.warning("⚠️ Aucune ressource image trouvée")
    st.caption("Statut : système validé, tous les modules sont synchronisés.")

    st.subheader("❌ Error – Panne détectée")
    st.warning("⚠️ Aucune ressource image trouvée")
    st.caption("Statut : erreur critique détectée dans le module de rebond.")

    st.subheader("🚀 Succès cockpit – Lancement réussi")
    st.warning("⚠️ Aucune ressource image trouvée")
    st.caption("Statut : tous les modules ont été déployés avec succès.")

    st.subheader("⏳ Loading – Animation d’attente")
    st.warning("⚠️ Aucune ressource image trouvée")
    st.caption("Statut : en attente de synchronisation des modules API.")

    st.markdown("---")
    st.button("🔄 Recharger les animations")
    
elif page == "Statistiques cockpit IA":
    st.title("📈 Statistiques cockpit IA")

    st.subheader("📊 Activité des modules")
    st.line_chart([120, 180, 150, 220, 190, 250])
    st.caption("Évolution du nombre d’actions par module sur les 6 derniers cycles.")

    st.subheader("📉 Taux d’erreur")
    st.bar_chart([5, 3, 2, 4, 1])
    st.caption("Nombre d’erreurs critiques par jour (dernière semaine).")

    st.subheader("📈 Tendance IA")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Tendance positive", "68%", delta="+12%")
    with col2:
        st.metric("Tendance négative", "32%", delta="-12%")

    st.markdown("---")
    st.subheader("📤 Export des statistiques")
    if st.button("📁 Télécharger les stats"):
        st.success("Statistiques exportées avec succès.")