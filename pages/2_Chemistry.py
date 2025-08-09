import streamlit as st

# Page config
st.set_page_config(page_title="Chemistry - Sciviz", layout="centered", page_icon="🧪")

# Session state
if "chemistry_concept" not in st.session_state:
    st.session_state.chemistry_concept = None
if "show_chem_video" not in st.session_state:
    st.session_state.show_chem_video = False

# Title
st.title("🧪 Chemistry Visualizations")

# Main selection
if st.session_state.chemistry_concept is None:
    st.markdown("### Explore key Chemistry concepts through animated, AI-generated visuals.")
    st.markdown("#### 🧬 Choose a Chemistry Concept:")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔥 Arrhenius Equation"):
            st.session_state.chemistry_concept = "arrhenius"
        if st.button("🧫 Boyle’s Law"):
            st.session_state.chemistry_concept = "boyle"

    with col2:
        if st.button("🌡️ Charles’s Law"):
            st.session_state.chemistry_concept = "charles"
        if st.button("🧪 Energy Profile"):
            st.session_state.chemistry_concept = "energy"

    st.caption("Developed by Ezra Yalley • Sciviz Project • ezra.yalley@gmail.com")

else:
    def show_equation_page(title, equations):
        st.subheader(f"🔬 {title}")
        st.markdown("#### 📗 Equations Used:")
        for eq in equations:
            st.latex(eq)

        if st.button("🎬 Generate Visuals"):
            st.session_state.show_chem_video = True

    def show_chem_video(title, file):
        st.subheader(f"🎥 {title} Animation")
        st.video(f"assets/chemistry/{file}")

    # Logic for each concept
    if st.session_state.chemistry_concept == "arrhenius":
        if not st.session_state.show_chem_video:
            show_equation_page("Arrhenius Equation", [r"k = A e^{-E_a / RT}"])
        else:
            show_chem_video("Arrhenius Equation", "ArrheniusEquation.mp4")

    elif st.session_state.chemistry_concept == "boyle":
        if not st.session_state.show_chem_video:
            show_equation_page("Boyle’s Law", [r"P \cdot V = k"])
        else:
            show_chem_video("Boyle’s Law", "BoyleLaw.mp4")

    elif st.session_state.chemistry_concept == "charles":
        if not st.session_state.show_chem_video:
            show_equation_page("Charles’s Law", [r"\frac{V}{T} = k"])
        else:
            show_chem_video("Charles’s Law", "CharlesLaw.mp4")

    elif st.session_state.chemistry_concept == "energy":
        if not st.session_state.show_chem_video:
            show_equation_page(
    "Energy Profile of Chemical Reaction",
    [
        "ΔH = H_products - H_reactants",
        "ΔH = (Sum of bond energies of bonds broken) - (Sum of bond energies of bonds formed)"
    ]
)

        else:
            show_chem_video("Energy Profile", "EnergyProfile.mp4")

    if st.button("🔙 Back"):
        st.session_state.chemistry_concept = None
        st.session_state.show_chem_video = False
# Back Button
if st.button("🔙 Back to Home"):
    st.switch_page("app.py") 