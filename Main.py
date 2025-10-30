import sys
import os
import time
os.system('python -m ensurepip')
os.system('cls')
cwd=os.getcwd()
os.chdir(cwd)
global user_key
if os.path.exists("gemini_api_key.gemini_key"):
    with open("gemini_api_key.gemini_key","r") as f:
        user_key=f.read()
else:
    os.system('cls')
    print('You need to make a txt file called "gemini_api_key.gemini_key" and put your api key in there')
    print('(make sure to put it in the directory where you are running this file at)')
    time.sleep(9999)
print('(HINT: You can just say "none" for the default system prompt)')
user_specified_ai_instruction=input('What do you want the ai system prompt to be ?:')
if user_specified_ai_instruction=='none' or user_specified_ai_instruction=='None':
    print('Default ai instruction chosen')
    user_specified_ai_instruction="Your name is jarvis and you are an ai on someones computer running in a python file"
else:
    user_specified_ai_instruction=str(user_specified_ai_instruction)


print('Checking for requirements...')
os.system('color 02')
try:
    import speech_recognition as sr
except:
    os.system('pip install SpeechRecognition')
try:
    import keyboard
except:
    os.system('pip install keyboard')
try:
    #It says it's not used but whenever I dont use this it errors so we keeping it
    import pyaudio
except:
    os.system('pip install pyaudio')
try:
    import whisper
except:
    os.system('pip install -U openai-whisper')
try:
    import pyttsx3
except:
    os.system('pip install pyttsx3')
try:
    #This is needed !!! even tho it says it's not accessed 
    import soundfile
except:
    os.system('pip install soundfile')
try:
    from google import genai
except:
    os.system('pip install -q -U google-genai')
print('You own all of the requirements.')
os.system('color 03')
time.sleep(2)
import speech_recognition as sr
import keyboard
import pyttsx3
from google import genai 
from google.genai import types


def record_mic():
    recognizer = sr.Recognizer()
    mic = sr.Microphone(device_index=1)
    audio_chunks = []

    with mic as source:
        while keyboard.is_pressed('`'):
            audio = recognizer.listen(source, phrase_time_limit=1)
            audio_chunks.append(audio)

    if not audio_chunks:
        return None
    

    combined_audio = sr.AudioData(
        b''.join(chunk.get_raw_data() for chunk in audio_chunks),
        sample_rate=audio_chunks[0].sample_rate,
        sample_width=audio_chunks[0].sample_width
    )
    whisper_voice_rec=recognizer.recognize_whisper(combined_audio, language="english", model="tiny.en")
    print('You said:'+whisper_voice_rec)
    print('')
    
    client=genai.Client(api_key=user_key)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
        system_instruction=str(user_specified_ai_instruction)),
        contents=whisper_voice_rec
    )
    print('Ai response:'+str(response.text))
    print('')
    engine = pyttsx3.init()
    engine.setProperty('rate', 190) 
    engine.say(response.text)
    engine.runAndWait()

print('Listening for input')

while True:
    if keyboard.is_pressed('`'):
        mp3File=record_mic()
        while keyboard.is_pressed('`'):
            pass

