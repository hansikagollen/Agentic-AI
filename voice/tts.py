from gtts import gTTS
import os

def speak_telugu(text):
    tts = gTTS(text=text, lang='te')
    tts.save("output.mp3")
    os.system("start output.mp3")  # windows

speak_telugu("మీకు స్వాగతం")
