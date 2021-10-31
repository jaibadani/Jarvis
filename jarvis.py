
import pyttsx3
import datetime
import os
import speech_recognition as sr
import wikipedia
import webbrowser
import smtplib
import numpy as np
from PIL import ImageGrab
import winsound
from win32api import GetSystemMetrics
import cv2
from time import sleep
email_da_list = {
    'jai':'jaibadani28@gmail.com',
    'manav':'manavbadani26@gmail.com',
    'mom':'sonalbadani5@gmail.com',
    'dad':'mayurbadani5@gmail.com'
}
whatsapplist = {
    'jai':'+919867515436',
    'manav':'+919833515191',
    'dad':'+919833515199',
    'mom':'+918369393969'
}
os.system('cls')
webbrowser.register('Chrome',
None,
webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)
def whatsappmsg(number,msg):
    what_link = "https://web.whatsapp.com/send?phone="+number+"&text="+msg
    webbrowser.get('Chrome').open(what_link)
    
def speak(audio):
    engine.say(audio) 
    engine.runAndWait()
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning!")
        speak("Good Morning!")
        
    elif hour>=12 and hour<18:
        print("Good Afternoon!")
        speak("Good Afternoon!")
    else:
        print("Good Evening!")
        speak("Good evening!")
    print("I am Jarvis, how may i help you")
    speak("I am Jarvis, how may i help you")
def alarm(specific_time):
    while True:
        sleep(1)
        current_time = datetime.datetime.now().strftime("%I%M")
        if str(current_time) == str(specific_time):
            print("The time is up! ")
            print("press ctrl c to exit the alarm")
            while True:
                try:
                    
                    winsound.PlaySound('Deathnote.wav',winsound.SND_FILENAME)
                except:

                    break
            break
def remider(date,msg):
    filename = str(date)+".txt"
    fh = open(filename,'w')
    fh.write(msg)
    fh.close()
def checkreminder():
    today = datetime.datetime.now().date()
    guessed_file = str(today)+".txt"
    try:
        f = open(guessed_file,'r')
        rem = f.read()
        f.close()
        print("The reminder for today is: ")
        speak("The reminder for today is")
        print(rem)
        speak(rem)
    except Exception:
        print("There are no reminders for today")
        speak("There are no reminders for today")
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('humanplaysofficial@gmail.com','shinchan5199')
    server.sendmail('humanplaysofficial@gmail.com',to,content)
    server.close()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("listening")
        r.pause_threshold = 1
    
        audio = r.listen(source)
    try:
        print("Recognizing...")
        speak("recognizing")
        query = r.recognize_google(audio, language='en-in')
        print("User said: ",query)
    except Exception as e:
        print("Say that again please...")
        speak("Say that again please")
        takeCommand()
    return query
