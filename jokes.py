import pyttsx3
import time

e = pyttsx3.init()
voices = e.getProperty('voices')
e.setProperty('voice', voices[1].id)
while True:
    
    s=input("Enter the thing u want to say: ")
    e.say(s)
    e.runAndWait()
    time.sleep(0.5)

