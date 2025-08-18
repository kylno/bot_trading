import os
import csv
import time
import random
import smtplib
from fpdf import FPDF
from datetime import datetime, timedelta
from collections import defaultdict, Counter
from email.message import EmailMessage
import matplotlib.pyplot as plt
from colorama import Fore, init
init(autoreset=True)

# 🧠 Option 31 — Générateur de nom stylisé
def generer_nom_stylisé():
    préfixes = ["Alpha", "Beta", "Gamma", "Delta", "Epsilon", "Zeta", "Theta", "Omega", "Sigma", "Xeno"]
    suffixes = ["-X", "-Core", "-Pulse", "-Net", "-AI", "-Shadow", "-Nova", "-Flux"]
    symboles = ["⚡", "🐜", "🧠", "🔥", "🛰️", "💡"]
    return random.choice(symboles) + random.choice(préfixes) + random.choice(suffixes)

# ✅ Option 27 — Générer statistiques PNG
def generer_statistiques_visuelles():
    try:
        with open("logs/fourmi_log.csv", "r", encoding="utf-8") as f:
            lignes = list(csv.reader(f))[1:]
        roles = [l[2] for l in lignes]
        bots = [l[3] for l in lignes]
        dates = [l[0].split(" ")[0] for l in lignes]
        compteur_roles = Counter(roles)
        compteur_bots = Counter(bots)
        compteur_dates = Counter(dates)
        os.makedirs("exports", exist_ok=True)

        # Graphs
        plt.figure(figsize=(6, 4))
        plt.bar(compteur_roles.keys(), compteur_roles.values(), color="skyblue")
        plt.title("Répartition des rôles")
        plt.savefig("exports/stats_roles.png"); plt.close()

        plt.figure(figsize=(6, 6))
        plt.pie(compteur_bots.values(), labels=compteur_bots.keys(), autopct="%1.1f%%")
        plt.title("Répartition des Bots")
        plt.savefig("exports/stats_bots.png"); plt.close()

        jours = sorted(compteur_dates.items())
        plt.figure(figsize=(8, 4))
        plt.plot([j[0] for j in jours], [j[1] for j in jours], marker="o")
        plt.title("Activité quotidienne")
        plt.xticks(rotation=45)
        plt.savefig("exports/stats_journalier.png"); plt.close()
        print(Fore.GREEN + "📊 Graphiques enregistrés dans /exports/")
    except Exception as e:
        print(Fore.RED + f"❌ Erreur stats : {e}")

# ✅ Option 28 — Export PDF des stats visuelles
def export_graphes_pdf():
    try:
        pdf = FPDF()
        images = [
            ("stats_roles.png", "Répartition des rôles"),
            ("stats_bots.png", "Répartition des Bots"),
            ("stats_journalier.png", "Activité quotidienne"),
        ]
        for file, titre in images:
            path = os.path.join("exports", file)
            if os.path.exists(path):
                pdf.add_page()
                pdf.set_font("Arial", 'B', 14)
                pdf.cell(0, 10, titre, ln=True, align="C")
                pdf.image(path, x=10, y=25, w=190)
            else:
                print("❌ Image manquante :", file)
        pdf.output("exports/statistiques_fourmis.pdf")
        print(Fore.CYAN + "📎 PDF des stats généré : exports/statistiques_fourmis.pdf")
    except Exception as e:
        print(Fore.RED + f"❌ Erreur export PDF stats : {e}")
        
        # ✅ Option 30 — Détection d'inactivité
