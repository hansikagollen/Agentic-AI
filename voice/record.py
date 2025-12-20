import sounddevice as sd
from scipy.io.wavfile import write

fs = 16000
seconds = 5

print("Speak now...")
recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
sd.wait()
write("input.wav", fs, recording)
print("Saved input.wav")
