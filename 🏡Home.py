import streamlit as st
import os

st.set_page_config(page_title="My Portfolio", layout="wide")

theme = st.sidebar.toggle("🌙 Dark Mode")

if theme:
    bg = "linear-gradient(135deg, #0f2027, #203a43, #2c5364)"
else:
    bg = "linear-gradient(135deg, #667eea, #764ba2)"

st.markdown(f"""
<style>
.stApp {{
    background: {bg};
    color: white;
}}

h1, h2, h3, p, label {{
    color: white !important;
}}

.card {{
    background: rgba(255,255,255,0.18);
    padding: 20px;
    border-radius: 15px;
    backdrop-filter: blur(10px);
    box-shadow: 0px 4px 20px rgba(0,0,0,0.3);
    margin-bottom: 20px;
    transition: transform 0.3s;
}}

.card:hover {{
    transform: scale(1.03);
}}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
<h1 style="text-align:center;">🌐 My Portfolio</h1>
<h3 style="text-align:center;">💻 Aspiring Exterior Designer | 🚀 Creative Thinker</h3>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([2,1])

with col1:
    st.markdown("""
    <div class="card">
    <h2>Hi, I'm Jieca Marie Juarez Malacad 👋</h2>
    <p>🎓 Bachelor of Science in Computer Science Student</p>
    <p>💡 Passionate about creating things that make me happy and building my own business</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    
    image_path = os.path.join(os.path.dirname(__file__), "myphoto.jpeg")

    if os.path.exists(image_path):
        st.image(image_path, width=250)
    else:
        st.warning("Profile photo not found. Please check myphoto.jpeg location.")

st.markdown("---")

name = st.text_input("Enter your name")

if st.button("🚀 Enter Portfolio"):
    if name:
        st.balloons()
        st.success(f"Welcome, {name}! Enjoy exploring 💯")
    else:
        st.warning("Please enter your name first.")