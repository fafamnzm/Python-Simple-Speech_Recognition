#pretty trivial work
#heavily inspired by the works of others especially brad traversy
import speech_recognition as sr
import webbrowser
from time import ctime
import  playsound, os, random
from gtts import gTTS

rec = sr.Recognizer()
def audioRecorder(question = False):
    with sr.Microphone() as source:
        if question:
            speak(question)
        vData = ""
        audio = rec.listen(source)
        try:
            vData = rec.recognize_google(audio)
        except sr.UnknownValueError:
            speak("I'm Sorry, I don't understand you!!")
        except sr.RequestError:
            speak("Sorry, I'm down and really don't feel like it now!!")
        return vData

def speak(audioStr):
    txtsp = gTTS(text=audioStr, lang= "en")
    rnd = random.randint(1, 100000000000)
    audioFile = "recorded_" + str(rnd) + ".mp3"
    txtsp.save(audioFile)
    playsound.playsound(audioFile)
    print(audioStr)
    os.remove(audioFile)

def responce(vData):
    if "what" and "my" and "name" in vData:
        speak("You are Faramarz")
    if "what" and "your" and  "name" in vData:
        speak("I'm Captain Jack Sparrow!")    
    if "what" and "time" in vData:
        speak(ctime())
    if "where are you" in vData:
        speak("wherever you want me")
    if "search" in vData:
        search = audioRecorder("What do you want me to search for?")
        url = "https://www.google.com/search?q=" + search
        webbrowser.get().open(url)
        speak("I found these for " + search)
    if "location" in vData:
        location = audioRecorder("Where do you want me to find on map?")
        url = "https://www.google.com/maps/place/" + location
        webbrowser.get().open(url)
        speak("This is where I found for " + location + " : ")
    if "exit" in vData:
        speak('thank you, bye bye')
        exit()
    if "thank you" in vData:
        speak('thank you, bye bye')
        exit()
    if "bye" in vData:
        speak('thank you, bye bye')
        exit()


speak("Hey gorgeous, Say something I'm giving up on you: ")

while True:
    Voice_Input = audioRecorder()
    #print(Voice_Input)
    responce(Voice_Input)