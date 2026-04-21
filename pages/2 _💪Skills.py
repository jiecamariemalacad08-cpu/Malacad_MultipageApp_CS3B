import streamlit as st

st.set_page_config(page_title="Skills", page_icon="⚡", layout="wide")
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 50%, #fdf2f8 100%);
    font-family: 'Segoe UI', sans-serif;
}

h1 {
    text-align: center;
    color: #1e3a8a;
    font-weight: 700;
    margin-bottom: 20px;
}

.card {
    background: rgba(255, 255, 255, 0.90);
    padding: 18px;
    border-radius: 16px;
    margin-bottom: 12px;
    box-shadow: 0 6px 14px rgba(0,0,0,0.08);
    border-left: 6px solid #3b82f6;
    transition: all 0.3s ease;
}

.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 18px rgba(0,0,0,0.12);
}

.card b {
    font-size: 16px;
    color: #1f2937;
}

.quote-box {
    background: rgba(255,255,255,0.75);
    padding: 18px;
    border-radius: 14px;
    text-align: center;
    font-style: italic;
    margin-top: 20px;
    color: #4b5563;
    border: 1px solid #dbeafe;
}

</style>
""", unsafe_allow_html=True)

st.title("⚡ My Skills")

st.markdown("""
<div class="quote-box">
    Skills are not just talents — they are reflections of passion, discipline, and growth 🌸
</div>
""", unsafe_allow_html=True)

skills = {
    "💃 Dancing": 70,
    "🎤 Communication Skills": 90,
    "🏐 Volleyball": 55,
    "🏡 Designing Exterior Design": 60,
    "🙎 Leadership Skills": 80
    
}
for skill, value in skills.items():
    st.markdown(f"""
    <div class="card">
        <b>{skill}</b>
    </div>
    """, unsafe_allow_html=True)
    st.progress(value)

st.markdown("### 🌟 Choose Your Favorite Skills")

selected = st.multiselect(
    "Select skills you like most:",
    list(skills.keys())
)

if selected:
    st.success(f"✨ You selected: {', '.join(selected)}")
else:
    st.info("Select a skill to highlight your favorites 💡")