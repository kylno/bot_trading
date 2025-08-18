# 🧭 Architecture du Cockpit IA — KylianBot

Ce système est conçu pour surveiller, scorer et déclencher des actions sur des alertes financières en temps réel. Il est piloté par une IA adaptative, auditable et sécurisée.

## 📦 Modules principaux

- `core/` : scoring, déclenchement, utilitaires  
- `routines/` : scripts automatisés (matin, soir, hebdo)  
- `streamlit_app/` : interfaces de contrôle et visualisation  
- `meta/` : surveillance comportementale de l’IA  
- `config/` : configuration horaire et comportementale  
- `logs/` : journalisation des événements, audits, seuils

## 🔁 Flux de données

1. Collecte des alertes  
2. Scoring IA  
3. Déclenchement des bots  
4. Journalisation  
5. Visualisation + audit
