import pandas as pd
import datetime
from plyer import notification
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
df = pd.read_excel("C:\\Users\\Yuvraj Da God\\Downloads\\Book.xlsx")
today = datetime.datetime.now().strftime("%d-%m")
print(today)
for index,item in df.iterrows():
    bd = item["birthday"]
    if today == bd:
        a = item["name"]
        notification1("Birthday Alert!", "It is "+a+"'s birthday today!!")
        speak("Yuvraj !! It is "+a+"'s birthday today ")