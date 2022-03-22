import datetime
import speech_recognition as sp
import pyttsx3
import pywhatkit
import wikipedia
import pyjokes

listener = sp.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sp.Microphone() as source:
            print('Listening..')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                talk(command)

    except:
        pass
    return command


def run_Assitant():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        print(song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M:%S %p')
        talk('Current time is' + time)
        print(time)

    elif 'who is' in command:
        person = command.replace('who', '')
        info = wikipedia.summary(person, 3)
        print(info)
        talk(info)

    elif 'single' in command:
        talk('I am in relation with wifi, computer and technology')

    elif 'created' in command:
        talk('I am created by Shayan Hassan currently enrolled in Fast University in Bachelors of Computer Science.')
        print('I am created by Shayan Hassan currently enrolled in Fast University in Bachelors of Computer Science.')
    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'close' in command:
        talk('I am going to sleep, had a great time with you.')
        print('Bye see you again!!!!!')

    else:
        talk('Please repeat the command Again.')


while True:
    run_Assitant()
