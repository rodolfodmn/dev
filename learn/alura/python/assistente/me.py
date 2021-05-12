from gtts import gTTS
import speech_recognition as sr
from subprocess import call
from requests import get
from bs4 import BeautifulSoup
import webbrowser as browser
import json

## configs
hotword = 'rose'

with open('rosie-python-assistente-fe02a8d39c53.json') as credenciais_google:
    credenciais_google = credenciais_google.read()


## functions

def monitora_audio():
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            print("Aguardando o comando: ")
            audio = microfone.listen(source)
            try:
                trigger =  microfone.recognize_google_cloud(
                    audio, credentials_json=credenciais_google, language='pt-BR'
                )
                trigger = trigger.lower()

                if hotword in trigger:
                    print('COMANDO: ', trigger)
                    responde('feedback')
                    executa_comandos(trigger)
                    break

            except sr.UnknownValueError:
                print("Google not understand audio")
            except sr.RequestError:
                print("Could not request results from Google Cloud Speech service; {0}".format(e))

    return trigger

def responde(arquivo):
    call(['afplay', 'audios/' + arquivo + '.mp3'])

def cria_audio(mensagem):
    tts = gTTS(mensagem, lan='pt-br')
    tts.save('audios/mensagem.mp3')
    print('ROSIE: ', mensagem)
    call(['afplay', 'audios/mensagem.mp3'])


def executa_comandos(trigger):
    if 'notícias' in trigger:
        ultimas_noticias()

    elif 'toca' in trigger and 'bee gees' in trigger:
        playlists('bee_gees')

    elif 'toca' in trigger and 'bee gees' in trigger:
        playlists('bee_gees')

    elif 'tempo agora' in trigger:
        previsao_tempo(tempo=True)

    elif 'temperatura hoje' in trigger:
        previsao_tempo(minmax=True)

    else:
        mensagem = trigger.strip(hotword)
        cria_audio(mensagem)
        print('C. INVÁLIDO', mensagem)
        responde('comando_invalido')

## functions commands

def ultimas_noticias():

