import streamlit as st
from AIengine import get_ai_response
from VoiceOutput import speak_with_browser  # Removed stop_speaking since it's not used
from dotenv import load_dotenv
import os

load_dotenv()
st.set_page_config(page_title="MentorMate", layout="wide")

# --- Session State Init ---
if "chat" not in st.session_state:
    st.session_state.chat = []

# --- UI Header ---
st.markdown("""
    <h1 style='text-align: center; color: #ff4b4b;'>🤖 MentorMate</h1>
    <p style='text-align: center;'>Your AI mentor for programming, education & productivity</p>
""", unsafe_allow_html=True)

# --- Input ---
user_question = st.text_input("Type your question:")

# --- Submit Button ---
if st.button("Submit") and user_question.strip():
    with st.spinner("MentorMate is thinking..."):
        response = get_ai_response(user_question)
        st.session_state.chat.append((user_question, response))

# --- Clear Chat Button ---
if st.button("🧹 Clear Chat"):
    st.session_state.chat = []
    st.experimental_rerun()

# --- Chat History ---
st.markdown("---")
st.subheader("🧠 Chat History")

for i, (user, bot) in enumerate(st.session_state.chat[::-1]):
    st.markdown(f"**🧑 You:** {user}")
    st.markdown(f"**🤖 MentorMate:** {bot}")
    if st.button(f"🔊 Speak #{i}", key=f"speak_{i}"):
        speak_with_browser(bot)
    st.markdown("---")
