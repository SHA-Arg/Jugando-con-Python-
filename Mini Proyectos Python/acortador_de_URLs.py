import pyshorteners
import streamlit as st


def shorten_url(url):
    s = pyshorteners.Shortener()
    shorten_url = s.tinyurl.short(url)
    return shorten_url


st.title("Acortador de URLs")
url = st.text_input("Introduce la URL que quieres acortar")
if st.button("Acortar"):
    short_url = shorten_url(url)
    st.success(short_url)
    st.write("La URL acortada es:", short_url)
    st.write(
        "Puedes copiar y pegar la URL acortada en tu navegador para acceder a la página original.")
