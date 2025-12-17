# AI Task Prioritization System

A Python-based task prioritization system designed using **Generative AI concepts**.  
The project demonstrates how traditional rule-based logic can be replaced with an AI-powered decision layer in a clean and modular backend architecture.

---

##  Project Overview

This project takes user-defined tasks and classifies them into **High, Medium, or Low priority**.

The system is designed with a **separate AI abstraction layer**, allowing easy integration with real Generative AI APIs (Gemini / OpenAI).  
During development, a fallback stub is used to ensure reliability and smooth testing without dependency on external APIs.

---

##  Key Concepts Demonstrated

- Backend development using Python
- Modular code structure (separation of concerns)
- GenAI integration design (text-in → decision-out)
- Secure API key handling using environment variables
- Use of stubs during development (industry best practice)
- Basic UI demo using Streamlit

---

##  Project Structure

ai-task-prioritizer/
│
├── ai_utils.py # AI logic (stub / replaceable with real API)
├── main.py # CLI-based execution
├── app.py # Streamlit demo UI
├── requirements.txt
├── README.md
└── .gitignore

---

##  How It Works

1. Tasks are provided as text input
2. Each task is processed individually
3. The AI layer (or stub) determines priority
4. The result is returned to the application layer
5. Output is displayed either in terminal or via Streamlit UI

---

##  Example Output

Finish DBMS assignment -> High

Buy groceries -> Low

Prepare for coding test -> High


---

##  Running the Project

### Run in Terminal

```bash```

python main.py

### Run Streamlit Demo
```bash```

streamlit run app.py

---

## About AI Integration
The system is designed to integrate with real Generative AI APIs such as:

Google Gemini

OpenAI GPT

Due to API access and quota limitations during development, a rule-based stub is used.
The AI logic is abstracted in ai_utils.py, making it easy to swap the stub with a live API when required.

This approach follows standard backend development practices.

---

## Future Improvements

Replace stub with live AI API integration

Improve prompt engineering for better prioritization

Add database support for persistent tasks

Deploy Streamlit demo online
