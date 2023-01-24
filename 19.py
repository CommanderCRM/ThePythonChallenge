import email
import wave

with open("email.txt", "rb") as email_file:
  message = email_file.read().decode()

mail = email.message_from_string(message)
audio = mail.get_payload(0).get_payload(decode=True)

with open("indian.wav", "wb") as audio_file:
  audio_file.write(audio)

# changing the original audio file
with wave.open('indian.wav', 'rb') as w, wave.open("result.wav", "wb") as h:
  h.setnchannels(w.getnchannels())
  h.setsampwidth(w.getsampwidth() // 2)
  h.setframerate(w.getframerate() * 2)
  frames = w.readframes(w.getnframes())
  h.writeframes(frames)
