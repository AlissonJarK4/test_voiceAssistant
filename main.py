import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
import wolframalpha
import json
import requests

print('loading your personal assistant')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', 'voices[1].id')

def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet():
    hour = datetime.datetime.now().hour
    text = ""
    if hour >= 0 and hour < 12:
        text = 'mornin, dude'
        speak(text)
        print(text)
    elif hour >= 12 and hour < 18:
        text = 'afternoon'
        speak(text)
        print(text)
    else:
        text = 'evening'
        speak(text)
        print(text)

def takeCommand():
    recognizer = sr.Recognizer()
    with sr.Microphone() as capturedAudio:
        print('i\'m hearing you...')
        listenedAudio = recognizer.listen(capturedAudio)

        try:
            textSpoken = recognizer.recognize_google(listenedAudio, language='en-us')
            print(f'you spoke this phrase ---> {textSpoken}\n')
        except:
            speak('i don\'t understand u')
            return 'None'

        return textSpoken

speak('loading your personal assistant')

if __name__ == '__main__':
    while True:
        speak('speak to me please')
        textSpoken = takeCommand().lower
        if textSpoken == 0:
            continue

        if 'bye' in textSpoken or 'goodbye' in textSpoken or 'stop' in textSpoken:
            speak('goodbye')
            print('goodbye')

        elif 'wikipedia' in textSpoken:
            speak('searching on wikipedia')
            textSpoken = textSpoken.replace('wikipedia', '')
            results = wikipedia.summary(textSpoken, sentences = 3)
            speak('i have found this')
            print(results)
            speak(results)

        elif 'open youtube' in textSpoken:
            webbrowser.open_new_tab('https://www.youtube.com')
            speak('youtube opened')
            time.sleep(5)
        elif 'open google' in textSpoken:
            webbrowser.open_new_tab('https://www.google.com')
            speak('google opened')
            time.sleep(5)
        elif 'open gmail' in textSpoken:
            webbrowser.open_new_tab('gmail.com')
            speak('gmail opened')
            time.sleep(5)

        elif 'time' in textSpoken:
            stringTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'the time now is {stringTime}]')

        elif 'search' in textSpoken:
            textSpoken = textSpoken.replace('search', '')
            webbrowser.open_new_tab(textSpoken)
            time.sleep()

        elif 'ask' in textSpoken:
            speak('i can resolve any operation, you just need to ask')
            question = takeCommand()
            app_id = 'E8GPH6-3ALEVWA3HX'
            client = wolframalpha.Client(app_id)
            resource = client.query(question)
            answer = next(resource.results).text
            speak(answer)
            print(answer)

        elif 'who are you' in textSpoken:
            speak('i\'m sophia')

        elif "weather" in textSpoken:
            api_key = "8ef61edcf1c576d65d836254e11ea420"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name = takeCommand()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")




