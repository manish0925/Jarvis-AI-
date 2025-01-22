import pyttsx3
import pywin32_system32
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import random
import pyautogui
import cv2  # Importing OpenCV for the camera feature

engine = pyttsx3.init()

def speak(audio) -> None:
    engine.say(audio)
    engine.runAndWait()

def time() -> None:
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)
    print("The current time is ", Time)

def date() -> None:
    day: int = datetime.datetime.now().day
    month: int = datetime.datetime.now().month
    year: int = datetime.datetime.now().year
    speak("the current date is")
    speak(day)
    speak(month)
    speak(year)
    print(f"The current date is {day}/{month}/{year}")

def wishme() -> None:
    print("Welcome back sir!!")
    speak("Welcome back sir!!")

    hour: int = datetime.datetime.now().hour
    if 4 <= hour < 12:
        speak("Good Morning Sir!!")
        print("Good Morning Sir!!")
    elif 12 <= hour < 16:
        speak("Good Afternoon Sir!!")
        print("Good Afternoon Sir!!")
    elif 16 <= hour < 24:
        speak("Good Evening Sir!!")
        print("Good Evening Sir!!")
    else:
        speak("Good Night Sir, See You Tommorrow")

    speak("Jarvis at your service sir, please tell me how may I help you.")
    print("Jarvis at your service sir, please tell me how may I help you.")

def screenshot() -> None:
    img = pyautogui.screenshot()
    img_path = os.path.expanduser("~\\Pictures\\ss.png")
    img.save(img_path)

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(query)

    except sr.UnknownValueError:
        speak("Sorry, I did not understand that.")
        return "Try Again"

    except sr.RequestError:
        speak("Sorry, my speech service is down.")
        return "Try Again"

    except Exception as e:
        print(e)
        speak("Please say that again")
        return "Try Again"

    return query

def open_camera():
    speak("Opening the system camera, sir.")
    print("Opening the system camera, sir.")
    
    # Initialize the system camera (camera index 0)
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Use cv2.CAP_DSHOW for DirectShow on Windows
    
    if not cap.isOpened():
        speak("Sorry, I couldn't access the system camera.")
        print("Sorry, I couldn't access the system camera.")
        return
    
    while True:
        ret, frame = cap.read()
        if not ret:
            speak("Camera feed is not working properly.")
            break

        cv2.imshow("System Camera", frame)

        # Instructions for the user
        print("Press 'c' to click a picture. Press 'q' to exit.")

        key = cv2.waitKey(1) & 0xFF
        if key == ord('c'):
            # Save the picture
            img_path = os.path.expanduser("~\\Pictures\\captured_image.png")
            cv2.imwrite(img_path, frame)
            speak("Picture has been clicked and saved.")
            print(f"Picture saved at: {img_path}")

        elif key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    speak("System camera closed.")
    print("System camera closed.")
def open_whatsapp():
    try:
        # Define the path to WhatsApp executable
        possible_paths = [
            "C:\\Program Files\\WindowsApps\\5319275A.WhatsAppDesktop_2.2345.5.0_x64__cv1g1gvanyjgm\\WhatsApp.exe",
            "C:\\Program Files\\WhatsApp\\WhatsApp.exe",
            "C:\\Users\\<YourUsername>\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
        ]

        # Check which path exists and use the first valid one
        whatsapp_path = next((path for path in possible_paths if os.path.exists(path)), None)

        if whatsapp_path:
            os.startfile(whatsapp_path)
            speak("Opening WhatsApp on your system, sir.")
            print("WhatsApp has been opened.")
        else:
            speak("WhatsApp is not installed in standard locations.")
            print("WhatsApp not found. Please check the installation path.")
    except Exception as e:
        speak("An error occurred while opening WhatsApp.")
        print(f"Error: {e}")


def open_chrome():
    try:
        # Define possible paths for Chrome
        possible_paths = [
            "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        ]

        # Check which path exists
        chrome_path = next((path for path in possible_paths if os.path.exists(path)), None)

        if chrome_path:
            os.startfile(chrome_path)
            speak("Opening Google Chrome.")
            print("Google Chrome has been opened.")
        else:
            speak("Google Chrome is not installed in standard locations.")
            print("Google Chrome not found. Please check its installation.")
    except Exception as e:
        speak("An error occurred while trying to open Google Chrome.")
        print(f"Error: {e}")
    





if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()
        if "time" in query:
            time()

        elif "date" in query:
            date()

        elif "open camera" in query:
            open_camera()

        elif "your name please" in query:
            speak("I'm JARVIS created by Mr. Manish and I'm a desktop voice assistant.")
            print("I'm JARVIS created by Mr. Manish and I'm a desktop voice assistant.")

        elif "kaise ho" in query:
            speak("I'm fine sir, What about you?")
            print("I'm fine sir, What about you?")

        elif "fine" in query or "good" in query:
            speak("Glad to hear that sir!!")
            print("Glad to hear that sir!!")

        elif "open wikipedia" in query:
            try:
                speak("Ok wait sir, I'm searching...")
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(query, sentences=2)
                print(result)
                speak(result)
            except:
                speak("Can't find this page sir, please ask something else")

        elif "open youtube" in query:
            wb.open("youtube.com")

        elif "open google" in query:
            wb.open("google.com")

        elif "open stack overflow" in query:
            wb.open("stackoverflow.com")
        elif "open whatsapp" in query:
            open_whatsapp()

        elif "open instagram" in query:
            wb.open("https://www.instagram.com/")

        elif "play music" in query:
            try:
                song_dir = os.path.expanduser("~\\Music")
                songs = [f for f in os.listdir(song_dir) if os.path.isfile(os.path.join(song_dir, f))]
        
                if not songs:
                    print("No songs found in the Music folder.")
                else:
                    song = random.choice(songs)
                    print(f"Playing: {song}")
                    os.startfile(os.path.join(song_dir, song))
            except Exception as e:
                print(f"An error occurred: {e}")

        elif "open chrome" in query:
            open_chrome()


        elif "search on chrome" in query:
            try:
                speak("What should I search?")
                print("What should I search?")
                chromePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                search = takecommand()
                wb.get(chromePath).open_new_tab(search)
                print(search)

            except Exception as e:
                speak("Can't open now, please try again later.")
                print("Can't open now, please try again later.")

        elif "remember that" in query:
            speak("What should I remember")
            data = takecommand()
            speak("You said me to remember that" + data)
            print("You said me to remember that " + str(data))
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()

        elif "do you remember anything" in query:
            remember = open("data.txt", "r")
            speak("You told me to remember that" + remember.read())
            print("You told me to remember that " + str(remember))

        elif "screenshot" in query:
            screenshot()
            speak("I've taken screenshot, please check it")

        elif "offline" in query:
            quit()
