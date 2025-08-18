# 🤖 Fiches techniques des bots de trading

## 1. Casa de Papel

| Caractéristique            | Détail                                     |
|----------------------------|--------------------------------------------|
| 🔍 Type de trading         | Swing trading ou daily                     |
| 📈 Style                   | Stratégie calme, sécurisée et stable       |
| 🎯 Objectif                | Bénéfice régulier (+10 à +20% / mois)      |
| ⚖️ Gestion du capital      | Prudente, sans levier                      |
| 🛑 Comportement défensif   | Se retire si l’actif devient incertain     |
| 🧭 Usage recommandé        | Partie stable et conservatrice du portefeuille |

---

## 2. Berzerk

| Caractéristique            | Détail                                       |
|----------------------------|----------------------------------------------|
| 🔍 Type de trading         | Scalping, sniper, haute réactivité            |
| 🧨 Style                   | Explosif, agressif, chasse aux signaux        |
| 📡 Sources analysées       | Actus, X, Reddit, Telegram, microcaps         |
| 📈 Objectif                | +5 %, +12 %, jusqu’à +500 %                  |
| ⚠️ Risques                 | Drawdowns acceptés, levier possible          |
| 💥 Usage recommandé        | Partie offensive, allocation distincte       |

---

## 3. Berzerk+ (version survitaminée)

| Caractéristique            | Détail                                                                 |
|----------------------------|------------------------------------------------------------------------|
| 🎯 Objectif                | Pré-pumps & mouvements massifs avant explosion                        |
| 📈 Gains visés             | +100 % ➜ +500 % sur microcaps et smallcaps                             |
| 📡 Intelligence            | IA avec score de pump via sentiment + volume + timing social           |
| ⚠️ Gestion du capital      | Très agressive, à utiliser sur moins de 10 % du portefeuille            |
| 🧬 Modules associés        | `scanner_social.py`, `score_predictif.py`, `execution_sniper.py`       |

---

## 💰 Répartition du capital suggérée

| Bot         | Allocation | Rôle                         |
|-------------|------------|------------------------------|
| Casa        | 70 %       | Sécurité, croissance stable |
| Berzerk     | 20 %       | Performance agressive       |
| Berzerk+    | 10 %       | Gros coups ultra risqués    |