import csv

with open("logs/alerts_berserk.csv", encoding="utf-8") as f:
    reader = csv.reader(f)
    print("\n🧾 Alertes BERSERK :\n")
    for i, row in enumerate(reader):
        print(f"{i:>2}. {row[0]} | {row[1]} | {row[2]}% → {row[3]} USDT")