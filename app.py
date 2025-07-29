import streamlit as st
from AIengine import get_ai_response
from VoiceOutput import speak_with_browser, stop_speaking
from dotenv import load_dotenv
from streamlit_js_eval import streamlit_js_eval

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(page_title="MentorMate", layout="wide")

# Initialize session state
if "chat" not in st.session_state:
    st.session_state.chat = []

if "voice_input" not in st.session_state:
    st.session_state.voice_input = ""

# Header
st.markdown("""
    <h1 style='text-align: center; color: #ff4b4b;'>🤖 MentorMate</h1>
    <p style='text-align: center;'>Your AI mentor for programming, education & productivity</p>
""", unsafe_allow_html=True)

# Input mode toggle
mode = st.radio("Choose your input method:", ["📝 Text", "🎤 Voice"], horizontal=True)

# Input handling
user_input = ""

if mode == "📝 Text":
    user_input = st.text_input("Type your message:", key="text_input")

elif mode == "🎤 Voice":
    st.markdown("Click the button below and start speaking:")

    # Show recognized speech
    recognized = st.empty()

    # Run JS to capture voice
    result = streamlit_js_eval(
        js_expressions="""
        const sleep = ms => new Promise(r => setTimeout(r, ms));

        async function getSpeech() {
            const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
            recognition.lang = 'en-US';

            return await new Promise((resolve, reject) => {
                recognition.onresult = e => resolve(e.results[0][0].transcript);
                recognition.onerror = err => reject(err.error);
                recognition.start();
            });
        }

        getSpeech();
        """,
        key="voice_capture"
    )

    if result and isinstance(result, str):
        st.session_state.voice_input = result
        user_input = result
        recognized.markdown(f"#### Recognized Speech: `{result}`")

# Process AI response
if user_input:
    with st.spinner("MentorMate is thinking..."):
        response = get_ai_response(user_input)
        st.session_state.chat.append((user_input, response))
        st.session_state.voice_input = ""

# Chat history
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
