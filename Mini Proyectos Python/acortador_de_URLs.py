# # Projecto para acortar urls

# import pyshorteners
# import streamlit as st

# def shorten_url(url):
#     recorte =pyshorteners.Shortener()
#     shorten_url = recorte.tinyurl.short(url)
#     return shorten_url

# # Creacion de la web con streamlit

# st.set_page_config(page_title="S3BA", page_icon=None, layout="centered", initial_sidebar_state="auto", menu_items=None)
# st.image("ima") 

import streamlit as st

st.set_page_config(
    page_title= "S3B4 App",
    page_icon="🐱‍👤"
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items= {
        'Get Help': 'https://www.youtube.com/watch?v=120mtOLScug',
        'Report a bug': 'https://www.youtube.com/watch?v=120mtOLScug',
        'About': "Esto es el Header"
    }
)

