import streamlit as st
from pathlib import Path

# Set page config
st.set_page_config(
    page_title="Sciviz - AI-Powered Visual Science",
    layout="wide",
    page_icon="🔬"
)

# Background style
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(to right, #f0f4f8, #e6f7ff);
}
[data-testid="stHeader"] {
    background: none;
}
h1, h2, h3 {
    color: #003366;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# Title and subtitle
st.title("🔬 Sciviz")
st.subheader("AI-Powered Visualizations – Bringing Science Concepts to Life")

# Intro video button
st.markdown("### 🎥 Introductory Video")
st.page_link("pages/0_Intro_Video.py", label="📺 Click to Watch Intro Video")

# Quick tip
st.markdown("🧭 *Click a subject to explore animated science visualizations.*")

# Subject cards (2 columns)
col1, col2 = st.columns(2)

with col1:
    st.page_link("pages/1_Physics.py", label="📘 Physics", icon="📘")
    st.page_link("pages/2_Chemistry.py", label="🧪 Chemistry", icon="🧪")

with col2:
    st.page_link("pages/3_Biology.py", label="🧬 Biology", icon="🧬")
    st.page_link("pages/4_Practice_Test.py", label="📝 Practice Test", icon="📝")

# Footer
st.markdown("---")
st.markdown("📌 **Developed by:** Ezra Yalley  \n📧 **Email:** ezra.yalley@gmail.com")
