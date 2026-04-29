from plyer import notification
import time
import os
import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def notification1(title, msg):
    notification.notify(
                    title = title,
                    message = msg,
                    app_icon = "",
                    timeout = 8
                )
    
game_time = input("Do you want to start your game time for the day? (yes/y, no/n)")

if game_time.lower() == "yes" or game_time.lower() == "y":
    time.sleep(5)
    os.system("taskkill /f /im brave.exe")
    os.system("taskkill /f /im EpicGamesLauncher.exe")
    os.system("taskkill /f /im FortniteClient-Win64-Shipping.exe")
    notification1("*** Take Rest ***", "Rest is vital for better mental health, do some other work!!")
    speak("Stop playing games, not allowed")

else:
    print("Good decision !")