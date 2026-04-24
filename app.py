import streamlit as st

st.set_page_config(
    page_title="AI Problem Solving Assignment",
    page_icon="🤖",
    layout="centered"
)

# === VIBRANT LANDING CSS ===
st.markdown("""
<style>
    .stApp {
        background: radial-gradient(circle at center, #1a0b2e, #000000);
        color: #e0e6ed;
        font-family: 'Inter', sans-serif;
    }
    h1 {
        background: -webkit-linear-gradient(45deg, #ff00cc, #333399);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 900 !important;
        text-shadow: 0px 0px 20px rgba(255, 0, 204, 0.4);
        text-align: center;
    }
    .landing-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 20px;
        margin-bottom: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        transition: transform 0.3s ease;
    }
    .landing-card:hover {
        transform: scale(1.02);
        border-color: rgba(255, 0, 204, 0.5);
        box-shadow: 0 10px 30px rgba(255,0,204,0.2);
    }
</style>
""", unsafe_allow_html=True)

st.title("🤖 AI Problem Solving Assignment")
st.markdown("---")

st.markdown("""
### Welcome to the assignment portal!

Please use the **sidebar navigation on the left** to switch between the two different applications:

<div class="landing-card">
<h4 style="color: #FF2B2B;">🧩 Problem 6: Sudoku Solver</h4>
An interactive, premium-designed Sudoku grid that uses the Constraint Satisfaction Problem (CSP) backtracking algorithm to automatically solve puzzles.
</div>

<div class="landing-card">
<h4 style="color: #00f2fe;">📈 Problem 18: Student Predictor</h4>
A Machine Learning application that uses a Random Forest Regressor to predict student exam scores based on hours studied and attendance.
</div>

<h3 style="text-align: center; margin-top: 30px;">👈 Click the links in the sidebar to get started!</h3>
""", unsafe_allow_html=True)
