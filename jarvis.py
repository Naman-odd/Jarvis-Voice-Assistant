import win32com.client
import datetime
import speech_recognition as sr
import wikipedia
import os
import webbrowser

speaker = win32com.client.Dispatch("SAPI.SpVoice")


paths = [
    "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe",
    "C:\\Program Files (x86)\\BraveSoftware\\Brave-Browser\\Application\\brave.exe",
    f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
]

brave_path = None
for path in paths:
    if os.path.exists(path):
        brave_path = path
        print(f"✅ Found Brave at: {path}")
        break

if brave_path:
    webbrowser.register('brave', None, webbrowser.BackgroundBrowser(brave_path))
else:
    print("❌ Brave not found! Using default browser")

def open_browser(url):
    if brave_path:
        webbrowser.get('brave').open(url)
    else:
        webbrowser.open(url)

def speak(audio):
    speaker.Speak(audio)

def greet():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("It is a fine morning Sir!")
    elif hour >= 12 and hour < 18:
        speak("Hope you had your brunch, Good Afternoon Sir!")
    else:
        speak("The wind is lovely, Good Evening Sir!")
    speak("I am Jarvis, how may I help you?")

def command():
    r = sr.Recognizer()
    r.energy_threshold = 100
    r.dynamic_energy_threshold = True

    with sr.Microphone() as source:
        print("Calibrating mic...")
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=10, phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")

    except sr.WaitTimeoutError:
        print("No speech detected")
        return "None"
    except sr.UnknownValueError:
        print("Could not understand, please speak again")
        return "None"
    except sr.RequestError:
        print("Check internet connection!")
        return "None"
    except Exception as e:
        print(f"Error: {e}")
        return "None"

    return query

if __name__ == "__main__":
    greet()  

    while True:  
        query = command().lower()

        if query == "none":
            continue  


        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(f'{query}', sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open instagram' in query:
            open_browser("https://instagram.com")

        elif 'open youtube' in query:
            open_browser("https://youtube.com")

        elif 'open google' in query:
            open_browser("https://google.com")

        elif 'open kaggle' in query:
            open_browser("https://kaggle.com")

        elif 'the weather' in query:
            open_browser("https://weather.com")

        elif 'the score' in query:
            open_browser("https://cricbuzz.com")

        elif 'open claude' in query or 'open cloud' in query:
            open_browser("https://claude.ai/new")


        elif 'play music' in query:
            music_dir = 'Urban Sound\\fold2'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open anaconda' in query:
            condapath = "C:\\Users\\khank\\anaconda3"
            os.startfile(condapath)

        elif 'discord' in query:
            calpath = "C:\\Users\\Asus\\AppData\\Local\\Discord\\app-1.0.9235"
            os.startfile(calpath)

        elif 'stop' in query or 'exit' in query:
            speak("Goodbye Sir!")
            break  

        
        elif 'open vs code' in query:
            os.startfile("C:\\Users\\Asus\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

        elif 'tell me a joke' in query:
            import pyjokes
            joke = pyjokes.get_joke()
            speak(joke)

        elif 'the date' in query:
            date = datetime.datetime.now().strftime("%B %d, %Y")
            speak(f"Sir, today is {date}")

        elif 'shutdown' in query:
            speak("Shutting down Sir!")
            os.system("shutdown /s /t 5")


        elif 'take screenshot' in query:
            import pyautogui
            pyautogui.screenshot("screenshot.png")
            speak("Screenshot taken Sir!")

