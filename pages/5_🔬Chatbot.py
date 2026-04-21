import streamlit as st

st.set_page_config(page_title="Portfolio Chatbot", page_icon="🤖", layout="wide")

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

.chat-box {
    background: rgba(255, 255, 255, 0.90);
    padding: 20px;
    border-radius: 18px;
    margin-top: 15px;
    box-shadow: 0 8px 18px rgba(0,0,0,0.08);
    border-left: 6px solid #3b82f6;
}

.user-msg {
    background: #dbeafe;
    padding: 12px;
    border-radius: 12px;
    margin: 8px 0;
    color: #1e3a8a;
    font-weight: 500;
}

.bot-msg {
    background: #fce7f3;
    padding: 12px;
    border-radius: 12px;
    margin: 8px 0;
    color: #9d174d;
    font-weight: 500;
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

st.title("🤖 Portfolio Chatbot")

st.markdown("""
<div class="quote-box">
    Ask me anything about my portfolio, skills, or projects ✨
</div>
""", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("💭 Ask something about me:")

if st.button("🚀 Send"):
    if user_input:
        if "name" in user_input.lower():
            reply = "I'm Jieca Marie Malacad 👋"
        elif "skills" in user_input.lower():
            reply = "My skills include Dancing, Communication Skills, Playing Volleyball, Designing Exterior Design, and Leadership Skills💃🎤🏐🏡"
        elif "project" in user_input.lower():
            reply = "I created To-Do App, Hotel Reservation System, Library System, and Simple Snake Game App 📂🐍"
        elif "goal" in user_input.lower():
            reply = "My goal is to become successful, financially stable, and live a peaceful life 🌸"
        else:
            reply = "Thanks for your question 😊"

        st.session_state.messages.append(("You", user_input))
        st.session_state.messages.append(("Bot", reply))

st.markdown('<div class="chat-box">', unsafe_allow_html=True)

for sender, msg in st.session_state.messages:
    if sender == "You":
        st.markdown(f"""
        <div class="user-msg">
            🧑 <b>You:</b> {msg}
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="bot-msg">
            🤖 <b>Bot:</b> {msg}
        </div>
        """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)