import streamlit as st

st.set_page_config(page_title="About Me", page_icon="👩‍💻", layout="wide")

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #dbeafe 0%, #f0f9ff 50%, #fdf2f8 100%);
    font-family: 'Segoe UI', sans-serif;
}

h1 {
    text-align: center;
    color: #1e3a8a;
    font-weight: 700;
    margin-bottom: 20px;
}

.card {
    background: rgba(255, 255, 255, 0.85);
    border-radius: 18px;
    padding: 25px;
    margin: 15px 0;
    box-shadow: 0 8px 18px rgba(0,0,0,0.08);
    backdrop-filter: blur(10px);
    transition: all 0.3s ease;
    border-left: 6px solid #60a5fa;
}

.card:hover {
    transform: translateY(-6px);
    box-shadow: 0 12px 22px rgba(0,0,0,0.12);
}
.card h3 {
    color: #2563eb;
    margin-bottom: 12px;
    font-weight: 600;
}

.card p {
    color: #374151;
    font-size: 15px;
    line-height: 1.7;
}

.quote {
    background: rgba(255,255,255,0.7);
    padding: 18px;
    border-radius: 14px;
    text-align: center;
    font-style: italic;
    color: #4b5563;
    margin-top: 20px;
    border: 1px solid #dbeafe;
}

</style>
""", unsafe_allow_html=True)

st.title("👩‍💻 About Me")

st.markdown("""
<div class="card">
    <h3>✨ Who Am I?</h3>
    <p>
        I am a passionate working student here in DEBESMSCAT, persuing Bachelor of Science in Computer Science who enjoys exploring new things,
        learning new technologies,designing, creating meaningful projects and i'm also starting my own small business.
        I also believe in balancing ambition with peace while living my hopeless romantic life 🌸
    </p>
</div>
""", unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
        <h3>🎓 Education</h3>
        <p>📘 Bachelor of Science in Computer Science</p>
        <p>💡 Continuously learning programming, UI design, and system development</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h3>🎯 Goals</h3>
        <p>✔ Become financially successful</p>
        <p>✔ Build a peaceful and stable future</p>
        <p>✔ Travel and live a life full of purpose</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="quote">
    "Success for me is not just about money,  
    but having peace, freedom, helping others specially who expreienced sexual abuse and the life I truly deserve."
</div>
""", unsafe_allow_html=True)