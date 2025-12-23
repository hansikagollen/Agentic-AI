# 🏛️ Telugu Voice-Based  AI Agent

## 📌 Overview
This project is a **voice-first AI assistant** designed to help **Telugu-speaking users** understand and apply for government welfare schemes.  
It enables users to **interact entirely through voice**, making it accessible for rural and non-English-speaking citizens.

The system demonstrates an **Agentic AI workflow** that can:
- Listen to Telugu speech
- Convert speech to text
- Reason over user input
- Respond intelligently
- Speak back in Telugu

---

## 🎯 Problem Statement
Many government schemes fail to reach rural citizens due to:
- Language barriers
- Lack of digital literacy
- Complex application processes

This project addresses the problem by providing a **simple voice-based interface in Telugu**, allowing users to interact naturally without typing.

---

## ✨ Key Features
- 🎙️ **Voice-First Interaction** – Users speak in Telugu instead of typing
- 🧠 **Agentic Reasoning** – The agent can interpret user input and respond logically
- 🗣️ **Telugu Language Support** – Both input and output are in Telugu
- 🔊 **Text-to-Speech Output** – Replies are spoken back to the user
- 🌐 **Browser-Based Microphone Capture** – Ensures reliability across systems
- 📁 **Modular Project Design** – Clean separation of UI, logic, and speech components

---

## 🧠 System Architecture

Browser Microphone (Streamlit)
↓
Audio Input (.wav)
↓
Speech-to-Text (Google STT)
↓
Agent Reasoning Logic
↓
Text-to-Speech (gTTS Telugu)
↓
Audio Response


---

## 🛠️ Tech Stack
- **Frontend**: Streamlit
- **Speech-to-Text**: Google Speech Recognition API
- **Text-to-Speech**: gTTS (Google Text-to-Speech)
- **Programming Language**: Python
- **Agent Logic**: Rule-based / LLM-ready agent design

---

## 📂 Project Structure

Agentic-AI/
│
├── app.py # Main Streamlit application
├── voice.py # Telugu Text-to-Speech logic
├── agent/ # Agent reasoning logic
├── data/ # Data files 
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── .gitignore # Ignored files (venv, audio files, etc.)


---

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/hansikagollen/Agentic-AI.git
cd Agentic-AI

2️⃣ Create and Activate Virtual Environment
python -m venv venv
venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Application
streamlit run app.py
