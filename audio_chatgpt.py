import openai
import speech_recognition as sr
import pyttsx3
import datetime
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
from colorama import just_fix_windows_console
just_fix_windows_console()

# Define OpenAI API key 
openai.api_key = "API_KEY"

# Création d'un objet recognizer
r = sr.Recognizer()
engine = pyttsx3.init()
voice = engine.getProperty('voices')[0] # Use the first available voice
engine.setProperty('voice', voice.id)
engine.setProperty('rate', 150) # Set the speaking rate (words per minute)

history = []
while True:
    print(Style.BRIGHT + Fore.RED + "Q: ", end = '')
    with sr.Microphone() as source:
        audio = r.listen(source)
        
    try:
        # Utilisation de l'API de Google pour transcrire en texte la voix enregistrée
        user_input = r.recognize_google(audio, language='fr-FR')
        print(user_input + Style.RESET_ALL)

        
        if user_input.strip():
            messages = []
            for input_text, completion_text in history:
                messages.append({"role": "user", "content": input_text})
                messages.append({"role": "assistant", "content": completion_text})

            messages.append({"role": "user", "content": user_input})

            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages
            )

            completion_text = completion.choices[0].message.content
            print(Style.BRIGHT + Fore.GREEN + completion_text + Style.RESET_ALL)
            
            engine.say(completion_text)
            engine.runAndWait()
            
            history.append((user_input, completion_text))

            if user_input.upper() == "QUIT":
                break
    
    except sr.UnknownValueError:
        print("Impossible de comprendre la voix")
    except sr.RequestError as e:
        print("Erreur lors de la reconnaissance vocale : {0}".format(e))
