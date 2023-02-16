import time
from turtle import done
from winreg import QueryInfoKey, QueryValue, QueryValueEx
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys
import config

engine = pyttsx3.init('sapi5')
#wolframalpha API Code
client = wolframalpha.Client('T5JWT6-X8VXYT9KY5')
#pyttsx3
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)
#Def to speak the pyttsx3
def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()
#Reading Time
def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')

greetMe()

#UserTalk 
def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-US')
        print('User: ' + query + '\n')
        
    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))

    return query
#Selenium Settings MAKE SURE U DOWNLOAD THE CHROMEDRIVER AND YOU INSTALL THE SELENIUM LIB       
def openbrowser():
    global browser
    chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument("--headless")
    chrome_options.add_argument('--no-sandbox')
    browser = webdriver.Chrome('C:/Users/ExampleName/Desktop/chromedriver.exe',chrome_options=chrome_options)   #Replace the ExampleName with yours
#Assistant Doing What you want    
if __name__ == '__main__':

    while True:
    
        query = myCommand();
        query = query.lower()
#Assistant Writes For You In SearchBar
        if 'i want to listen music in youtube' in query:
            speak('Okey.Tell me what do you want to search for you.')
            search = myCommand()
            youtube_search = 'https://www.youtube.com/results?search_query=' + search
            print ("Done!")
            webbrowser.open(youtube_search)
#Just Open Youtube Tab        
        elif 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')
#Netflix Login (Make sure you edited the configFile)            
        elif 'login to my netflix account' in query:
            speak('Done!')
            def navigate(link):
                browser.get(link)
                time.sleep(8)
            openbrowser()
            browser.get("https://www.netflix.com/gr/login")
            name= browser.find_element_by_name('userLoginId')
            print ("Email Or ID Entered...")
            name.send_keys(config.netflixLogin)
            password= browser.find_element_by_name('password')
            print ("Password Has Entered...")
            password.send_keys(config.netflixPassword)
            print ("Login In")
            log=browser.find_element_by_css_selector(".btn.login-button.btn-submit.btn-small")
            log.click()
            
#Open Google Tab
        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.gr')

        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')
#Facebook Login (Make sure you edited the configFile)
        elif 'login to my facebook account' in query:
            speak('Done!')
            def navigate(link):
                browser.get(link)
            openbrowser()
            navigate("https://www.facebook.com/")
            name= browser.find_element_by_name('email')
            print ("Email Or ID Entered...")
            name.send_keys(config.faceboookMail)
            password= browser.find_element_by_name('pass')
            print ("Password Has Entered...")
            password.send_keys(config.facebookPassword)
            print ("Login In")
            bot=browser.find_element_by_id("loginbutton")
            bot.click()

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))
#Mail Send
        elif 'email' in query:
            speak('Who is the recipient? ')
            recipient = myCommand()

            if 'me' in recipient:
                try:
                    speak('What should I say? ')
                    content = myCommand()
                    server = smtplib.SMTP('smtp.gmail.com:587')
                    server.ehlo()
                    server.starttls()
                    server.login(config.mailEmail , config.mailPassword)
                    server.sendmail( config.mailEmail, config.mailSend, content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry Sir! I am unable to send your message at this moment!')


        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye Sir, have a good day..')
            sys.exit()
        elif 'what can you do?' in query:
            speak('I am programmed to make your life more simple..I can automatically sign in your account..e.g Facebook Account or Netflix Account')
            
        elif 'hello' in query:
            speak('Hello sir.')

        elif 'bye' in query:
            speak('Bye sir, have a good day..')
            sys.exit()
                                    
        elif 'play music' in query:
            music_folder = "Your_music_folder_path"
            music = ["music1, music2, music3, music4, music5"]
            random_music = music_folder + random.choice(music) + '.mp3'
            os.system(random_music)
                  
            speak('Okay, here is your music! Enjoy!')
            
#Login Instagram (Make sure you edited the configFile)
        elif 'Login to my Instagram account' in query:
            speak ('Done!')
            def navigate(link):
                browser.get(link)
            openbrowser()
            navigate ("https://www.instagram.com/accounts/login/")
            name= browser .find_element_by_name('email')
            print ("Login credentials has been entered.....")
            name.send_keys(config.InstagramMail)
            password= browser.find_element_by_name('pass')
            print ("Passkey has been entered......")
            password.send_keys(config.InstagramPassword)
            print ("Access Granted")
            bot=browser.find_element_by_id("loginbutton")
            bot.click()
                                    
#Twitter Login (Make sure to edit the configfile)      
        elif 'login to my twitter account' in query:
            speak('Done!')
            def navigate(link):
                browser.get(link)
            openbrowser()
            navigate("https://twitter.com/home")
            name= browser.find_element_by_name('email')
            print ("Email or ID Entered...")
            name.send_keys(config.TwitterMail)
            password= browser.find_element_by_name('pass')
            print ("Password Has Entered...")
            password.send_keys(config.TwitterPassword)
            print ("Login In")
            bot=browser.find_element_by_id("loginbutton")
            bot.click()       
            
#Discord Login (Make sure to edit the configfile)
        elif 'login to my Discord account' in query:
            speak('Done!')
            def navigate(link):
                browser.get(link)
            openbrowser()
            navigate("https://discord.com/")
            name= browser.find_element_by_name('email')
            print ("Email or ID Entered...")
            name.send_keys(config.DiscordMail)
            password= browser.find_element_by_name('pass')
            print("Password Has Entered...")
            password.send_keys(config.DiscordPassword)
            print ("Login In")
            bot=browser.find_element_by_id("loginbutton")
            bot.click()

#Github Login (Add login data in the comfig file)
        elif 'login to my Github account' in query:
            speak('Done!')
            def navigate(link):
                browser.get(link)
            openbrowser()
            navigate('https://github.com/')

                       
                                                                   
#Searching On Wikipedia (Sometimes if you say something wrong its searching on wiki (Little Bug :P))
        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA says -')
                    speak('Got it!')
                    speak(results)
                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it!')
                    speak('WIKIPEDIA says - ')
                    speak(results)
        
            except:
                webbrowser.open('www.google.com')
        
        speak('Next Command! Sir!') 
        
           
#Anonymous browsing(Tor browsing)      [In Development]         
        
