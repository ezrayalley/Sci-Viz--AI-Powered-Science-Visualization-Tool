import streamlit as st

# Page config
st.set_page_config(page_title="Physics - Sciviz", layout="centered", page_icon="📘")

# Initialize session state
if "physics_concept" not in st.session_state:
    st.session_state.physics_concept = None
if "show_video" not in st.session_state:
    st.session_state.show_video = False

# Title
st.title("📘 Physics Visualizations")

# Main selection page
if st.session_state.physics_concept is None:
    st.markdown("### Explore core Physics concepts through AI-powered animations and graphs.")
    st.markdown("---")
    st.markdown("#### 📊 Select a Physics Concept")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🚀 Projectile Motion"):
            st.session_state.physics_concept = "projectile"
    
        if st.button("🌀 Circular Motion"):
            st.session_state.physics_concept = "circular"

    with col2:
        if st.button("🔁 Simple Harmonic Motion"):
            st.session_state.physics_concept = "shm"

    st.markdown("---")
    st.caption("Developed by Ezra Yalley • Sciviz Project • ezra.yalley@gmail.com")

# Detail page for each concept
else:
    def show_equations_page(title, equations):
        st.subheader(f"📘 {title}")
        st.markdown("#### 📗 Equations Used:")
        for eq in equations:
            st.latex(eq)

        if st.button("🎬 Generate Visuals"):
            st.session_state.show_video = True

    def show_video_page(title, video_file):
        st.subheader(f"📽️ {title} Animation")
        st.video(f"assets/physics/{video_file}")

    if st.session_state.physics_concept == "projectile":
        if not st.session_state.show_video:
            show_equations_page(
                "Projectile Motion",
                [
                    r"x = v_0 \cos(\theta) t",
                    r"y = v_0 \sin(\theta) t - \frac{1}{2} g t^2"
                ]
            )
        else:
            show_video_page("Projectile Motion", "ProjectileMotion.mp4")

    elif st.session_state.physics_concept == "shm":
        if not st.session_state.show_video:
            show_equations_page(
                "Simple Harmonic Motion (SHM)",
                [
                    r"x(t) = A \cos(\omega t + \phi)",
                    r"a = -\omega^2 x"
                ]
            )
        else:
            show_video_page("Simple Harmonic Motion (SHM)", "SHMCombinedScene.mp4")

    elif st.session_state.physics_concept == "circular":
        if not st.session_state.show_video:
            show_equations_page(
                "Uniform Circular Motion",
                [
                    r"F_c = \frac{mv^2}{r}",
                    r"a_c = \frac{v^2}{r}"
                ]
            )
        else:
            show_video_page("Uniform Circular Motion", "CircularMotion.mp4")

    # Back button
    if st.button("🔙 Back"):
        st.session_state.physics_concept = None
        st.session_state.show_video = False
# Back Button
if st.button("🔙 Back to Home"):
    st.switch_page("app.py") 
