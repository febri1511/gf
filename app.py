import streamlit as st
import time

st.set_page_config(
    page_title="Buat Kamu 💖",
    page_icon="💖",
    layout="centered"
)

# Background gradasi
st.markdown(
    """
    <style>
    .main {
        background: linear-gradient(135deg, #ff9a9e, #fad0c4);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Judul
st.markdown(
    "<h1 style='text-align:center;'>Hai Sengg 💖</h1>",
    unsafe_allow_html=True
)

# Ucapan utama
st.markdown(
    """
    <p style='text-align:center; font-size:18px;'>
    Selamat Hari Senin yaa ☀️<br>
    Semangat jalanin magangnya hari ini 🌱<br>
    Aku tahu kamu capek, tapi kamu hebat banget.
    </p>
    """,
    unsafe_allow_html=True
)

# Emoji hati
st.markdown(
    "<div style='text-align:center; font-size:40px;'>💖</div>",
    unsafe_allow_html=True
)

# Tombol interaksi
if st.button("Klik aku 💌"):
    with st.spinner("Loading cinta..."):
        time.sleep(1.5)

    st.success("💌 Pesan khusus buat kamu")

    st.markdown(
        """
        <p style='text-align:center; font-size:17px;'>
        Jangan lupa senyum hari ini 🤍<br>
        Kerja pelan-pelan tapi konsisten ya 🌿<br>
        Aku selalu doain kamu dari sini.<br><br>
        <b>Aku bangga sama kamu, selamat menjalani hari Senin 😘</b>
        </p>
        """,
        unsafe_allow_html=True
    )

# Footer
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align:center; font-size:12px;'>Dibuat dengan ❤️ oleh febrianscah</p>",
    unsafe_allow_html=True
)
