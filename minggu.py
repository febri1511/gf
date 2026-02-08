import streamlit as st
import time

st.set_page_config(
    page_title="💌 Sebuah Amplop Untuk Kamu",
    page_icon="💖",
    layout="centered"
)

# CSS
st.markdown("""
<style>
.envelope {
    font-size: 120px;
    text-align: center;
}

.message-box {
    background-color: #ffeef5;
    padding: 35px;
    border-radius: 22px;
    border: 2px solid #ff7eb3;
    text-align: center;
    color: #000;
}

.message-box h2,
.message-box p,
.message-box b {
    color: #000;
}

.message-box p {
    font-size: 17px;
    line-height: 1.7;
}

.heart {
    font-size: 30px;
}
</style>
""", unsafe_allow_html=True)

st.title("💖 Sebuah Amplop Untuk Kamu")
st.write("Klik amplopnya yaa… ada sesuatu di dalamnya 🥰")

if "opened" not in st.session_state:
    st.session_state.opened = False

# AMPL0P TERTUTUP
if not st.session_state.opened:
    st.markdown('<div class="envelope">💌</div>', unsafe_allow_html=True)

    if st.button("📩 Buka Amplop"):
        st.session_state.opened = True
        st.rerun()

# AMPL0P TERBUKA
else:
    st.markdown('<div class="envelope">💖</div>', unsafe_allow_html=True)
    time.sleep(0.3)
    st.balloons()

    st.markdown("""
    <div class="message-box">
        <div class="heart">💗 💕 💖

        Selamat Hari Minggu, Seng 🌸
        
            Semoga hari ini hatimu tenang,
            senyummu nggak hilang,
            dan capekmu pelan-pelan menghilang 🤍
        
            Semangat ngerjain tugasnya yaa 📝✨
            Aku tau kamu lagi berjuang,
            dan aku selalu bangga sama kamu 💞
        
            Jangan lupa istirahat,
            banyak minum air putih,
            dan inget… ada aku yang selalu sayang kamu 💘
        
        💗 💕 💖
    
    """, unsafe_allow_html=True)

    st.caption("— Dari Febri, yang selalu jatuh cinta sama Nadia setiap hari 🖤")
