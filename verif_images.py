import os

DOSSIER_IMAGES = "images"
VISUELS_ATTENDUS = [
    "fusee.gif",
    "error.gif",
    "check.gif",
    "loading.gif",
    "logo.png",
    "intro_cockpit.gif",
    "fond.gif",
    "fond.png"
]

print(f"📁 Vérification des visuels dans : {DOSSIER_IMAGES}\n")

if not os.path.exists(DOSSIER_IMAGES):
    print("❌ Dossier 'images' introuvable.")
else:
    fichiers = os.listdir(DOSSIER_IMAGES)
    for visuel in VISUELS_ATTENDUS:
        if visuel in fichiers:
            print(f"✅ {visuel} trouvé")
        else:
            print(f"❌ {visuel} manquant")