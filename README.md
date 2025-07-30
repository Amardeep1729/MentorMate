# 🤖 MentorMate

MentorMate is an AI-powered personal mentor built using **Streamlit**, **OpenAI**, and **Gemini (Google AI)**.  
It helps you with:

🎓 Learning • 👨‍💻 Programming • 💼 Career Guidance • ⏱️ Productivity

> ❌ Politely ignores unrelated questions like jokes, food, entertainment, or inappropriate topics.

---

## 🔧 Features

- 🔄 Gemini + GPT fallback (whichever responds first)
- 🔊 Voice Output using Web Speech API (reads answers aloud)
- 🧠 Context-aware responses that stay on-topic
- 🖥️ Streamlit-based web interface
- 🧹 **Clear Chat** button for resetting the session
- 📃 Chat history with readable formatting
- 🔊 **Speak** button to hear answers aloud
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

- Type your question in the input field
- MentorMate responds instantly
- Use 🔊 to hear responses
- Use 🧹 to clear chat history
---

## 📌 Notes

- Requires internet connection  
- Works best in **Chrome / Edge**  
- Only text input is supported
- API keys needed for Gemini and OpenAI (Free tiers available)  
- Voice output works via browser (no mic needed)

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
- 🔊 Web Speech API for voice output
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
