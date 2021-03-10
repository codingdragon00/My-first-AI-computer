import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices =engine.getProperty("voices")
engine.setProperty("voices", voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
   try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "computer" in command:
                command = command.replace("computer", "")
                print(command)
   except:
       pass
   return command

def run_computer():
    command = take_command()
    print(command)
    if "play" in command:
        song = command.replace("play", "")
        talk("playing" + song)
        pywhatkit.playonyt(song)
    elif "time" in command:
        time = datetime.datetime.now().strftime("%H:%M %p")
        print(time)
        talk("My master, time is " + time)
    elif "who is " in command:
        person = command.replace("who is ", "")
        info =wikipedia.summary(person, 4)     #lines from wikipedia.
        print(info)
        talk(info)
    elif "weather" in command:
        talk("sorry, i dont know and dont want you to know as well")
    elif "are you single" in command:
        talk("I am currently dating hard drive")
    elif "joke" in command:
        talk(pyjokes.get_joke())
    else:
        talk("now i feel stupid, master can you please say that again. ")


while True:
    run_computer()