import pyttsx3
import speech_recognition as sr
import eel
import time

def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices') 
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 174)
    eel.DisplayMessage(text)
    engine.say(text)
    engine.runAndWait()

def takecommand():
    
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print('Escuchando.....')
        eel.DisplayMessage('Escuchando....')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
    
        audio = r.listen(source, 10, 6)
        
    try:
        print('reconociendo')
        eel.DisplayMessage('reconociendo....')
        query = r.recognize_google(audio, language='es-MX')
        print(f"usted dijo: {query}")
        eel.DisplayMessage(query)
        time.sleep(2)
        
    except Exception as e:
        return ""
    
    return query.lower()

@eel.expose
def allCommands():
    
    query = takecommand()
    print(query)
    
    if "abre" in query:
        from engine.features import openCommand
        openCommand(query)
    elif "en youtube":
        from engine.features import PlayYoutube
        PlayYoutube(query)
    
    else :
        print("not run")
        
    eel.ShowHood()