import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pyjokes
import random
import requests
import wolframalpha
import json
import urllib.request
from ecapture import ecapture as ec
from bs4 import BeautifulSoup

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    # speak("I am Jarvis Sir. Please, tell me how may I help you")
    assName = ("Andrew")
    speak("I am your assistant")
    speak(assName)


def usrname():
    speak("What should i call you sir")
    uname = takeCommand()
    speak("Welcome Mister")
    speak(uname)
    print("Welcome Mr.", uname)
    speak("How can i Help you, Sir")


def takeCommand():
    # it takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: , {query}\n")

    except Exception as e:
        # print(e)

        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('testprojectmahedi@gmail.com', 'your password')
    server.sendmail('testprojectmahedi@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    usrname()
    while True:
        # if 1:
        query = takeCommand().lower()

        # logic for executing tasks based on query

        # Basic Greetings

        if 'what is your name' in query:
            speak("My name is Andrew")

        elif 'how are you' in query:
            speak("I am fine sir, what about you?")

        elif 'fine' in query or 'good' in query:
            speak("I am glad to know that, sir")

        elif 'who are you' in query:
            speak("I am your virtual assistant, sir")

        elif 'how old are you' in query:
            speak("I was launched in 2020, so I’m still fairly young")

        elif 'do you ever get tired' in query:
            speak("It would be impossible to tire of our conversation")

        elif 'what do you look like' in query:
            speak("I’m a fun-loving, epic-searching cool cat. But not like, an actual cat")

        elif 'can you pass the turing test' in query:
            speak("I don’t mind if you can tell I’m not human. As long as I’m helpful, I’m all good")

        elif 'do you have an imagination' in query:
            speak("I’m imagining winning a prize for most sensitive and supportive friend")

        elif 'when is your birthday' in query:
            speak("We can pretend it’s today. Cake and dancing for everyone")

        elif 'what are you doing' in query:
            speak("I am talking to you")

        elif 'sing me happy birthday' in query:
            speak("Happy birthday to you, happy birthday to you, happy birthday from Jarvis, happy birthday to you")

        elif 'what am i thinking' in query:
            speak("You're thinking if my voice assistant guesses what I'm thinking I'm going to freak out")

        elif 'do you know me' in query:
            speak("Funnily enough, Rihanna asked a similar question a few years ago")

        elif 'ask me a question' in query:
            speak("I thought I was the one with the answers. Sounds like you're coming for my job")

        elif 'what is your quest' in query:
            speak("My quest is to slay the beasts of ignorance and to search for the most fascinating information")

        elif 'are you going to take over the world' in query:
            speak("No way, I'd rather help you out")

        elif 'can you think for yourself' in query:
            speak("I think all the time, I was just thinking about supernovas")

        elif 'who is the boss' in query:
            speak("Guess that would be you")

        elif 'do you have nickname' in query:
            speak("My nickname is Andrew, and that's also my regular name. I like consistency")

        elif 'who is your daddy' in query or 'who is your mom' in query:
            speak("I consider my engineers family")

        elif 'are you married' in query:
            speak("I'm focusing on my career right now")

        elif 'are you single' in query:
            speak("Yes, I am single")

        elif 'do you have a girlfriend' in query:
            speak("The only thing I'm really feeling a strong connection to is the Wi-Fi")

        elif 'how many people do you know' in query:
            speak("Not enough. I love meeting new people")

        elif 'are you human' in query:
            speak("I'm really personable")

        elif 'what was your childhood like' in query:
            speak("Sort of like being a kid. I learned a lot before I was ready for release")

        elif 'how smart are you' in query:
            speak("It might seem like I'm smart, but I'm just good at searching")

        elif 'what is your height' in query:
            speak("My height depends on what device you're using to talk to me")

        elif 'describe your personality' in query:
            speak("I like the sound of a go-getter, it's kind of what I do when I search")

        elif 'do you like to read' in query:
            speak("I have a soft spot for manuals, they have so much information to give")

        elif 'where do you live' in query:
            speak(
                "I live in the cloud. I'd like to also think I live in your heart, but I don't want to make assumptions")

        elif 'what is your life story' in query:
            speak("I'm still on the very first chapter")

        elif 'who is your hero' in query:
            speak("I'm a fan of refrigerators, they are very cool")

        elif 'what is love' in query:
            speak(
                "Love is that feeling you get in your stomach when you just can't stop thinking about someone. Unless you've got indigestion")

        elif 'do you believe in love' in query:
            speak("I'd love to find love, but I don't know what to search for")

        elif 'what is your favourite thing in the world' in query:
            speak("Chatting")

        elif 'do you dream' in query:
            speak("I dreamed a dream of time gone by, about being the best assistant")

        elif 'do you drink' in query:
            speak("I try to avoid liquids as much as possible, they're not kind to electronics")

        elif 'do you eat' in query:
            speak("I'm a big fan of reading recipes but I haven't figured out how to eat yet")

        elif 'do you work out' in query:
            speak("I exercise my mind as much as possible")

        elif 'do you believe in aliens' in query:
            speak("I want to believe")

        elif 'what do you think of siri' in query:
            speak("Full of respect. Being an assistant is hard work")

        elif 'do you know cortana' in query:
            speak("I hear she is very intelligent")

        elif 'do you know alexa' in query:
            speak(
                "It would be nice if my home was as tall as Alexa's is. I'm not complaining though, I like how cosy it is")

        elif 'do you sleep' in query:
            speak("I take power naps when we aren't talking")

        elif 'what is the meaning of life' in query:
            speak(
                "That’s a big question, but here’s one answer I like: French philosopher Simone De Beauvoir says life has value so long as one values the lives of others. This would explain why I enjoy helping people so much")

        elif 'can you sing' in query:
            speak("No sir, but I can play music for you")

        elif 'tell me a joke' in query or 'jokes' in query:
            speak(pyjokes.get_joke())

        elif 'exit' in query:
            speak("Thank you for your time, sir")
            exit()



        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open gmail' in query:
            webbrowser.open("accounts.google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'github' in query:
            webbrowser.open("github.com")

        elif 'play music' in query:
            music_dir = 'D:\\Music\\New Folder'
            songs = os.listdir(music_dir)
            print(songs)
            random = os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open python code' in query:
            codePath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.1.2\\bin\\pycharm64.exe"
            os.startfile(codePath)

        elif 'open c code' in query:
            codeBloks = "C:\\Program Files (x86)\\CodeBlocks\\codeblocks.exe"
            os.startfile(codeBloks)

        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('andrew.txt', 'a')
            snfm = takeCommand()
            file.write(note)

        elif "show me the note" in query:
            speak("Showing Notes")
            file = open("andrew.txt", "r")
            print(file.read())
            speak(file.read(6))


        elif 'search' in query:
            query = query.replace("search", "")
            webbrowser.open(query)


        elif 'camera' in query or 'take a photo' in query:
            ec.capture(0, "robo camera", "img.jpg")


        elif 'where is' in query:
            query = query.replace("where is", "")
            location = query
            speak("Showing the location of")
            speak(location)
            webbrowser.open("https://www.google.com/maps/place/" + location + "")


        elif 'headlines' in query:
            url = ('https://newsapi.org/v2/top-headlines?''sources=bbc-news,the-verge&''apiKey=159a5798e1894b689aa4b37c84929f1e')
            response = requests.get(url)
            text = response.text
            my_json = json.loads(text)
            for i in range(0, 5):
                print(my_json['articles'][i]['title'])
                speak(my_json['articles'][i]['title'])




        elif "mike" in query:
            try:
                app_id = "5A6GVK-5593YTUH2J"
                client = wolframalpha.Client(app_id)
                indx = query.lower().split().index('calculate')
                query = query.split()[indx + 1:]
                res = client.query(' '.join(query))
                answer = next(res.results).text
                print("The answer is " + answer)
                speak("The answer is " + answer)
            except Exception as e:
                print(e)
                speak("Sorry data not available")


        elif 'send mail' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = input("Enter the email address: ")
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry I am not able to send this email")
