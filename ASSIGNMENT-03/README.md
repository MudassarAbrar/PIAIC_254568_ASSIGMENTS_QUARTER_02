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

You: make  a quiz on python advance topics containing atleast 10 multiple choice questions
StudyBuddy: Alright, let's test your Python advanced knowledge! Don't worry if you don't know all the answers, just try your best and we can review them together. Good luck, you've got this!

**Python Advanced Topics Quiz**

1.  **What is a decorator in Python?**

    a)  A design pattern for creating objects
    b)  A way to add new functionality to an existing function or class
    c)  A type of loop
    d)  A module for handling exceptions

2.  **Which of the following is the correct way to use a context manager?**

    a)  `try: ... finally: ...`
    b)  `with open('file.txt', 'r') as f: ...`
    c)  `if ... else: ...`
    d)  `for i in range(10): ...`

3.  **What is the purpose of the `__slots__` attribute in a Python class?**

    a)  To define the order of attributes
    b)  To prevent the creation of new attributes after instantiation, saving memory
    c)  To make attributes private
    d)  To define default values for attributes

4.  **Which module is commonly used for asynchronous programming in Python?**

    a)  `threading`
    b)  `multiprocessing`
    c)  `asyncio`
    d)  `socket`

5.  **What is the Global Interpreter Lock (GIL) in Python?**

    a)  A lock that prevents multiple threads from executing Python bytecode concurrently in a single process
    b)  A lock that prevents access to global variables
    c)  A lock that ensures only one process can run at a time
    d)  A lock that protects memory from being overwritten

6.  **Which of the following is NOT a valid use of metaclasses?**

    a)  Automating attribute creation
    b)  Enforcing coding standards
    c)  Creating singleton classes
    d)  Defining functions

7.  **What is the purpose of the `functools` module?**

    a)  To provide mathematical functions
    b)  To provide higher-order functions and operations on callable objects
    c)  To provide file I/O operations
    d)  To provide network programming tools

8.  **Which of the following is an example of a generator expression?**

    a)  `[x for x in range(10)]`
    b)  `(x for x in range(10))`
    c)  `{x for x in range(10)}`
    d)  `x for x in range(10)`

9.  **What is the purpose of the `collections` module in Python?**

    a)  To provide mathematical data structures
    b)  To provide alternative container datatypes
    c)  To provide regular expression operations
    d)  To provide operating system interfaces

10. **What is the difference between `multiprocessing` and `threading` in Python?**

    a)  `multiprocessing` uses threads, while `threading` uses processes
    b)  `multiprocessing` bypasses the GIL, allowing for true parallelism, while `threading` is limited by the GIL
    c)  `threading` is faster than `multiprocessing`
    d)  There is no difference

***

Take your time and think through each question. Once you're done, let me know and we can go over the answers together! Remember, it's all about learning! Don't be discouraged if you find it challenging, this is an advanced topic! You're doing great just by trying!












