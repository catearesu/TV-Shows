import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import streamlit.components.v1 as components
import codecs
import buscador
import reviews
import predictor
import overview
import tableau


# Configuramos la página
st.set_page_config(
    page_title="TV-Shows Analysis, Finder & much more",
    page_icon=":tv:",
    layout="wide",
    initial_sidebar_state="auto"
)



# Barra lateral de navegación
with st.sidebar:
    selected_option = option_menu(
        menu_title="Menu",
        options=["OVERVIEW","VISUALIZATIONS","SEARCH","EMMY PREDICTOR", "USERS OPINIONS"],
        icons=["file-text", "bar-chart","search","trophy", "chat"],
        menu_icon="cast",
        default_index=0
    )

# Llamamos a la función correspondiente según la opción seleccionada
if selected_option== "SEARCH":
    buscador.tv_shows_finder()
elif selected_option == "USERS OPINIONS":
    reviews.user_reviews()
elif selected_option == "EMMY PREDICTOR":
    predictor.predict_emmy()
elif selected_option == "OVERVIEW":
    overview.show_overview()
elif selected_option == "VISUALIZATIONS":
    tableau.show_dashboard()