import streamlit as st

# Page config
st.set_page_config(page_title="Biology - Sciviz", layout="centered", page_icon="🧬")

# Session state
if "bio_concept" not in st.session_state:
    st.session_state.bio_concept = None
if "bio_video" not in st.session_state:
    st.session_state.bio_video = False

st.title("🧬 Biology Visualizations")

# Concept Selector
if st.session_state.bio_concept is None:
    st.markdown("### Explore biology concepts through animated models and scientific graphs.")
    st.markdown("---")
    st.markdown("#### 📊 Select a Biology Concept")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("⚗️ Enzyme Kinetics"):
            st.session_state.bio_concept = "enzyme"
    with col2:
        if st.button("🌱 Population Growth"):
            st.session_state.bio_concept = "population"

    if st.button("🔬 Cell Division (Mitosis)"):
        st.session_state.bio_concept = "mitosis"

    st.markdown("---")
    st.caption("Developed by Ezra Yalley • Sciviz Project • ezra.yalley@gmail.com")

# Equation + Generate Visuals Page
else:
    def show_equation_page(title, equations):
        st.subheader(f"📘 {title}")
        st.markdown("#### 📗 Equations Used:")
        for eq in equations:
            st.latex(eq)

        if st.button("🎬 Generate Visuals"):
            st.session_state.bio_video = True

    def show_video_page(title, video_file):
        st.subheader(f"📽️ {title} Animation")
        st.video(f"assets/biology/{video_file}")

    if st.session_state.bio_concept == "enzyme":
        if not st.session_state.bio_video:
            show_equation_page(
                "Enzyme Kinetics",
                [
                    r"v = \frac{V_{max} [S]}{K_m + [S]}"
                ]
            )
        else:
            show_video_page("Enzyme Kinetics", "EnzymeKinetics.mp4")

    elif st.session_state.bio_concept == "population":
        if not st.session_state.bio_video:
            show_equation_page(
                "Population Growth",
                [
                    r"P(t) = P_0 e^{rt} \quad \text{(Exponential)}",
                    r"P(t) = \frac{K}{1 + Ae^{-rt}} \quad \text{(Logistic)}"
                ]
            )
        else:
            show_video_page("Population Growth", "PopulationGrowth.mp4")

    elif st.session_state.bio_concept == "mitosis":
        if not st.session_state.bio_video:
            show_equation_page(
                "Cell Division (Mitosis)",
                [
                    r"\text{Stages: Prophase, Metaphase, Anaphase, Telophase}"
                ]
            )
        else:
            show_video_page("Cell Division (Mitosis)", "CellDivisionMitosis.mp4")

    if st.button("🔙 Back"):
        st.session_state.bio_concept = None
        st.session_state.bio_video = False
# Back Button
if st.button("🔙 Back to Home"):
    st.switch_page("app.py") 
 
