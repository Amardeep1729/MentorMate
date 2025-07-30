import streamlit as st
from AIengine import get_ai_response
from VoiceOutput import speak_with_browser, stop_speaking
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Streamlit page config
st.set_page_config(page_title="MentorMate", layout="wide")

# Session state init
if "chat" not in st.session_state:
    st.session_state.chat = []

# Title
st.markdown("""
    <h1 style='text-align: center; color: #ff4b4b;'>🤖 MentorMate</h1>
    <p style='text-align: center;'>Your AI mentor for programming, education & productivity</p>
""", unsafe_allow_html=True)

# --- Input field ---
user_input = st.text_input("Type your question here:", key="user_message")

# --- Clear Chat Button ---
if st.button("🧹 Clear Chat"):
    st.session_state.chat = []
    st.success("Chat history cleared.")
    st.stop()

# --- Chat History ---
st.markdown("---")
st.subheader("🧠 Chat History")

for i, (user, bot) in enumerate(st.session_state.chat[::-1]):
    st.markdown(f"**🧑 You:** {user}")
    st.markdown(f"**🤖 MentorMate:** {bot}")
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button(f"🔊 Speak #{i+1}", key=f"speak_{i}"):
            speak_with_browser(bot)
            st.stop()
    with col2:
        if st.button(f"🛑 Stop #{i+1}", key=f"stop_{i}"):
            stop_speaking()
            st.stop()
    st.markdown("---")

# --- Process input ---
if user_input:
    with st.spinner("MentorMate is thinking..."):
        response = get_ai_response(user_input)
        st.session_state.chat.append((user_input, response))

    # Force rerun to clear input field after processing
    st.experimental_rerun()
