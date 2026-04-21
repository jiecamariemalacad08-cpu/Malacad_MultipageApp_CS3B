import streamlit as st
import random

st.set_page_config(page_title="Mini Games", page_icon="🎮", layout="wide")

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
}

.card {
    background: rgba(255,255,255,0.9);
    padding: 20px;
    border-radius: 18px;
    margin-top: 15px;
    box-shadow: 0 8px 18px rgba(0,0,0,0.08);
    border-left: 6px solid #3b82f6;
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

st.title("🎮 Mini Games")

st.markdown("""
<div class="quote-box">
Maglaro muna tayo HEHEHE ✨
</div>
""", unsafe_allow_html=True)

game = st.selectbox(
    "Choose a Game:",
    ["Guess My Favorite Color", "Lucky Number", "Rock Paper Scissors"]
)

if game == "Guess My Favorite Color":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("🎨 Guess My Favorite Color")

    answer = "Blue"
    guess = st.text_input("Enter your guess:")

    if st.button("Check Color"):
        if guess.lower() == answer:
            st.success("Correct! My favorite color is Blue 💙")
            st.balloons()
        else:
            st.error("Oops! Try again 😊")

    st.markdown("</div>", unsafe_allow_html=True)

elif game == "Lucky Number":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("🔢 Lucky Number Game")

    user_number = st.number_input("Pick a number from 1 to 10", 1, 10)

    if st.button("Try Your Luck"):
        lucky = random.randint(1, 10)

        if user_number == lucky:
            st.success(f"Wow! You guessed it right 🎉 Lucky Number was {lucky}")
            st.balloons()
        else:
            st.warning(f"Not this time 😅 Lucky Number was {lucky}")

    st.markdown("</div>", unsafe_allow_html=True)

elif game == "Rock Paper Scissors":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("✊ Rock Paper Scissors")

    choices = ["Rock", "Paper", "Scissors"]
    user_choice = st.selectbox("Choose:", choices)

    if st.button("Play"):
        bot_choice = random.choice(choices)
        st.write(f"🤖 Bot chose: {bot_choice}")

        if user_choice == bot_choice:
            st.info("It's a Draw 😄")
        elif (
            (user_choice == "Rock" and bot_choice == "Scissors") or
            (user_choice == "Paper" and bot_choice == "Rock") or
            (user_choice == "Scissors" and bot_choice == "Paper")
        ):
            st.success("You Win 🎉")
            st.balloons()
        else:
            st.error("Bot Wins 😅")

    st.markdown("</div>", unsafe_allow_html=True)