import streamlit as st

st.set_page_config(page_title="Contact Me", page_icon="📞", layout="wide")

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
    padding: 25px;
    border-radius: 18px;
    margin-top: 20px;
    box-shadow: 0 8px 18px rgba(0,0,0,0.08);
    border-left: 6px solid #3b82f6;
    transition: all 0.3s ease;
}

.card:hover {
    transform: translateY(-6px);
    box-shadow: 0 12px 22px rgba(0,0,0,0.12);
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

.card p {
    color: #374151;
    font-size: 15px;
    line-height: 1.8;
}

</style>
""", unsafe_allow_html=True)

st.title("📞 Contact Me")

st.markdown("""
<div class="quote-box">
    Communication is the key, and every great opportunity starts with a simple message ✨
</div>
""", unsafe_allow_html=True)

with st.form("contact"):
    st.markdown("### 💌 Send Me a Message")

    name = st.text_input("👤 Name")
    email = st.text_input("📧 Email")
    message = st.text_area("📝 Message")

    submit = st.form_submit_button("🚀 Send Message")

    if submit:
        if name and email and message:
            st.success("✅ Message sent successfully!")
            st.balloons()
        else:
            st.error("⚠ Please fill in all fields")

st.markdown("""
<div class="card">
    <h3>🌐 Connect With Me</h3>
    <p>🐙 GitHub: <a href="https://github.com/jiecamariemalacad08-cpu" target="_blank">github.com/jiecamariemalacad08-cpu</a></p>
    <p>📘 Facebook: <a href="https://www.facebook.com/share/1DJWEYHYTY/" target="_blank">facebook.com/share/1DJWEYHYTY</a></p>
    <p>📸 Instagram: <a href="https://www.instagram.com/mj_mlcd?igsh=dzNlODdscWc1d2N/" target="_blank">@mj_mlcd</a></p>
    <p>💡 Just Message Me!</p>
</div>
""", unsafe_allow_html=True)
