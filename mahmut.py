#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 01:08:45 2019

@author: eco
"""
#import all libraries
import speech_recognition as sr
from gtts import gTTS
import os
from time import ctime
import time
from selenium import webdriver
import sys
from pygame import mixer

#creating a mixer object.
mixer.init()

#translate speech to text, after than load audio.mp3 to giving machine answers.
def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='tr')
    tts.save("audio.mp3")
    mixer.music.load("audio.mp3")
    mixer.music.play()

#record all sounds to permission a microfone.
def recordAudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Bir şeyler söyle!")
        audio = r.listen(source)
#sounds are taking a data string.
    data = ""
    try:
        data = r.recognize_google(audio, language='tr-tr')
        print("Dediğin şey: " + data)
    except sr.UnknownValueError:
        print("Google seni anlayamadı.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return data

#if person say anything in data, must be in this function.
def jarvis(data):
    if "Selamünaleyküm" in data:
        time.sleep(1)
        speak("Aleykum selam " + isim)

    if "Mahmut" in data:
        time.sleep(1)
        speak("Buyurun " + isim)

    if "nasılsın" in data:
        time.sleep(1)
        speak("İyiyim {}. Siz nasılsınız?".format(isim))

    if "Merhaba" in data:
        time.sleep(1)
        speak("Merhaba " + isim)

    if "saat kaç" in data:
        time.sleep(1)
        speak(ctime())

    if "neredeyiz" in data:
        time.sleep(1)
        data = data.split(" ")
        location = data[0]
        speak("Bekle {} Birazdan buluyorum ".format(isim) + location)
        driver = webdriver.Chrome('/home/eco/Masaüstü/Gereksiz/PYTHON_FILES/chromedriver') #change your chromedriver directory!
        os.system("chromium-browser https://www.google.com/maps/place/" + location + "/&amp;")
        time.sleep(15)

    if "çal" in data:
        time.sleep(1)
        data = data.split(" ")
        sarki_ismi = " "
        for i in data[:2]:
            sarki_ismi = sarki_ismi + i

        speak("Bekle {} Birazdan buluyorum. ".format(isim) + sarki_ismi + " yi çalıyorum")
        driver = webdriver.Chrome('/home/eco/Masaüstü/Gereksiz/PYTHON_FILES/chromedriver') #change your chromedriver directory!
        driver.get("https://www.youtube.com/results?search_query=" + sarki_ismi)

    if "çıkış" in data:
        speak("Hoşçakalın {} Yine bekleriz.".format(isim))
        time.sleep(4)
        sys.exit()

    return data


time.sleep(2)
#take your name and say all documents for your name
speak("İsminizi söyler misiniz?")
isim = recordAudio()
speak("Hoşgeldiniz " + isim)

time.sleep(3)

speak("Sizin için ne yapabilirim?")

while 1:
    data = recordAudio()
    jarvis(data)

