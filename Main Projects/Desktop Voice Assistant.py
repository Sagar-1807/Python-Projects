import datetime
import os
import pyttsx3 # text to speech without intrnet
import wikipedia
import smtplib
import speech_recognition as sp
import pyaudio
import webbrowser
import random

engine=pyttsx3.init('sapi5')   #Microsoft driver for inbuiilt voice (api)
voices=engine.getProperty('voices')
#print(voices)      # get inbuiult voice
# print(voices[0].id)
engine.setProperty('voice',voices[0].id) # 0 for male , 1 for female


def speak(audio): # system (laptop will speak)
    engine.say(audio)
    engine.runAndWait()


def wishme():       #auto good morning,evening as per time
    hour=int(datetime.datetime.now().hour)# 24 hr format

    if hour >=0 and hour < 12:
        speak('Good Morning Sagar')
    elif hour >=12 and hour < 16:
        speak('Good Afternoon Sagar')
    elif hour >=16 and hour < 18:
        speak('Good  evening Sagar')
    else:
        speak('Good night Sagar')

def takecommands():
    '''speech_recognition module'''
    '''take input from laptop mic'''
    r=sp.Recognizer()

    with sp.Microphone() as soure:
        print('listening ur voice...')
        #r.pause_threshold=1 # system will respond after 1 sec of our voice
        audio=r.listen(soure)

    try:
        print('Recognizing..')
        query=r.recognize_google(audio,language='en-in')     # using googleengine
        print(f"Sagar said: {query}\n")
    except Exception as e:
        print('pls say again..')
        return "None"
    return query

if __name__=="__main__":
    wishme()
    speak('hi,how r u')
    while True:
        query=takecommands().lower()

        if 'wikipedia' in query:
            speak('Searching your subject in wikipedia')
            query=query.replace('wikipedia','')
            result=wikipedia.summary(query,sentences=2)
            speak('According to wikipedia')
            print(result)
            speak(result)

        elif 'open youtube' in query:
            speak('opening youtube in your edge browser')
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            speak('opening google in your edge browser')
            webbrowser.open('google.com')
        elif 'open naukri' in query:
            speak('opening naukri.com in your edge browser')
            webbrowser.open('naukri.com')

        elif 'play video' in query:
            music_dir='E:\\Video & songs\\Bollywood\\Hrithik & tiger shroff'
            songs=os.listdir(music_dir)
            print(songs)
            speak('playing video for you')
            os.startfile(os.path.join(music_dir,songs[random.randrange(0,len(songs)-1)]))
        elif 'time' in query:
            t=datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'sir the now time is {t}')
            print(t)
        elif 'open chrome' in query:
            chrom='C:\\Users\\sagar\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe'
            os.startfile(chrom)
            speak('opening google chrome for you')

        elif 'send mail to sagar' in query:
            chrom = 'C:\\Users\\sagar\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe'
            os.startfile(chrom)
            speak('opening google chrome for you')












































