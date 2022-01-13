# # Taking speech and converting into the string 


# import pyttsx3          # pip install pyttsx3
# import datetime         # date time module is intalled as a default( Built in)
# import speech_recognition as sr       # pip install speech_recognition
# engine = pyttsx3.init('sapi5')   # sapi5 is microsoft speech api to get the voice inside the system
# voices = engine.getProperty('voices')
# # print(voices)   # two types of voices are there i.e male and female 

# #print(voices[0].id)      # You can print the voice of male or female by printing ( voices[1].id ) for female or ( voices[0].id ) for male       

# engine.setProperty('voice', voices[0].id)


# def speak(audio):                  # Function no. 1 
#     engine.say(audio)                 # to tell the engine
#     engine.runAndWait()      # From this command we can loud the voice

# def wishMe():                      # Function no. 2
#     hour = int(datetime.datetime.now().hour)
#     if hour >= 0 and hour < 12 :
#         speak("Good Morning!")
    
#     elif hour>=12 and hour<18:
#         speak("Good Afternoon!")
#     else :
#         speak("Good Evening!")
        
#     speak("I am Google,Please tell me how may help you ")

# def takeCommand():
#     # It takes microphone input from the user and returns string output
    
#     r = sr.Recognizer()    # Recogniser is a class
#     with sr.Microphone() as source:
#         print("Listening...")
#         r.pause_threshold = 1            # This is to set the freQuency of the volume received          
#         audio = r.listen(source)         # get it from the source file
        
#     try :       # try keyword is used To recognize 
#         print("Recognizing...")
#         query = r.recognize_google(audio , Language = 'en-in')        # en-in means english india
#         print(f"User said : {query}\n")             # Asked Query will be printed here
        
#     except Exception as e:
#        # print(e)                   # if anyone wants that the error will not display then just remove this line
#         print("Say that again please...")                # This Will be running like a while infinite loop             
#         return "None"
    
#     return query

import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime  # as built in
import wikipedia #pip install wikipedia    thsi is for the searching material
import webbrowser  # used to searh for youtube
import os    # used for the music
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Google. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    takeCommand()
    while True:
    # if 1:
        query = takeCommand().lower()                 # Logic for executing tasks based on query why we are taking in lower case bcoz queries
       # also so that Query will be easily matched, are there in lower case and Queries will be recognized in the lower case only
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)             # return two results and sentences
            speak("According to Wikipedia")
            print(results)       # Also print the results
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'open coding' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'      # Address of the folder
            songs = os.listdir(music_dir)             # os.listdir will list all the directories in one list
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))        # sing the songs, also we can add mp3 folder type
                              # songs[0] will sing songs as randomly suprise will create

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")      # get the time in string format     
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\users\\Priyam Gupta\\Downloads"
            os.startfile(codePath)

        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "priyamgupta880@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend !. I am not able to send this email")    


