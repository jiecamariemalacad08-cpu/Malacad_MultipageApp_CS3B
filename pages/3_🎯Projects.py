import streamlit as st

st.set_page_config(page_title="My Projects", page_icon="📂", layout="wide")

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
    padding: 22px;
    border-radius: 18px;
    margin-bottom: 16px;
    box-shadow: 0 8px 18px rgba(0,0,0,0.08);
    border-left: 6px solid #3b82f6;
    transition: all 0.3s ease;
}

.card:hover {
    transform: translateY(-6px);
    box-shadow: 0 12px 22px rgba(0,0,0,0.12);
}

.card h3 {
    color: #2563eb;
    margin-bottom: 10px;
    font-weight: 600;
}

.card p {
    color: #374151;
    font-size: 15px;
    line-height: 1.6;
}

.quote-box {
    background: rgba(255,255,255,0.75);
    padding: 18px;
    border-radius: 14px;
    text-align: center;
    font-style: italic;
    margin-bottom: 20px;
    color: #4b5563;
    border: 1px solid #dbeafe;
}

</style>
""", unsafe_allow_html=True)

st.title("📂 My Projects")

st.markdown("""
<div class="quote-box">
    Every project is a step closer to becoming the developer I dream to be and most importantly is to get that diploma 🚀
</div>
""", unsafe_allow_html=True)

projects = {
    "📝 To-Do App": "A simple task management system that helps organize daily activities and improve productivity.",
    "🏨 Hotel Reservation": "A simple booking system for managing hotel room reservations efficiently.",
    "📚 Library System": "A borrowing books system for tracking borrowed and returned books.",
    "🐍 Snake Game App": "A simple Python snake game system designed for fun and learning game development basics."
}

search = st.text_input("🔍 Search project")

for name, desc in projects.items():
    if search.lower() in name.lower():
        st.markdown(f"""
        <div class="card">
            <h3>{name}</h3>
            <p>{desc}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("### 🌟 Which project do you like most?")

favorite = st.selectbox(
    "Choose your favorite project:",
    list(projects.keys())
)

if favorite:
    st.success(f"✨ Your favorite project is: {favorite}")