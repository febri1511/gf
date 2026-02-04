import streamlit as st
import random
import time

# ================= CONFIG =================
st.set_page_config(
    page_title="Pesan Bucin 💕",
    page_icon="❤️",
    layout="centered"
)

# ================= CSS =================
st.markdown("""
<style>
/* Background */
.stApp {
    background: linear-gradient(180deg, #ffd6dc, #f7a8b8);
}

/* Semua teks hitam */
h1, h2, h3, h4, h5, h6,
p, span, div, label {
    color: #000000 !important;
    text-align: center;
}

/* Tombol */
div.stButton > button {
    background-color: #ff4f7b;
    color: white !important;
    border-radius: 14px;
    padding: 12px 26px;
    font-size: 16px;
    border: none;
}
div.stButton > button:hover {
    background-color: #ff2f65;
}

/* Box pesan */
div[data-testid="stSuccess"] {
    background-color: #fff5f7;
    border-radius: 14px;
    padding: 18px;
    font-size: 18px;
}

/* Spinner */
div[data-testid="stSpinner"] {
    color: #000000 !important;
}

/* Love animation */
.heart {
    position: fixed;
    top: -10px;
    font-size: 24px;
    animation: fall linear infinite;
    color: rgba(255, 79, 123, 0.65);
}

@keyframes fall {
    0% {
        transform: translateY(-10px);
        opacity: 0.9;
    }
    100% {
        transform: translateY(110vh);
        opacity: 0;
    }
}
</style>
""", unsafe_allow_html=True)

# ================= LOVE JATUH =================
for _ in range(10):
    st.markdown(
        f"""
        <div class="heart" style="
            left:{random.randint(0,100)}%;
            animation-duration:{random.randint(8,15)}s;
            font-size:{random.randint(18,30)}px;
        ">❤️</div>
        """,
        unsafe_allow_html=True
    )

# ================= KONTEN =================
st.title("Hi Seng❤️ ada pesan baru nih! 💌")

pesan_bucin = [
    "Semangat magangnya hari ini yaa ❤️",
]

if st.button("💌 Klik aku dong"):
    with st.spinner("Lagi nyiapin pesan bucin... 💌"):
        time.sleep(1.2)

    st.success(random.choice(pesan_bucin))
    st.balloons()

st.markdown("---")
st.caption("Dibuat dengan ❤️ oleh mas-mas IT orang Kalong😁")
