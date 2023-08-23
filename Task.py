import datetime
from Speak import speak
def Time():
    time=datetime.datetime.now().strftime("%H pass %M minutes %S seconds")
    speak(f"the time is {time}")
def Date():
    date=datetime.datetime.now().strftime("%d of %B %Y")
    speak(f"the date is {date}")

def NonInputExecution(query):
    query=str(query)
    if "time" in query:
        Time()

    elif "date" in query:
        Date()
