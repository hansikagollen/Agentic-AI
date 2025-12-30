# 🏛️ Telugu Voice-Based Government Scheme AI Agent

## 📌 Overview
A voice-first, agentic AI system designed to help Telugu-speaking users discover and apply for government welfare schemes.  
The system enables natural Telugu voice interaction, reasons about eligibility using an agent workflow, and performs actions such as saving applications to a persistent store.

This project demonstrates a **Level-3 Agentic AI system** using planning, execution, and reasoning.

---

## 🚀 Key Features

- 🗣️ **Telugu Voice Interaction**
  - Browser-based speech input using Streamlit
  - Telugu Speech-to-Text (Google Speech Recognition)
  - Telugu Text-to-Speech responses

- 🧠 **Agentic Reasoning**
  - Built using **LangGraph (Planner–Executor pattern)**
  - Explicit reasoning steps shown in the UI
  - Determines missing information and eligibility logic

- 💾 **Persistent Actions**
  - Eligible applications are saved to `applications.csv`
  - Acts as proof-of-work for agent execution

- ⚠️ **Robust Error Handling**
  - Handles silence, unrecognized speech, and incomplete inputs gracefully

---

## 🛠️ Tech Stack

| Component | Technology |
|---------|-----------|
Frontend UI | Streamlit |
Speech-to-Text | SpeechRecognition (Google STT) |
Text-to-Speech | gTTS (Telugu) |
Agent Framework | LangGraph |
Language | Python |
Persistence | CSV File |
Environment | Python Virtual Environment |

---

## 📂 Project Structure

Agentic-AI/
├── app.py # Streamlit UI + voice pipeline
├── voice.py # Telugu TTS logic
├── agent/
│ ├── init.py
│ ├── agent.py # LangGraph planner–executor agent
│ └── logic.py # Eligibility logic + CSV persistence
├── applications.csv # Auto-generated application records
├── requirements.txt
└── README.md


---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/hansikagollen/Agentic-AI.git
cd Agentic-AI

2️⃣ Create Virtual Environment
python -m venv venv

Activate:
Windows

venv\Scripts\Activate

▶️ Run the Application
streamlit run app.py

