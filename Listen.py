import speech_recognition as sr

def Listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        audio = r.listen(source,0,5) #here we can set time for the assistant to hear our input. like here it is 5sec.

    try:
        print("recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"you said: {query}\n")

    except Exception as e:

        print("please say again...")
        return "none"
    return query

Listen()