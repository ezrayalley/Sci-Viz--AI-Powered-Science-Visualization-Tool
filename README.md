# 🎓 Sci-viz - Where Science Concepts Come to Life through AI-Powered Visualizations

Sci-viz is an interactive AI-powered STEM learning tool that transforms equations and theories in Physics, Chemistry, and Biology into dynamic animations and simulations using the Manim engine.
Designed for students, educators, and science enthusiasts, Sciviz makes complex concepts visual, interactive, and unforgettable.
---

<img width="1135" height="672" alt="image" src="https://github.com/user-attachments/assets/b61ab4a6-f46a-4f40-83c3-1e51a4e15362" />
---

✨ Features
🎥 Stunning Animated Visuals — Equations & theories brought to life with Manim.

🧪 Multi-Subject Support — Physics, Chemistry, and Biology visualizations.

📝 Interactive Practice Tests — One-question-per-screen exam mode with explanations.

📚 Accurate Formulas & Models — Scientifically precise representations.

🎤 Introductory Video — Engaging app walkthrough for first-time users.

🖥 Streamlit Interface — Clean, responsive, and easy to navigate.

⚡ Installation
bash
Copy
Edit
# Clone the repository
git clone https://github.com/YourUsername/Sciviz.git
cd Sciviz

# Create a virtual environment
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate # On Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
📂 Project Structure
graphql
Copy
Edit
Sciviz/
│
├── app.py                  # Main entry point
├── pages/                  # Streamlit multipage scripts
│   ├── 0_Intro_Video.py
│   ├── 1_Physics.py
│   ├── 2_Chemistry.py
│   ├── 3_Biology.py
│   └── 4_Practice_Test.py
├── backend/                # Manim animation scripts
├── assets/                 # Videos, images, and static files
├── questions/              # Practice test CSV files
└── requirements.txt
💡 Tech Stack
Streamlit — Interactive web UI

Manim — Mathematical animations

Python — Backend logic & data handling

Pandas — Practice test handling

FFmpeg — Video processing

📜 License
This project is licensed under the MIT License — feel free to modify and use it for educational purposes.

👨‍💻 Author
Ezra Yalley
📧 ezra.yalley@gmail.com
🌐 LinkedIn

Made with ❤️ for science learners worldwide.
