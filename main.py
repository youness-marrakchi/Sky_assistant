
import speech_recognition as sr
import time
import webbrowser
import playsound
from gtts import gTTS
import os
import random
from includes.jokes import jokes

rcg = sr.Recognizer()
# chromePath = "C:\Program Files\Google\Chrome\Application\chrome.exe %s"

def voice_Command(ask=False):
    with sr.Microphone() as source:
        if ask:
            sky_speaks(ask)
        audio = rcg.listen(source) # passing in the microphone
        voice_data = ''
        try:
            voice_data = rcg.recognize_google(audio) # The given commands
        except sr.UnknownValueError:
            sky_speaks('Pardon, i did not get that !')
        except sr.RequestError:
            sky_speaks('Sorry, my speech is not functioning')
        return voice_data

def sky_speaks(audio_string):
    tts = gTTS(text=audio_string, lang='en') # Text To Speech
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def sky_respond(voice_data):
    if "what's your name" in voice_data:
        sky_speaks('My name is sky')
    if 'what time is it' in voice_data:
        sky_speaks(time.asctime( time.localtime(time.time()) ))
    if 'thanks' in voice_data:
        sky_speaks("you're welcome !")
    # if 'tell me a joke' in voice_data:
    #     num = random.randint(1, 6)
    #     sky_speaks('okay here you go !')
    #     sky_speaks(jokes[num])
    if 'open' in voice_data:
        open = voice_Command('what do you want to open ?')
        url = 'https://'+ open +'.com/'
        sky_speaks('opening ' + open)
        webbrowser.get('C:/Program Files/Google/Chrome/Application/chrome.exe %s').open(url)
    if 'search' in voice_data:
        search = voice_Command('what do you want to search for ?')
        url = 'https://google.com/search?q=' + search
        sky_speaks("here's what i found about " + search)
        webbrowser.get('C:/Program Files/Google/Chrome/Application/chrome.exe %s').open(url)
    if 'find location' in voice_data:
        location = voice_Command("what's the location ?")
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        sky_speaks("here's the location of " + location)
        webbrowser.get('C:/Program Files/Google/Chrome/Application/chrome.exe %s').open(url)
    if 'turn off' in voice_data:
        exit()
time.sleep(1)
print('How can i help you ?')
while 1:
    voice_data = voice_Command()
    sky_respond(voice_data)