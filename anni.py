#By the way meet our new friend Anni.

import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[1].id) # Shows us the installed voices in our system
#Simply Acc to my system 0 = Male voice and 1 = female voice

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    # This Logic wishes me according to the time.
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon") 
    
    else:
        speak("GOod evening")

    speak("I am Annni. Please tell me, How may I help you")
def takeCommand():
    # it takes microphone input from user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in') #Setting language to English-India
        print(f"user said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please....")
        return "None"

    return query

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        #logic for executing queries
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) #Prints only two sentences from wikipedia
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com") #opens browser

        elif 'open google' in query:
            webbrowser.open("google.com") #Opens google

        elif 'open stackoverflow' in query:
            webbrowser.opne("stackoverflow.com") #Opens my favorite stack over flow[lol]

        elif 'play music' in query:
            music_dir = 'C:\\sdcard\\Music\\Ashique 2' #Opens my music directory and plays music
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'The time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S") #shows me date and time
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Tharun\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" #Opens My visual studio code
            os.startfile(codePath)

        elif 'quit' in query:
            exit()
        

