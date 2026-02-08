import streamlit as st
import time

st.set_page_config(
    page_title="💌 Sebuah Amplop Untuk Kamu",
    page_icon="💖",
    layout="centered"
)

# ================= CSS =================
st.markdown("""
<style>
.envelope {
    font-size: 120px;
    text-align: center;
}

img {
    display: block;
    margin-left: auto;
    margin-right: auto;
    border-radius: 20px;
    border: 4px solid #ff7eb3;
    box-shadow: 0 10px 25px rgba(0,0,0,0.25);
}
</style>
""", unsafe_allow_html=True)

# ================= HEADER =================
st.title("💖 Sebuah Amplop Untuk Kamu")
st.write("Klik amplopnya yaa… ada sesuatu di dalamnya 🥰")

# ================= STATE =================
if "opened" not in st.session_state:
    st.session_state.opened = False

# ================= AMPL0P TERTUTUP =================
if not st.session_state.opened:
    st.markdown("<div class='envelope'>💌</div>", unsafe_allow_html=True)

    if st.button("📩 Buka Amplop"):
        st.session_state.opened = True
        st.rerun()

# ================= AMPL0P TERBUKA =================
else:
    st.markdown("<div class='envelope'>💖</div>", unsafe_allow_html=True)
    time.sleep(0.3)
    st.balloons()

    # FOTO TENGAH
    st.image("fotokita.jpeg", width=260)

    # PESAN (TANPA KOTAK)
    st.markdown("## 💗 Selamat Hari Minggu, Seng 🌸")
    st.markdown("""
    Semoga hari ini hatimu tenang,  
    senyummu nggak hilang,  
    dan capekmu pelan-pelan menghilang 🤍
    """)

    st.markdown("""
    **Semangat ngerjain tugasnya yaa 📝✨**  
    Aku tau kamu lagi berjuang,  
    dan aku selalu bangga sama kamu 💞
    """)

    st.markdown("""
    Jangan lupa istirahat,  
    banyak minum air putih,  
    dan inget… ada aku yang selalu sayang kamu 💘
    """)

    st.markdown("💗 💕 💖")
    st.caption("— Dari Febri, yang selalu jatuh cinta sama Nadia setiap hari 🖤")
