import streamlit as st
from pathlib import Path

# Page setup
st.set_page_config(page_title="Intro Video", page_icon="📺", layout="centered")

st.title("📺 Sciviz Introductory Video")

video_path = Path("assets/Intro/Intro_video.mp4")

if video_path.exists():
    # Inject CSS to reduce video height
    st.markdown(
        """
        <style>
        video {
            max-height: 300px !important;  /* Adjust height */
            border-radius: 10px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.3);
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.video(str(video_path))
else:
    st.info("Introductory video coming soon...")

# Back button
if st.button("🔙 Back to Home"):
    st.switch_page("app.py")
