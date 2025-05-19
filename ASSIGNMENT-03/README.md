# 🤖 StudyBuddy - AI Tutor Chat Agent

**StudyBuddy** is a console-based AI tutor chatbot built using the [Google Generative Language SDK](https://github.com/google/generative-ai-docs). It leverages the Gemini API to provide an interactive and supportive study assistant that helps students understand tough concepts, stay focused, and feel motivated.

---

## 🚀 Features

- 🧠 Intelligent chatbot using `gemini-2.0-flash` model
- 💬 Interactive console chat with real-time responses
- 📚 Friendly and encouraging tutor persona
- 📝 Automatically logs all conversations to `study_buddy_conversation.md`
- 🔐 Secure API key management via `.env` file
- ⚡ Asynchronous client support with `AsyncOpenAI`

---

## 🧰 Technologies Used

- Python 3.7+
- [agents SDK](https://github.com/google/agents-sdk)
- Google Gemini API (via OpenAI-like interface)
- `dotenv` for managing API keys securely

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/studybuddy.git
cd studybuddy


## 🧠 How It Works

1. **Loads your Gemini API key** from the `.env` file using `python-dotenv`.
2. **Initializes an `AsyncOpenAI` client** with the Gemini base URL to communicate with the Gemini model.
3. **Creates a chatbot agent** named **StudyBuddy** with friendly and helpful tutor-like instructions.
4. **Starts a terminal-based input loop**, allowing the user to interact with StudyBuddy in real time.
5. **Logs each conversation** (both user input and StudyBuddy's response) to a markdown file named `study_buddy_conversation.md` for easy review and tracking.




## 💬 Example Interaction

**🤖 StudyBuddy is ready to chat! Type 'exit' to quit.**

**👨‍🎓 You:** What are the benefits of studying with flashcards?  
**🤖 StudyBuddy:** Flashcards help you actively recall information, which strengthens memory. They're also great for spaced repetition!

**👨‍🎓 You:** exit  
**🤖 StudyBuddy:** Goodbye, and happy studying! 👋

