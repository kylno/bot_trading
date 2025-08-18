import csv
import os

def calculer_statistiques_profit():
    chemin_csv = os.path.abspath(os.path.join("data", "profit_log.csv"))

    try:
        with open(chemin_csv, "r", encoding="utf-8") as fichier:
            lignes = list(csv.reader(fichier))

            total_trades = 0
            trades_gagnants = 0
            trades_perdants = 0
            profit_total = 0.0

            for ligne in lignes:
                if len(ligne) < 5:
                    continue  # Ignore les lignes invalides
                try:
                    profit = float(ligne[4])
                    profit_total += profit
                    total_trades += 1
                    if profit > 0:
                        trades_gagnants += 1
                    else:
                        trades_perdants += 1
                except ValueError:
                    continue  # Ignore erreurs de conversion

            taux_reussite = round((trades_gagnants / total_trades) * 100, 2) if total_trades > 0 else 0

            return {
                "total_trades": total_trades,
                "trades_gagnants": trades_gagnants,
                "trades_perdants": trades_perdants,
                "profit_total": round(profit_total, 2),
                "taux_reussite": f"{taux_reussite}%"
            }

    except FileNotFoundError:
        print(f"Fichier introuvable : {chemin_csv}")
        return {
            "total_trades": 0,
            "trades_gagnants": 0,
            "trades_perdants": 0,
            "profit_total": 0,
            "taux_reussite": "0%"
        }