import whisper

model = whisper.load_model("base")

def speech_to_text(audio):
    result = model.transcribe(audio, language="te")
    return result["text"]

print(speech_to_text("input.wav"))
