import pyttsx3
def speak(Text):
    engine = pyttsx3.init('sapi5') #sapi5 - microsoft API for speach recognition.
    voices = engine.getProperty('voices')
    engine.setProperty('voices', voices[0].id) #choosing voice
    engine.setProperty('rate', 170) #speed at which it talks
    print("  ")
    print(f"A.I : {Text}")
    # engine.say(text=Text)
    engine.runAndWait()
    print("  ")