if __name__ == "__main__":
    wishme()
    while True:
        try:

    
            query = takeCommand().lower()
            if 'wikipedia' in query:
                try:
                    speak("Searching wikipedia")
                    print("Searching wikipedia...")
                    query = query.replace("wikipedia","")
                    results = wikipedia.summary(f'{query}', sentences=3)
                    print("According to wikipedia...")
                    speak("According to wikipedia")
                    print(results)
                    speak(results)
                except Exception as e:
                    print(e)
                    print("some error occured:(")
                    speak("some error occured")
                    continue
            elif 'open youtube' in query:
                webbrowser.get('Chrome').open("youtube.com")
            elif 'open google' in query:
            
                webbrowser.get('Chrome').open("google.com")
            elif 'open discord' in query:
            
                webbrowser.get('Chrome').open("https://discord.com/channels/@me")
            elif 'open whatsapp' in query:
            
                webbrowser.get('Chrome').open("https://web.whatsapp.com/")
            elif 'open instagram' in query:
            
                webbrowser.get('Chrome').open("https://instagram.com/")
            elif 'open netflix' in query:
            
                webbrowser.get('Chrome').open("https://www.netflix.com/browse")
            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                print(strTime)
                speak(strTime)
            elif 'open code' in query:
                codePath = "C:\\Users\\manav\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk"
                os.startfile(codePath)
            elif 'open chrome' in query:
                chromePath = "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"
                os.startfile(chromePath)
            elif 'open java' in query:
                javaPath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\BlueJ\\BlueJ.lnk"
                os.startfile(javaPath)
            elif 'open teams' in query:
                teamsPath = "C:\\Users\\manav\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Teams.lnk"
            elif 'bye bye' in query:
                speak("OKAY I AM TAKING YOUR LEAVE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                exit()
                os.system('exit')
            elif 'who are you' in query:
                print("I was created by Jai Badani on 23ʳᴰ of November, 2021. I am far better than the cortana a literal noob in AI")
                speak("I was created by Jai Badani on 23ʳᴰ of November, 2021. I am far better than the cortana a literal noob in AI")                
            elif 'send an email' in query:
                try:
                    print("Enter the name of the contact")
                    speak("Enter the name of the contact")
                    name = takeCommand()
                    name = name.replace(" ","")
                    cont = email_da_list[name]
                    print(cont)
                    speak("Email will be sent to "+cont)
                    print("Enter the message you would send")
                    speak("Enter the message you would send")
                    msg =takeCommand()
                    sendEmail(cont,msg)
                    print("An email saying "+msg+" has been sent to "+name+" whose email id is "+cont)
                    speak("An email saying "+msg+" has been sent to "+name+" whose email id is "+cont)
                except Exception:
                    print("Some error occured:(")
                    speak("Some error occured")
                    continue

            # elif 'pause for' in query:
            #     try:

            #         query = query.replace("pause for","")
            #         query = query.replace("minutes","")
            #         query = int(query)
            #         query *= 60
            #         print("OKAY I WILL CALL YOU AGAIN IN ",query) 
            #         speak("OKAY I WILL CALL YOU AGAIN IN ",query)
            #         sleep(query)
            #     except:
            #         print("some error occured:(")
            #         speak("SOME ERROR OCCURED")
            #         continue
            elif 'send a whatsapp message' in query:
                print("Whom do you want to send the message? ")
                speak("Whom do you want to send the message?")
                name_of_what = takeCommand()
                if ' ' in name_of_what:
                    name_of_what = name_of_what.replace(" ","")
                    name_of_what = name_of_what.lower()
                mnumber = whatsapplist[name_of_what]
                print(mnumber)
                print("Say the content you want to send")
                speak("say the content you want to send")
                content = takeCommand()
                speak("sending whatsapp message to "+mnumber+" telling "+content)
                
                whatsappmsg(mnumber,content)

            elif 'on youtube' in query:
                query = query.replace("on youtube","")
                if 'search' in query:
                    query = query.replace("search","")
                print("Searching "+query+" on youtube")
                speak("Searching "+query+" on youtube")
                youtube_lin = "https://www.youtube.com/results?search_query="+query
                webbrowser.get('Chrome').open(youtube_lin)

            elif 'record screen' in query:
                width = GetSystemMetrics(0)
                height = GetSystemMetrics(1)
                fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
                captured_vid = cv2.VideoWriter('output.mp4',fourcc,20.0,(width,height))
                while True:
                    img = ImageGrab.grab(bbox=(0,0,width,height))
                    img_np = np.array(img) 
                    img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
                    cv2.imshow('secret capture',img_final)
                    captured_vid.write(img_final)
                    if cv2.waitKey(10) == ord('q'):
                        break
            elif 'who am i' in query:
                fh = open('pd.txt','r')
                data = fh.read()
                fh.close()
                print(data)
                speak(data)
            elif 'set an alarm' in query:
                print("At what time should I call you ?")
                speak("At what time should I call you ?")
                time = takeCommand()
                print("Okay your alarm for "+str(time)+" is set")
                speak("Okay your alarm for "+str(time)+" is set")
                if 'p.m.' in time:
                    time = time.replace("p.m.","")
                if 'a.m.' in time:
                    time = time.replace("a.m.","")
                if ' ' in time:
                    time = time.replace(" ","")
                if ':' in time:
                    time = time.replace(":","")
                if int(time)<1000:
                    time = "0"+time
                if 'pm' in time:
                    time = time.replace("pm","")
                if 'am' in time:
                    time = time.replace("am","")

                alarm(time)
            elif 'set a reminder' in query:
                print("Type the date in the format (yyyy-mm-dd): ")
                speak("Type the date in the format (yyyy-mm-dd): ")
                date = input()
                print("Now say the message to be reminded on "+date)
                speak("Now say the message to be reminded on "+date)
                messg = takeCommand()
                remider(date,messg)
                print("The reminder saying "+messg+" is set")
                speak("The reminder saying "+messg+" is set")
            elif 'reminder' in query:
                checkreminder()
            elif 'on google' in query:
                if 'search' in query:
                    query = query.replace("search","")
                query = query.replace("on google","")
                print("Searching "+query+" on google")
                speak("Searching "+query+" on google")
                goolink = "https://www.google.com/search?q="+query
                webbrowser.get('Chrome').open(goolink)
            elif 'help' in query:
                print("I am kinda an Artficial Intelligence bot created by Jai")
                speak("I am kinda an Artficial Intelligence bot created by Jai")
                os.system('functions.py')
            elif 'install-module' in query:
                print("Okay")
                speak("Okay")
                os.system('C:\\Users\\manav\\OneDrive\\Documents\\py4e\\Jarvis\\module_installer.py')
            else:
                print("Sorry I do not understand")
                speak("Sorry I do not understand")
                print("But you can always use the 'help' command to know what I am capable to do")
                speak("But you can always use the 'help' command to know what I am capable to do")
        except Exception as e:
            if 'bye bye' in query:
                exit()
            print(e)
            print("some error occured:(")
            speak("some error occured")