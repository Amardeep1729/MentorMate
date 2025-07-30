import streamlit as st
from AIengine import get_ai_response
from VoiceOutput import speak_with_browser, stop_speaking
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Set page config
st.set_page_config(page_title="MentorMate", layout="wide")

# Initialize session state
if "chat" not in st.session_state:
    st.session_state.chat = []

# Title
st.markdown("""
    <h1 style='text-align: center; color: #ff4b4b;'>🤖 MentorMate</h1>
    <p style='text-align: center;'>Your AI mentor for programming, education & productivity</p>
""", unsafe_allow_html=True)

# User input (text)
user_input = st.text_input("Type your question here:", key="text_input")

# Buttons
col1, col2 = st.columns([1, 1])
clear_clicked = col1.button("🧹 Clear Chat")
speak_clicked = col2.button("🔊 Speak Last Response")

# Handle Clear Chat
if clear_clicked:
    stop_speaking()
    st.session_state.chat = []
    st.success("Chat history cleared.")
    st.stop()

# Handle Speak
if speak_clicked and st.session_state.chat:
    last_bot_msg = st.session_state.chat[-1][1]
    speak_with_browser(last_bot_msg)
    st.stop()

# Process new input
if user_input.strip():
    with st.spinner("MentorMate is thinking..."):
        response = get_ai_response(user_input)
        st.session_state.chat.append((user_input, response))
    
    # Clear text input from field and memory
    st.session_state["text_input"] = ""
    user_input = ""

# Chat history
st.markdown("---")
st.subheader("🧠 Chat History")

# Show in reverse order (latest at top)
for i, (user, bot) in enumerate(reversed(st.session_state.chat), start=1):
    st.markdown(f"**🧑 You:** {user}**")
    st.markdown(f"**🤖 MentorMate:** {bot}")
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button(f"🔊 Speak #{i}", key=f"speak_{i}"):
            speak_with_browser(bot)
            st.stop()
    with col2:
        if st.button(f"🛑 Stop #{i}", key=f"stop_{i}"):
            stop_speaking()
    st.markdown("---")
