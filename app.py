import streamlit as st
from AIengine import get_ai_response
from VoiceOutput import speak_with_browser, stop_speaking
from dotenv import load_dotenv
import streamlit.components.v1 as components

# Load environment variables
load_dotenv()

# Streamlit page config
st.set_page_config(page_title="MentorMate", layout="wide")

# Session state for chat history
if "chat" not in st.session_state:
    st.session_state.chat = []

if "voice_input" not in st.session_state:
    st.session_state.voice_input = ""

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
    st.markdown("Click below to speak:")

    # Display-only speech box
    st.markdown("#### Recognized Speech:")
    st.markdown(
        f"<div id='speechBox' style='background-color:#222;padding:10px;border-radius:5px;color:white;min-height:40px;'>{st.session_state.voice_input}</div>",
        unsafe_allow_html=True
    )

    # Hidden input to sync with session state
    st.text_input("Hidden Voice Input", key="voice_input", label_visibility="collapsed", disabled=True)

    # JavaScript for speech recognition
    components.html(f"""
        <script>
        const doc = window.parent.document;
        const speechBox = doc.querySelector('#speechBox');
        const hiddenInput = doc.querySelector('input[data-testid="stTextInput"]');

        const btn = document.createElement('button');
        btn.innerText = '🎙️ Speak Now';
        btn.style.fontSize = '16px';
        btn.style.marginTop = '10px';
        btn.style.padding = '10px 20px';
        btn.style.backgroundColor = '#ff4b4b';
        btn.style.color = 'white';
        btn.style.border = 'none';
        btn.style.borderRadius = '6px';
        btn.style.cursor = 'pointer';

        btn.onclick = () => {{
            const recognition = new(window.SpeechRecognition || window.webkitSpeechRecognition)();
            recognition.lang = 'en-US';
            recognition.start();

            recognition.onresult = function(event) {{
                const speech = event.results[0][0].transcript;
                speechBox.innerText = speech;
                hiddenInput.value = speech;
                const inputEvent = new Event("input", {{ bubbles: true }});
                hiddenInput.dispatchEvent(inputEvent);
            }};
        }};

        document.body.appendChild(btn);
        </script>
    """, height=120)

    user_input = st.session_state.voice_input

# Process input
if user_input:
    with st.spinner("MentorMate is thinking..."):
        response = get_ai_response(user_input)
        st.session_state.chat.append((user_input, response))
        st.session_state.voice_input = ""  # Clear after processing

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
