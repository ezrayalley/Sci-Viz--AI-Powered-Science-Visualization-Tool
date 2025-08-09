import streamlit as st
import pandas as pd

st.set_page_config(page_title="Practice Test", page_icon="📝", layout="centered")

# ---------- SUBJECT SELECTION ----------
st.title("📝 Practice Test")

if "subject" not in st.session_state:
    subject = st.selectbox(
        "Select a subject:",
        ["Physics", "Chemistry", "Biology"]
    )
    if st.button("Start Test"):
        st.session_state.subject = subject
        st.session_state.current_q = 0
        st.session_state.user_answers = {}
        st.session_state.show_results = False
        st.rerun()

# ---------- LOAD QUESTIONS ----------
else:
    file_paths = {
        "Physics": "questions/physics_questions.csv",
        "Chemistry": "questions/chemistry_questions.csv",
        "Biology": "questions/biology_questions.csv"
    }
    df = pd.read_csv(file_paths[st.session_state.subject])

    # Shuffle once
    if "shuffled_questions" not in st.session_state:
        st.session_state.shuffled_questions = df.sample(frac=1).reset_index(drop=True)

    questions = st.session_state.shuffled_questions
    total_qs = len(questions)

    # ---------- SHOW RESULTS ----------
    if st.session_state.show_results:
        st.title(f"📊 {st.session_state.subject} Test Results")
        
        score = 0
        for i, row in questions.iterrows():
            user_answer = st.session_state.user_answers.get(i, None)
            correct_letter = row["CorrectAnswer"].strip()

            option_map = {
                "A": row["OptionA"],
                "B": row["OptionB"],
                "C": row["OptionC"],
                "D": row["OptionD"]
            }
            correct_text = option_map[correct_letter]

            if user_answer == correct_letter:
                score += 1

            st.markdown(f"**Q{i+1}:** {row['Question']}")
            st.markdown(f"✅ Correct Answer: **{correct_text}** ({correct_letter})")
            st.markdown(f"📝 Your Answer: **{option_map.get(user_answer, 'No answer')}**")
            st.info(f"💡 Explanation: {row['Explanation']}")
            st.markdown("---")

        st.subheader(f"🎯 Final Score: {score}/{total_qs}")

        if st.button("🔙 Back to Subject Selection"):
            for key in ["subject", "shuffled_questions", "user_answers", "show_results"]:
                st.session_state.pop(key, None)
            st.rerun()

    # ---------- SHOW QUESTIONS ----------
    else:
        row = questions.iloc[st.session_state.current_q]
        st.subheader(f"Q{st.session_state.current_q+1} of {total_qs}")
        st.markdown(f"**{row['Question']}**")

        options = {
            "A": row["OptionA"],
            "B": row["OptionB"],
            "C": row["OptionC"],
            "D": row["OptionD"]
        }

        selected = st.radio(
            "Select an answer:",
            options.keys(),
            format_func=lambda x: f"{x}: {options[x]}",
            index=None if st.session_state.current_q not in st.session_state.user_answers 
                 else list(options.keys()).index(st.session_state.user_answers[st.session_state.current_q]),
            key=f"q_{st.session_state.current_q}"
        )

        if selected:
            st.session_state.user_answers[st.session_state.current_q] = selected

        col1, col2 = st.columns(2)
        with col1:
            if st.session_state.current_q > 0:
                if st.button("⬅ Back"):
                    st.session_state.current_q -= 1
                    st.rerun()
        with col2:
            if st.session_state.current_q < total_qs - 1:
                if st.button("Next ➡"):
                    st.session_state.current_q += 1
                    st.rerun()
            else:
                if st.button("✅ Finish Test"):
                    st.session_state.show_results = True
                    st.rerun()
# Back to Home button
if st.button("🏠 Back to Home"):
    for key in list(st.session_state.keys()):
        del st.session_state[key]  # Clears all session data
    st.switch_page("app.py")  # Navigates to your home page
