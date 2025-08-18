from fpdf import FPDF
import pandas as pd, json
import matplotlib.pyplot as plt
from datetime import datetime

def generer_rapport_pdf():
    try:
        with open("logs/capital.jsonl", "r", encoding="utf-8") as f:
            capital_data = [json.loads(l) for l in f.readlines()]
        df = pd.DataFrame(capital_data)
        df["timestamp"] = pd.to_datetime(df["timestamp"])
    except:
        return False

    plt.figure(figsize=(8, 4))
    plt.plot(df["timestamp"], df["capital"], marker="o", color="teal")
    plt.title("Évolution du capital")
    plt.xlabel("Date")
    plt.ylabel("Capital (€)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("logs/capital_graph.png")

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=14)
    pdf.cell(200, 10, txt="🧠 Rapport IA – Évolution du Capital", ln=True, align="C")
    pdf.ln(10)
    pdf.image("logs/capital_graph.png", x=10, y=30, w=190)

    try:
        with open("logs/investissements.json", "r", encoding="utf-8") as f:
            investissements = json.load(f)
        pdf.set_font("Arial", size=12)
        pdf.ln(85)
        pdf.cell(200, 10, txt="📦 Investissements", ln=True)
        for k, v in investissements.items():
            pdf.cell(200, 10, txt=f"{k} : {v}", ln=True)
    except:
        pdf.cell(200, 10, txt="Aucun investissement trouvé.", ln=True)

    pdf.output("logs/rapport_capital.pdf")
    return True