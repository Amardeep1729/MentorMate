import streamlit as st
from AIengine import get_ai_response
from VoiceInput import listen_to_user
from VoiceOutput import speak_with_browser
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Streamlit page config
st.set_page_config(page_title="MentorMate", layout="wide")

# Session state for chat history
if "chat" not in st.session_state:
    st.session_state.chat = []

# Title and description
st.markdown("""
    <h1 style='text-align: center; color: #ff4b4b;'>🤖 MentorMate</h1>
    <p style='text-align: center;'>Your AI mentor for programming, education & productivity</p>
""", unsafe_allow_html=True)

# Input mode selection
mode = st.radio("Choose your input method:", ["📝 Text", "🎤 Voice"], horizontal=True)

# Input field or voice input
user_input = ""
if mode == "📝 Text":
    user_input = st.text_input("Type your message:", key="text_input")
elif mode == "🎤 Voice":
    if st.button("🎙️ Speak Now"):
        with st.spinner("Listening..."):
            try:
                user_input = listen_to_user()
                st.success(f"You said: {user_input}")
            except Exception as e:
                st.error(f"Voice input failed: {e}")

# Process input
if user_input:
    with st.spinner("MentorMate is thinking..."):
        response = get_ai_response(user_input)
        st.session_state.chat.append((user_input, response))

# Display chat history
st.markdown("---")
st.subheader("🧠 Chat History")
for i, (user, bot) in enumerate(st.session_state.chat[::-1]):
    st.markdown(f"**🧑 You:** {user}")
    st.markdown(f"**🤖 MentorMate:** {bot}")
    if st.button(f"🔊 Speak #{i+1}", key=f"speak_{i}"):
        speak_with_browser(bot)
    st.markdown("---")
