import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
from playsound import playsound
import os


r = sr.Recognizer()
translator = Translator()
while True:
    with sr.Microphone() as source:
        print("Speak now!")
        audio = r.listen(source)
        try:
            speech_text = r.recognize_google(audio)
            print(speech_text)
            if (speech_text == "exit"):
                break
            # Translate text
            translated_text = translator.translate(speech_text, dest='fr')
            print(translated_text.text)
            
            # Convert translated text to speech
            voice = gTTS(translated_text.text, lang='fr')
            voice.save('voice.mp3')
            playsound('voice.mp3')
            os.remove('voice.mp3')

        except sr.UnknownValueError:
            print('Could not understand')
        except sr.RequestError:
            print("Could not request result from Google")
