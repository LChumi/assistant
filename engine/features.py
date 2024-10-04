import re
from playsound import playsound
import eel
from engine.command import speak
from engine.config import ASSISTANT_NAME
import os 
import pywhatkit as kit
# Playing assiant sound function
@eel.expose
def playAssistantSound():
    music_dir ="www\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)
    
    
def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("abre", "")
    query.lower()
    
    if query!="":
        speak("Abriendo "+query)
        os.system('start '+query)
    else:
        speak("no se encontro")
        
def PlayYoutube(query):
    search_term = extract_yt_term(query)
    
    if search_term is None:
        speak("No se encontró un término de búsqueda válido.")
        return  # Termina la función si no hay término de búsqueda
    
    speak("Reproduciendo " + search_term + " en Youtube")
    kit.playonyt(search_term)

def extract_yt_term(command):
    # Define las expresiones regulares
    pattern = r'reproduce\s+(.*?)\s+en\s+youtube'
    # Usa re.search para encontrar la coincidencia en el comando
    match = re.search(pattern, command, re.IGNORECASE)
    # Si se encuentra una coincidencia, devuelve el nombre de la canción extraído; de lo contrario, devuelve None
    return match.group(1) if match else None