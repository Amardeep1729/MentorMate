import streamlit as st
from AIengine import get_ai_response
from VoiceOutput import speak_with_browser, stop_speaking
from dotenv import load_dotenv
import os
import streamlit.components.v1 as components
import uuid

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
    st.markdown("Click the button below and allow mic access to speak:")

    # Generate a unique ID so multiple voice buttons won't conflict
    speech_id = str(uuid.uuid4()).replace("-", "")

    # Placeholder to display captured voice
    speech_placeholder = st.empty()

    components.html(f"""
        <script>
        const speechButton = document.createElement("button");
        speechButton.innerText = "🎙️ Speak Now";
        speechButton.style.fontSize = "18px";
        speechButton.style.padding = "10px 20px";
        speechButton.style.marginTop = "10px";
        speechButton.onclick = () => {{
            var recognition = new(window.SpeechRecognition || window.webkitSpeechRecognition)();
            recognition.lang = 'en-US';
            recognition.start();
            
            recognition.onresult = function(event) {{
                const speech = event.results[0][0].transcript;
                const streamlitInput = window.parent.document.querySelector('iframe[srcdoc]').contentWindow;
                streamlitInput.postMessage({{ type: "streamlit:setComponentValue", value: speech }}, "*");
            }};
        }};
        document.body.appendChild(speechButton);
        </script>
    """, height=100, key=f"voice_{speech_id}")

    # Receive the result back from JS
    user_input = st.experimental_get_query_params().get("value", [""])[0]
    if user_input:
        st.success(f"Recognized: {user_input}")
# Process input
if user_input:
    with st.spinner("MentorMate is thinking..."):
        response = get_ai_response(user_input)
        st.session_state.chat.append((user_input, response))

# Display chat history
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
