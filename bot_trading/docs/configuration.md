# ⚙️ Configuration IA — `config/config_ia.json`

Ce fichier pilote le comportement de l’IA selon l’heure et le mode choisi.

## 🕒 Exemple de configuration

```json
{
  "plages": [
    {"debut": 0, "fin": 6, "mode": "silencieux", "seuil_critique": 95},
    {"debut": 6, "fin": 8, "mode": "préparation", "seuil_critique": 90},
    {"debut": 8, "fin": 22, "mode": "réactif", "seuil_critique": 85},
    {"debut": 22, "fin": 24, "mode": "observation", "seuil_critique": 90}
  ],
  "vacances": false
}
