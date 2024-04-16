import qrcode
import streamlit as st
from qrcode import QRCode
filename ="qr_codes/qr_code.png"

def generate_qr_code(url, filename):
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_side=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    
    #creacion de app streamlit
st.set_page_config(page_title="Generador QR", page_icon="🀫", layout="centered")
st.image("images/supports.JPG", use_column_width=True)
st.title("Generador QR en Python")
url = st.text_input("Ingrese aquí URL..")
    
    
if st.button("Generar QR"):
    generate_qr_code(url,filename)
    st.image(filename, use_column_width=True)
    with open(filename, "rb") as f:
        image_date = f.read()
    download = st.download_button(label="Download QR", data=image_date, file_name="qr_generated.png")    
