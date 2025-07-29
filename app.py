import streamlit as st
from AIengine import get_ai_response
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
    st.text_input("Recognized Speech:", key="voice_input")

    st.components.v1.html("""
        <script>
        const streamlitInput = window.parent.document.querySelector('input[data-testid="stTextInput"]');

        var button = document.createElement("button");
        button.innerText = "🎙️ Speak Now";
        button.style.fontSize = "18px";
        button.style.padding = "10px 20px";
        button.style.marginTop = "10px";
        button.onclick = () => {
            var recognition = new(window.SpeechRecognition || window.webkitSpeechRecognition)();
            recognition.lang = 'en-US';
            recognition.start();

            recognition.onresult = function(event) {
                const speech = event.results[0][0].transcript;
                streamlitInput.value = speech;
                const inputEvent = new Event("input", { bubbles: true });
                streamlitInput.dispatchEvent(inputEvent);
            };
        };
        document.body.appendChild(button);
        </script>
    """, height=100)

    user_input = st.session_state.get("voice_input", "")

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
