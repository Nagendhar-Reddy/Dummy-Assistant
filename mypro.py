import speech_recognition as sr
import time
import pyttsx3
import time
import pywhatkit
import wikipedia
import pyjokes
import webbrowser




def sir(answer):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(answer)
    engine.runAndWait()



r = sr.Recognizer()
with sr.Microphone() as source:
    print("please say something what you want")
    audio = r.listen(source)

try:
    print(r.recognize_google(audio))
    question = r.recognize_google(audio)

    if 'Alexa' in question:
        question = question.replace('Alexa', '')
        print(question)
        if 'what are you doing' in question:
            print('I am waiting for question..')
        elif 'how are you' in question:
            print('Iam good Thank you! how can I help you ?')
            sir('Iam good Thank you! how can I help you ?')
        elif 'what is time now' in question:
            question = time.localtime()
            current_time = time.strftime("%I:%M:%S %p", question)
            print(current_time)
            sir(current_time)
            (sir("Thank you for asking Time:..."))

        elif 'who is' in question:
            question = question.replace('who is', '')
            print(wikipedia.summary(question, 1))
            sir(wikipedia.summary(question, 1))
            (sir("Thank you for asking question:..."))
        elif 'joke' in question:
            joke = pyjokes.get_joke()
            print(joke)
            sir(joke)
        elif 'play' in question:
            question=question.replace("play",'')
            pywhatkit.playonyt(question)
        elif "search" in question:
         question=question.replace('search','')
         url="https://www.google.com/search?q="+ question
         webbrowser.register('chrome',None,
                             webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
         web=webbrowser.get('chrome').open(url)
         sir(web)
        sir("THANK YOU FOR ASKING!!")


    else:
        print("You are not talking with me..")

except sr.UnknownValueError:
    print("Sorry,I can't hear your voice... ")
