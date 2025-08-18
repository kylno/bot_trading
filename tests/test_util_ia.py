from streamlit_app.utils_ia import charger_donnees

def test_charger_donnees():
    data = charger_donnees("data/exemple.csv")
    assert data is not None