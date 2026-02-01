import streamlit as st
import time

st.set_page_config(
    page_title="Buat Kamu 💖",
    page_icon="💖",
    layout="centered"
)

# Background sederhana
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

st.markdown("<h1 style='text-align:center;'>Hai Kamu 💖</h1>", unsafe_allow_html=True)

st.markdown(
    """
    <p style='text-align:center; font-size:18px;'>
    Semangat ya magangny🌱 <br>
    Aku tahu kamu capek, tapi kamu hebat banget.
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown("<div style='text-align:center; font-size:40px;'>💖</div>", unsafe_allow_html=True)

if st.button("Klik aku 💌"):
    with st.spinner("Loading cinta..."):
        time.sleep(1.5)

    st.success("💌 Pesan khusus buat kamu")

    st.markdown(
        """
        <p style='text-align:center; font-size:17px;'>
        Aku selalu doain kamu dari sini 🤍<br>
        Jangan lupa istirahat, makan yang cukup,<br>
        dan jangan terlalu keras sama diri sendiri.<br><br>
        <b>Aku bangga sama kamu 😘</b>
        </p>
        """,
        unsafe_allow_html=True
    )

st.markdown("<br>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align:center; font-size:12px;'>Dibuat dengan ❤️ oleh pacarmu</p>",
    unsafe_allow_html=True
)
