# timeline.py
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os
from datetime import datetime, timedelta

# Configuration
log_file = 'fourmi_log.csv'
output_path = 'exports/img/timeline.png'
days_back = 10
rolling_window = 7

# Charger les logs
df = pd.read_csv(log_file)

# S'assurer que la colonne date existe
if 'date' not in df.columns:
    raise ValueError("Le fichier CSV doit contenir une colonne 'date' au format YYYY-MM-DD")

# Conversion des dates
df['date'] = pd.to_datetime(df['date'])

# Filtrer sur les X derniers jours
limit_date = datetime.now() - timedelta(days=days_back)
df = df[df['date'] >= limit_date]

# Grouper par jour
count_by_day = df.groupby(df['date'].dt.date).size()

# Créer un DataFrame propre
timeline_df = count_by_day.reindex(
    pd.date_range(limit_date, datetime.now(), freq='D').date,
    fill_value=0
)
timeline_df = pd.Series(timeline_df)

# Ajouter la moyenne mobile
rolling = timeline_df.rolling(window=rolling_window, min_periods=1).mean()

# Plot
fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(timeline_df.index, timeline_df.values, color='#4da6ff', label='Missions IA / jour')
ax.plot(timeline_df.index, rolling, color='orange', linewidth=2, label='Moyenne mobile (7j)')

# Format du graphique
ax.set_title("📈 Timeline des Missions IA (10 derniers jours)")
ax.set_xlabel("Date")
ax.set_ylabel("Nombre de missions")
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m'))
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.4)
plt.legend()

# Créer dossier si besoin
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Sauvegarder l’image
plt.tight_layout()
plt.savefig(output_path)
plt.close()

print(f"✅ Timeline générée ➤ {output_path}")