# 🤖 Greeting Agent

A simple conversational agent built using Google's Agent Development Kit (ADK). This agent warmly greets users by name using the `gemini-2.0-flash` model.
---

## 📝 Description


The `greeting_agent` showcases a basic setup for building agents with the `google.adk.agents.Agent` class. It is designed to:

- Use a specific Gemini model (`gemini-2.0-flash`)
- Prompt users for their name
- Respond with a personalized greeting
---

## ✨ Features

- **Gemini-Powered**: Utilizes Google's `gemini-2.0-flash` for natural conversations
- **Gemini-Powered**: Utilizes Google's `gemini-2.0-flash` for natural conversations  
- **Personal Interaction**: Asks for the user's name and responds accordingly  
- **Minimal Setup**: Easy to understand and extend

---

## 📁 Project Structure
```
Basic Agent/
├── greeting_agent/
│ ├── init.py
│ └── agent.py
└── README.md
```

- `greeting_agent/__init__.py`: Makes the agent module importable  
- `greeting_agent/agent.py`: Core logic and agent definition  

---

## ⚙️ Requirements

- Python 3.9+
- `google-adk`
- `google-genai` (installed with `google-adk`)

---

## 🚀 Setup and Installation


1. **Clone the repository (if applicable):**
   ```bash
   git clone <repository-url>
   cd Basic-Agent
Create and activate a virtual environment:
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
Create a .env file in the root directory:
GOOGLE_API_KEY="YOUR_API_KEY_HERE"
Install dependencies:
pip install google-adk google-genai
💬 Usage

Activate the virtual environment (if not already active):
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
Run the agent using ADK CLI:
adk run greeting_agent
Example Interaction:
You: Hello
Agent: Hi there! What's your name?
You: My name is Ebube.
Agent: Hello Ebube! Nice to meet you.
📌 Notes

This is a basic example intended to help you understand how to define and launch a conversational agent using ADK. Feel free to extend it with more capabilities.

🧠 Author

Ebube Imoh
GitHub | LinkedIn