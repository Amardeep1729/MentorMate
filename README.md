# 🤖 MentorMate

MentorMate is a voice-enabled, AI-powered personal mentor built using **Streamlit**, **OpenAI**, and **Gemini (Google AI)**. It answers questions related to:

🎓 Learning • 👨‍💻 Programming • 💼 Career Guidance • ⏱️ Productivity

> ❌ It politely ignores unrelated questions like "how to cook" or "tell me a joke".

---

## 🔧 Features

- 🔄 Gemini + GPT fallback (whichever responds first)
- 🎙️ Voice Input (via browser — no PyAudio needed!)
- 🔊 Voice Output using Web Speech API
- 🧠 Contextual AI behavior (stays on-topic)
- 📜 Logging enabled
- 🖥️ Web interface built using **Streamlit**
- 🎨 Sleek, fast UI with chat history

---

## 🧰 Requirements

Install the dependencies:

```bash
pip install -r requirements.txt
```

---

## 🛠️ Setup

### 1. Clone this repo:

```bash
git clone https://github.com/yourusername/MentorMate.git
cd MentorMate
```

### 2. Create a `.env` file in the root folder:

```env
OPENAI_API_KEY=your_openai_key
GEMINI_API_KEY=your_gemini_key
```

### 3. Run the app:

```bash
streamlit run app.py
```

---

## 🖥️ How to Use

- Choose Voice or Text input  
- Type or Speak your question  
- Responses are shown on-screen and spoken via browser 

---

## 📌 Notes

- Requires internet connection  
- Works best in **Chrome / Edge**  
- API keys needed for Gemini and OpenAI (Free tiers available)  
- Browser must support JavaScript for voice features
- No external mic library needed (thanks to browser-based input/output!)

---

## ☁️ Deploy Online (Optional)

You can deploy it on:

- [Streamlit Cloud](https://streamlit.io/cloud)
- [Render](https://render.com/)
- [Vercel](https://vercel.com/)
- [HuggingFace Spaces](https://huggingface.co/spaces)

---

## 🙌 Made With

- 💡 Streamlit  
- 🧠 OpenAI API  
- ⚡ Google Gemini AI  
- 🎤  SpeechRecognition (for voice input, local use)

---

## 🧠 Example Questions

### ✅ Ask:

- “How can I learn Python faster?”  
- “Tips to stay focused while studying?”  
- “Should I choose data science or web dev?”

### ❌ Avoid:

- “How to cook biryani?”  
- “Tell me a joke”

---

**Built with 💻 + ❤️ for focused learners.**
