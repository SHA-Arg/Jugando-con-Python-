import qrcode
import streamlit as st


filename = "qr_codes/"


def generate_qr_code(url, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=5,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")
    img.save(filename)


# App
st.set_page_config(page_title="Generador de Códigos QR",
                   page_icon=":smile:", layout="centered")
st.title("Generador de Códigos QR")
url = st.text_input("Introduce la URL que quieres convertir en un código QR")

# st.set_page_config(page_title="QR Code Generator",
#                    page_icon="🌐", layout="centered")
# st.title("QR Code Generator")
# url = st.text_input("Enter the URL")

if st.button("Generate QR Code"):
    generate_qr_code(url, filename)
    st.image(filename, use_column_width=True)
    with open(filename, "rb") as f:
        image_data = f.read()
    download = st.download_button(
        label="Download QR", data=image_data, file_name="qr_generated.png")


# Ejecuta este código en tu terminal para ver la aplicación:
# ejecución streamlit generador_de_qr.py
# La aplicación se abrirá en su navegador web predeterminado.


# Run this code in your terminal to see the app:
# streamlit run generador_de_qr.py
# The app will open in your default web browser.
