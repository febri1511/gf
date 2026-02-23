import streamlit as st
import base64
from pathlib import Path
import random

# =========================
# CONFIG PAGE
# =========================
st.set_page_config(page_title="Surat Cinta 💌", page_icon="💖", layout="centered")

# =========================
# FUNCTION ENCODE
# =========================
def encode_file(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# =========================
# LOAD FILES
# =========================
foto_path = Path("fotokita.jpeg")
musik_path = Path("perfect.mp3")

if not foto_path.exists():
    st.error("File fotokita.jpeg tidak ditemukan 😢")
    st.stop()

if not musik_path.exists():
    st.error("File perfect.mp3 tidak ditemukan 🎵😢")
    st.stop()

foto_base64 = encode_file(foto_path)
musik_base64 = encode_file(musik_path)

# =========================
# SESSION STATE
# =========================
if "open" not in st.session_state:
    st.session_state.open = False

# =========================
# GLOBAL CSS
# =========================
st.markdown(f"""
<style>

/* Hapus padding atas */
.block-container {{
    padding-top: 3rem;
}}

/* LOVE FLOATING */
.love {{
    position: fixed;
    bottom: -10%;
    color: rgba(255,0,100,0.7);
    animation: floatUp linear infinite;
}}

@keyframes floatUp {{
    0% {{ transform: translateY(0); opacity:0; }}
    30% {{ opacity:1; }}
    100% {{ transform: translateY(-120vh); opacity:0; }}
}}

/* AMPLOP */
.envelope {{
    font-size:140px;
    text-align:center;
    cursor:pointer;
    animation: bounce 2s infinite;
}}

@keyframes bounce {{
    0%,100% {{ transform: translateY(0); }}
    50% {{ transform: translateY(-15px); }}
}}

/* HALAMAN ROMANTIS */
.romantic {{
    background: linear-gradient(135deg, #ffc0cb, #ffb6c1);
    padding:50px;
    border-radius:30px;
    text-align:center;
    box-shadow: 0 15px 40px rgba(0,0,0,0.2);
    animation: fadeIn 1.5s ease;
}}

@keyframes fadeIn {{
    from {{opacity:0; transform:scale(0.9);}}
    to {{opacity:1; transform:scale(1);}}
}}

.photo {{
    width:320px;
    border-radius:20px;
    margin-top:20px;
    box-shadow:0 10px 30px rgba(0,0,0,0.3);
}}

.text {{
    color:black;
    font-size:20px;
    margin-top:25px;
    line-height:1.7;
}}

.title {{
    color:black;
    font-size:38px;
    font-weight:bold;
}}

</style>

<!-- MUSIK AUTOPLAY -->
<audio autoplay loop>
    <source src="data:audio/mp3;base64,{musik_base64}" type="audio/mp3">
</audio>
""", unsafe_allow_html=True)

# =========================
# LOVE ANIMATION RANDOM
# =========================
for i in range(40):
    left = random.randint(0, 100)
    size = random.randint(15, 30)
    duration = random.randint(5, 12)
    st.markdown(
        f'<div class="love" style="left:{left}%; font-size:{size}px; animation-duration:{duration}s;">❤️</div>',
        unsafe_allow_html=True
    )

# =========================
# HALAMAN AMPLOP
# =========================
if not st.session_state.open:

    st.markdown("<h1 style='text-align:center;'>Untuk Kamu 💌</h1>", unsafe_allow_html=True)
    st.markdown("<div class='envelope'>💌</div>", unsafe_allow_html=True)

    if st.button("Buka Surat 💖"):
        st.session_state.open = True
        st.rerun()

# =========================
# HALAMAN ROMANTIS
# =========================
else:

    html_content = f"""
    <div class="romantic">
        <div class="title">Happy Valentine Sayang ❤️</div>

        <img src="data:image/fotokita.jpeg;base64,{foto_base64}" class="photo" />

        <div class="text">
        Terima kasih sudah hadir di hidupku.<br>
        Kamu adalah alasan aku tersenyum setiap hari.<br><br>

        Aku bersyukur bisa mengenalmu, mencintaimu,<br>
        dan menjagamu sepenuh hati.<br><br>

        Kamu adalah rumah ternyaman,<br>
        pelukan terhangat,<br>
        dan alasan terindah aku bahagia.<br><br>

        <b>Aku sayang kamu, hari ini, besok, dan selamanya ❤️</b>
        </div>
    </div>
    """

    st.markdown(html_content, unsafe_allow_html=True)
