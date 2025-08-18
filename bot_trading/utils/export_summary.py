import json

def exporter_summary(perf_file="logs/performance_month.json", out_file="logs/summary.json"):
    with open(perf_file, encoding="utf-8") as f:
        perf_data = json.load(f)

    resume = {}
    for bot, perf in perf_data.items():
        vals = list(perf.values())
        if vals:
            resume[bot] = {
                "Trades": len(vals),
                "Moyenne": round(sum(vals)/len(vals), 2),
                "Max": max(vals),
                "Min": min(vals),
                "Recommandation": (
                    "🔥 Augmenter capital" if sum(vals)/len(vals) > 15 else
                    "🔄 Ajustement recommandé" if min(vals) < -10 else
                    "🧊 Neutre"
                )
            }

    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(resume, f, indent=2)
    print("✅ Fichier résumé enregistré :", out_file)

if __name__ == "__main__":
    exporter_summary()