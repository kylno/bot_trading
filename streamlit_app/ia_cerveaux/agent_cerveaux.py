from streamlit_app.ia_cerveaux.microcap1 import MicroCap1IA
from streamlit_app.ia_cerveaux.microcap2 import MicroCap2IA
from streamlit_app.ia_cerveaux.profiteur import ProfiteurIA
from streamlit_app.ia_cerveaux.casa import CasaDePapelIA
from streamlit_app.ia_cerveaux.diagnostiqueur import DiagnostiqueurIA
# Ajoute ici les autres cerveaux

cerveaux_disponibles = {
    "MicroCap1": MicroCap1IA(),
    "MicroCap2": MicroCap2IA(),
    "Profiteur": ProfiteurIA(),
    "CasaDePapel": CasaDePapelIA(),
    "Diagnostiqueur": DiagnostiqueurIA(),
    # etc.
}

def get_cerveau(nom):
    return cerveaux_disponibles.get(nom)