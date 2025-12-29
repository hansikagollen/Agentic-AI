import streamlit as st
import speech_recognition as sr

from voice import speak_telugu
from agent.agent import build_agent


# -----------------------------
# Streamlit Page Setup
# -----------------------------
st.set_page_config(page_title="Telugu Scheme Assistant", layout="centered")

st.title("🏛️ Telugu Voice-Based Government Scheme AI Agent")
st.write("Speak in Telugu to know about government welfare schemes.")

# Build LangGraph agent once
agent = build_agent()


# -----------------------------
# Audio Input (Browser-based)
# -----------------------------
audio_bytes = st.audio_input("🎤 Tap and speak Telugu")

if audio_bytes is not None:
    # 🔊 Play back recorded audio (for user confirmation)
    st.audio(audio_bytes, format="audio/wav")

    # Save audio to temporary WAV file
    with open("input.wav", "wb") as f:
        f.write(audio_bytes.getvalue())

    # Speech-to-Text
    recognizer = sr.Recognizer()
    with sr.AudioFile("input.wav") as source:
        audio_data = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio_data, language="te-IN")
        st.success(f"📝 You said: {text}")

        # -----------------------------
        # Initialize Agent State
        # -----------------------------
        initial_state = {
            "name": None,
            "age": None,
            "income": None,
            "scheme": None,
            "result": None,
            "reasoning": []
        }

        # ⚠️ Simple demo extraction (can be improved later)
        for word in text.split():
            if word.isdigit():
                initial_state["age"] = int(word)

        # Invoke LangGraph agent
        final_state = agent.invoke(initial_state)

        # -----------------------------
        # Show Agent Reasoning
        # -----------------------------
        st.subheader("🧠 Agent Reasoning")
        for step in final_state.get("reasoning", []):
            st.write("•", step)

        # -----------------------------
        # Final Response
        # -----------------------------
        if final_state["result"] == "ELIGIBLE":
            reply = f"మీకు {final_state['scheme']} వర్తిస్తుంది. దరఖాస్తు విజయవంతంగా నమోదు చేయబడింది."
            st.success(reply)
            speak_telugu(reply)

        elif final_state["result"] == "NOT_ELIGIBLE":
            reply = "క్షమించండి, మీరు ప్రస్తుతం ఏ పథకానికి అర్హులు కాదు."
            st.warning(reply)
            speak_telugu(reply)

        else:
            reply = "దయచేసి మీ వయస్సు మరియు ఆదాయం వివరాలు చెప్పండి."
            st.info(reply)
            speak_telugu(reply)

    except sr.UnknownValueError:
        st.error("❌ మాటలు అర్థం కాలేదు. దయచేసి మళ్లీ స్పష్టంగా మాట్లాడండి.")
        speak_telugu("దయచేసి మళ్లీ స్పష్టంగా మాట్లాడండి.")

    except Exception as e:
        st.error("❌ Unexpected error occurred.")
        st.write(e)
