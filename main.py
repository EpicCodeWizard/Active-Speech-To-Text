import speech_recognition
import pyttsx3

recognizerEngine = speech_recognition.Recognizer()
speakerEngine = pyttsx3.init()

def SpeakText(command):
  speakerEngine.say(command)
  speakerEngine.runAndWait()

while True:
  recognizerEngine.adjust_for_ambient_noise(source2, duration=0.2)
  MyText = recognizerEngine.recognize_google(recognizerEngine.listen(sr.Microphone())).lower()
  print(MyText)
  SpeakText(MyText)