def detecter_fourmis_inactives(jours=3):
    try:
        limite = datetime.today() - timedelta(days=jours)
        with open("logs/fourmi_log.csv", "r", encoding="utf-8") as f:
            lignes = list(csv.reader(f))[1:]
        dernières_dates = {}
        for ligne in lignes:
            date, fourmi, *_ = ligne
            d = datetime.strptime(date, "%Y-%m-%d %H:%M")
            if fourmi not in dernières_dates or d > dernières_dates[fourmi]:
                dernières_dates[fourmi] = d
        inactives = [f for f, d in dernières_dates.items() if d < limite]
        if inactives:
            print(Fore.YELLOW + f"\n🧠 Fourmis inactives depuis plus de {jours} jours :")
            for f in inactives: print(" -", f)
        else:
            print(Fore.GREEN + "✅ Aucune inactivité détectée.")
    except Exception as e:
        print(Fore.RED + f"❌ Erreur inactivité : {e}")

# ✅ Option 32 — Simulateur IA automatique
def simuler_colonie(cycles=10, delay=5):
    print(Fore.CYAN + f"🚀 Simulation IA : {cycles} missions toutes les {delay} sec")
    try:
        for i in range(cycles):
            print(Fore.YELLOW + f"📡 Mission {i+1}/{cycles}")
            generer_mission_auto()
            time.sleep(delay)
        print(Fore.GREEN + "✅ Simulation terminée.")
    except Exception as e:
        print(Fore.RED + f"❌ Erreur simulateur : {e}")

# ✅ Option 29 — Interface Tkinter (facultative)
def lancer_interface_tkinter():
    try:
        import tkinter as tk
        root = tk.Tk()
        root.title("BrainTrader 🐜")
        root.geometry("320x330")
        tk.Label(root, text="Interface BrainTrader", font=("Arial", 14)).pack(pady=10)
        tk.Button(root, text="Mission IA solo", command=generer_mission_auto).pack(pady=5)
        tk.Button(root, text="5 missions IA", command=lambda: generer_missions_auto_par_lot(5)).pack(pady=5)
        tk.Button(root, text="Statistiques visuelles", command=generer_statistiques_visuelles).pack(pady=5)
        tk.Button(root, text="PDF des stats", command=export_graphes_pdf).pack(pady=5)
        tk.Button(root, text="Quitter", command=root.destroy).pack(pady=15)
        root.mainloop()
    except Exception as e:
        print(Fore.RED + f"❌ Erreur Tkinter : {e}")
        
def menu():
    print("✅ Fonction menu() bien appelée")  # ← Sonde pour vérifier qu'on entre bien ici


    print(Fore.MAGENTA + "\n🐜 Bienvenue dans BRAINTRADER ZeroX.1\n")
    print(Fore.CYAN + f"📅 {datetime.today().strftime('%A %d %B %Y — %H:%M')}\n") 
    while True:
        
        print(Fore.YELLOW + "\n🔷 MENU BRAINTRADER")
        print("1  : Afficher statut")
        print("22 : Export PDF")
        print("23 : Ouvrir PDF")
        print("24 : Envoyer PDF par email")
        print("25 : Mission IA solo")
        print("26 : Missions IA groupées")
        print("27 : Statistiques PNG")
        print("28 : PDF Statistiques")
        print("29 : Interface Tkinter")
        print("30 : Fourmis inactives")
        print("31 : Générer nom stylisé")
        print("32 : Simulateur IA")
        print("0  : Quitter\n")
        choix = input("🧭 Choix > ")

        if choix == "1": afficher_statut()
        elif choix == "22": export_statut_pdf()
        elif choix == "23": ouvrir_pdf()
        elif choix == "24":
            to = input("📧 Destinataire > ")
            envoyer_pdf_par_email(to)
        elif choix == "25": generer_mission_auto()
        elif choix == "26":
            try: generer_missions_auto_par_lot(int(input("Combien ? > ")))
            except: print("❌ Nombre invalide.")
        elif choix == "27": generer_statistiques_visuelles()
        elif choix == "28": export_graphes_pdf()
        elif choix == "29": lancer_interface_tkinter()
        elif choix == "30":
            try: detecter_fourmis_inactives(int(input("Inactives depuis ? jours > ")))
            except: print("❌ Entrée invalide.")
        elif choix == "31": print("⚡ Nom stylisé : ", generer_nom_stylisé())
        
if __name__ == "__main__":
    menu()