import streamlit as st
import time
import threading
from prometheus_client import start_http_server, Counter, Summary, REGISTRY

# Empêche la redéfinition multiple des métriques si le code est rechargé par Streamlit
def get_or_create_metric(metric_class, name, documentation, **kwargs):
    try:
        return metric_class(name, documentation, **kwargs)
    except ValueError:
        return REGISTRY._names_to_collectors[name]

# Définir les métriques
CLICK_COUNT = get_or_create_metric(Counter, "streamlit_button_clicks", "Nombre total de clics sur le bouton")
ERROR_COUNT = get_or_create_metric(Counter, "streamlit_errors_total", "Nombre total d’erreurs dans l’application")
PROCESSING_TIME = get_or_create_metric(Summary, "streamlit_processing_seconds", "Temps de traitement")

# Démarrer serveur Prometheus (une seule fois)
def launch_prometheus_server():
    try:
        start_http_server(8000)
    except OSError:
        pass  # Port déjà occupé (pas besoin de relancer)

threading.Thread(target=launch_prometheus_server, daemon=True).start()

# Interface Streamlit
st.title("Monitoring Streamlit")

@PROCESSING_TIME.time()
def traitement():
    time.sleep(1.5)
    if time.time() % 2 < 1:
        raise Exception("Erreur simulée")

if st.button("Lancer le traitement"):
    CLICK_COUNT.inc()
    try:
        traitement()
        st.success("Succès !")
    except Exception as e:
        ERROR_COUNT.inc()
        st.error(f"Erreur : {e}")
