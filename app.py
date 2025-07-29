import streamlit as st
from AIengine import get_ai_response
from VoiceOutput import speak_with_browser, stop_speaking
from dotenv import load_dotenv
import streamlit.components.v1 as components

# Load .env variables
load_dotenv()

# Streamlit config
st.set_page_config(page_title="MentorMate", layout="wide")

# Initialize session state
if "chat" not in st.session_state:
    st.session_state.chat = []

if "voice_input" not in st.session_state:
    st.session_state.voice_input = ""

# Title
st.markdown("""
    <h1 style='text-align: center; color: #ff4b4b;'>🤖 MentorMate</h1>
    <p style='text-align: center;'>Your AI mentor for programming, education & productivity</p>
""", unsafe_allow_html=True)

# Input mode
mode = st.radio("Choose your input method:", ["📝 Text", "🎤 Voice"], horizontal=True)

# Input handler
user_input = ""

if mode == "📝 Text":
    user_input = st.text_input("Type your message:", key="text_input")

elif mode == "🎤 Voice":
    st.markdown("Click the button below and start speaking:")
    
    # Text input to sync recognized text
    user_input = st.text_input("Recognized Speech:", key="voice_input")

    # JS for voice recognition
    components.html("""
        <script>
        const inputBox = window.document.querySelector('input[data-testid="stTextInput"]');

        const button = document.createElement('button');
        button.innerText = "🎙️ Speak Now";
        button.style.padding = "10px 20px";
        button.style.fontSize = "16px";
        button.style.backgroundColor = "#ff4b4b";
        button.style.color = "white";
        button.style.border = "none";
        button.style.borderRadius = "8px";
        button.style.marginTop = "10px";
        button.style.cursor = "pointer";

        button.onclick = () => {
            const recognition = new(window.SpeechRecognition || window.webkitSpeechRecognition)();
            recognition.lang = 'en-US';
            recognition.start();

            recognition.onresult = function(event) {
                const speech = event.results[0][0].transcript;
                inputBox.value = speech;
                const inputEvent = new Event('input', { bubbles: true });
                inputBox.dispatchEvent(inputEvent);
            };
        };

        document.body.appendChild(button);
        </script>
    """, height=130)

# Run AI
if user_input:
    with st.spinner("MentorMate is thinking..."):
        response = get_ai_response(user_input)
        st.session_state.chat.append((user_input, response))
        st.session_state.voice_input = ""  # Clear it after processing

# Display chat
st.markdown("---")
st.subheader("🧠 Chat History")

if st.button("🧹 Clear Chat"):
    st.session_state.chat = []
    st.success("Chat history cleared.")

for i, (user, bot) in enumerate(st.session_state.chat[::-1]):
    st.markdown(f"**🧑 You:** {user}")
    st.markdown(f"**🤖 MentorMate:** {bot}")
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button(f"🔊 Speak #{i+1}", key=f"speak_{i}"):
            speak_with_browser(bot)
    with col2:
        if st.button(f"🛑 Stop #{i+1}", key=f"stop_{i}"):
            stop_speaking()
    st.markdown("---")
