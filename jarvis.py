import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pywhatkit
import pyautogui


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak('good morning')
    elif hour <= 0 and hour >=12:
        speak('good afternoon')
    else:
        speak("good evening")
    speak("I am jarvis sir, Please tell me how may I help you")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listining...")
        r.pause_threshold = 0.5 
        
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"user said: {query} \n ")
    except Exception as e:
        print(e) 

        print("Say that again please...")
        return"None"
    return query

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        print("Recognizing...")
        return recognizer.recognize_google(audio)


if __name__=="__main__":
    wishMe()
    while True:
 
        query = takecommand().lower()
        
        if "wikipedia" in query:
            speak("Searching wikipedia...")
            query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences = 3 )
            speak("According to wikipedia")
            print(results)
            speak(results)
            
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
            
        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow")

        elif "open github" in query:
             webbrowser.open("github.com")
            
        elif "open chatgpt" in query:
             webbrowser.open("chatgpt.com")
                
        elif "open google" in query:
            speak("Sir, what should i search on google")
            cmd = takecommand().lower()
            webbrowser.open(f"{cmd}")
    
        elif "tell me time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}")

        elif "shutdown my pc" in query:
            speak("Shutting down the system, goodbye!")
            os.system("shutdown /s /f /t 1")
            break
            
        elif "restart my pc" in query:
            speak("Restarting the system, please wait!")
            os.system("shutdown /r /f /t 1")
            break

        elif "send message on whatsapp" in query:
            speak("who do you want me to send message")
            person = listen()
            speak("What message do you want to send?")
            message = listen()  
            speak(f"your message is {message}.Is this message correct, would you like me to send it")
            confirm = listen().lower()
            if "yes" in confirm:
              pywhatkit.sendwhatmsg("+923183367360", message, datetime.datetime.now().hour, datetime.datetime.now().minute + 1)\
        
            elif "no" in confirm:
              speak("Your message has not been sent")

        elif "open" in query:
            query = query.replace("open" , "")
            pyautogui . press( "super" )
            pyautogui . typewrite (query)
            pyautogui. sleep(2)
            pyautogui . press ( " enter " )

        elif "exit" in query:
            speak("Good bye sir. Have a good day!")
            break
