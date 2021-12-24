import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening now...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alex' in command:
                command = command.replace('alex', '')
                print(command)
    except:
        pass
    return command


def run_alex():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M %p')
        print(time)
        talk('The time right now is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk('This is what I found on the internet. ' + info)
    elif 'information' in command:
        person = command.replace('information', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif 'country' in command:
        talk('I am not from a country, I was made in Python')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('I did not understand, can you repeat?')


while True:
    run_alex()
