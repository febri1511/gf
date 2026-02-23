import streamlit as st
import random
from datetime import datetime

# ======================
# KONFIGURASI HALAMAN
# ======================
st.set_page_config(
    page_title="Semangat Kerja, Sayang ❤️",
    page_icon="💖",
    layout="centered"
)

# ======================
# CUSTOM CSS
# ======================
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    color: white;
}

h1 {
    text-align: center;
    font-size: 42px !important;
}

.stButton>button {
    background: linear-gradient(45deg, #ff4b6e, #ff758c);
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 16px;
    font-weight: bold;
}

.stButton>button:hover {
    background: linear-gradient(45deg, #ff758c, #ff4b6e);
}

.footer {
    text-align: center;
    margin-top: 50px;
    font-size: 14px;
    opacity: 0.7;
}
</style>
""", unsafe_allow_html=True)

# ======================
# JUDUL
# ======================
st.markdown("<h1>💼 Semangat Kerjanya, Sayang ❤️</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Pesan spesial buat kamu yang lagi kerja hari ini 💖</p>", unsafe_allow_html=True)

st.write("")

# ======================
# LIST PESAN
# ======================
pesan_semangat = [
    "Aku bangga banget sama kamu 💖",
    "Semangat yaa, calon orang sukses 😘",
    "Kerja keras kamu hari ini untuk masa depan kita ✨",
    "Kalau capek, ingat ada aku yang selalu dukung kamu 🤗",
    "Kamu hebat banget, jangan pernah ragu 💪",
    "Semoga semua urusan kamu lancar hari ini 🍀",
    "Jangan lupa makan dan istirahat ya ❤️"
]

# ======================
# TOMBOL
# ======================
if st.button("💌 Tekan Aku"):
    pesan = random.choice(pesan_semangat)

    st.markdown(f"""
    <div style='
        background: linear-gradient(45deg,#11998e,#38ef7d);
        padding:20px;
        border-radius:15px;
        font-size:18px;
        text-align:center;
        margin-top:20px;
    '>
        <b>Halo Sayang! 💕</b><br><br>
        {pesan}
    </div>
    """, unsafe_allow_html=True)

# ======================
# UCAPAN SESUAI WAKTU
# ======================
jam = datetime.now().hour

if jam < 12:
    waktu = "Selamat pagi! Semoga harimu menyenangkan ☀️"
elif jam < 18:
    waktu = "Selamat siang! Tetap semangat ya 🌤️"
else:
    waktu = "Selamat malam! Jangan lupa istirahat ya 😴"

st.markdown(f"""
<div style='
    background-color:#1f4068;
    padding:15px;
    border-radius:10px;
    margin-top:20px;
    text-align:center;
'>
    {waktu}
</div>
""", unsafe_allow_html=True)

# ======================
# FOOTER
# ======================
st.markdown("<div class='footer'>Dibuat oleh Febri", unsafe_allow_html=True)