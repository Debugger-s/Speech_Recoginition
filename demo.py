import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
from tkinter import *
from PIL import ImageTk, Image
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import time
import googletrans
import speech_recognition
import gtts

def education():
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
            speak("Good Morning")
        elif hour>=12 and hour<18:
            speak("Good Afternoon")
        else:
            speak("Good Evening")
        speak("Hello Boss. I am Jarvis.Please tell me. How may I help you sir")

    def takeCommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening..")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing..")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            # print(e)
            print("Say that again please...")
            return "None"
        return query


    def standard():
        speak("Are you interested in telling us your standard.")
        query = takeCommand().lower()
        if 'ok' in query:
            speak("Thank you for your support.")
            speak("Please tell me your standard.")
            query = takeCommand().lower()
            if 'first' in query:
                speak("Hello, small kid.")
                speak("The subjects in first class are: Mathematics, Hindi, English, Urdu")
                speak("Which subject do you want to study?")
                query = takeCommand().lower()
                if 'maths' in query:
                    speak("Now you can enjoy study maths ")
                    webbrowser.open("https://ncert.nic.in/textbook.php?aemh1=0-13")
                    speak("Thank you")
                elif 'hindi' in query:
                    speak("Now you can enjoy study hindi")
                    webbrowser.open("https://ncert.nic.in/textbook.php?ahhn1=0-19")
                    speak("Thank you")
                elif 'english' in query:
                    speak("Now you can enjoy study english")
                    webbrowser.open("https://ncert.nic.in/textbook.php?aerd1=0-19")
                    speak("Thank you")
                elif 'urdu' in query:
                    speak("Now you can enjoy study urdu")
                    webbrowser.open("https://ncert.nic.in/textbook.php?aulb1=0-27")
                    speak("Thank you")
                
            elif 'second' in query:
                speak("Hello, small kid.")
                speak("The subjects are: English, Maths, Hindi, Urdu")
                webbrowser.open("https://ncert.nic.in/textbook.php?been1=0-10")

            elif 'third' in query:
                speak("Hello, small kid.")
                speak("The subjects are: English, Maths, Hindi, Urdu, Evs")
                webbrowser.open("https://ncert.nic.in/textbook.php?cemh1=0-14")

            elif 'fourth' in query:
                speak("Hello, small kid.")
                speak("The subjects are: English, Maths, Hindi, Urdu, Evs")
                webbrowser.open("https://ncert.nic.in/textbook.php?deap1=0-27")

            elif 'fifth' in query:
                speak("Hello, small kid.")
                speak("The subjects are: English, Maths, Hindi, Urdu, Evs")
                webbrowser.open("https://ncert.nic.in/textbook.php?ehhn1=0-18")

            elif 'sixth' in query:
                speak("Hello, small kid.")
                speak("The subjects are: English, Maths, Hindi, Social Science, Sanskrit, Urdu, Science")
                webbrowser.open("https://ncert.nic.in/textbook.php?fehl1=0-10")

            elif 'seventh' in query:
                speak("Hello, small kid.")
                speak("The subjects are: English, Maths, Hindi, Social Science, Sanskrit, Urdu, Science")
                webbrowser.open("https://ncert.nic.in/textbook.php?gess3=0-9")

            elif 'eighth' in query:
                speak("Hello, small kid.")
                speak("The subjects are: English, Maths, Hindi")
                webbrowser.open("https://ncert.nic.in/textbook.php?hess3=0-10")

            elif 'ninth' in query:
                speak("Hello, small kid.")
                speak("The subjects are: English, Maths, Hindi, Social Science, Sanskrit, Urdu, Science, ICT, Health and Physical education")
                webbrowser.open("https://ncert.nic.in/textbook.php?iesc1=0-15")

            elif 'tenth' in query:
                speak("Hello, small kid.")
                speak("The subjects are: English, Maths, Hindi, Social Science, Sanskrit, Urdu, Science, ICT, Health and Physical education")
                webbrowser.open("https://ncert.nic.in/textbook.php?jemh1=0-15")

            elif 'eleventh' in query:
                speak("Hello, small kid.")
                speak("The subjects are: English, Maths, Hindi, Social Science, Sanskrit, Urdu, Science, ICT, Health and Physical education, Economics, Biology, Accountacy, Chemistry")
                webbrowser.open("https://ncert.nic.in/textbook.php?keph1=0-8")

            elif 'twelveth' in query:
                speak("Hello, small kid.")
                speak("The subjects are: English, Maths, Hindi, Social Science, Sanskrit, Urdu, Science, ICT, Health and Physical education, Economics, Biology, Accountacy, Chemistry")
                webbrowser.open("https://ncert.nic.in/textbook.php?lebo1=0-16")
        else:
            speak("Thank you")
            speak("Enjoy our technology.")


    def main():
        # speak("Bhanu I Love you.")
        wishMe()
        # standard()
        speak("Are you ready to explore. Please tell me what can I do for you.")
        while True:
            query = takeCommand().lower()

            if 'wikipedia' in query:
                speak("Searching Wikipedia...")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'yourself' in query:
                speak("My name is Jarvis. I am your personal learning assistant. You can learn anything with me free of cost. I am available for you anytime. I was developed by team debuggers.")

            elif 'open youtube' in query:
                speak("Opening Youtube")
                webbrowser.open("youtube.com")

            elif 'open google' in query:
                speak("Opening Google")
                webbrowser.open("google.com")

            elif 'play music' in query:
                music_dir = 'D:\\Songs'
                songs = os.listdir(music_dir)
                print(songs)
                speak("Playing the song")
                os.startfile(os.path.join(music_dir, songs[5]))

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Boss, the time is {strTime}")

            elif 'code' in query:
                codePath  ='"C:\\Users\\Admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"'
                speak("Opening the code")
                os.startfile(codePath)

            elif 'online learning' in query:
                speak("Showing you the free online courses available.")
                webbrowser.open("https://www.learnvern.com/")

            elif 'html' in query:
                speak("Showing you the free course on HTML.")
                webbrowser.open("https://www.learnvern.com/html5-tutorial")
                webbrowser.open("https://youtu.be/HcOc7P5BMi4")

            elif 'css' in query:
                speak("Showing you the course on CSS.")
                webbrowser.open("https://youtu.be/Edsxf_NBFrw")
                webbrowser.open("https://www.learnvern.com/css3-tutorial")

            elif 'javascript' in query:
                speak("Showing you the course on Javascript.")
                webbrowser.open("https://www.youtube.com/playlist?list=PL0rxPh2ovQP_JTqkFUtaZzBXzppx-VSWn")
                webbrowser.open("https://www.learnvern.com/javascript-tutorial-for-web-designers")

            elif 'bootstrap' in query:
                speak("Showing you the course on Bootstrap.")
                webbrowser.open("https://youtu.be/vpAJ0s5S2t0")
                webbrowser.open("https://www.learnvern.com/bootstrap-tutorial")

            elif 'web development' in query:
                speak("Showing you the complete course on Web Development.")
                webbrowser.open("https://www.youtube.com/playlist?list=PLu0W_9lII9agiCUZYRsvtGTXdxkzPyItg")

            elif 'c' in query:
                speak("Showing you the complete course on C programming language.")
                webbrowser.open("https://www.youtube.com/playlist?list=PLu0W_9lII9aiXlHcLx-mDH1Qul38wD3aR")
                webbrowser.open("https://www.learnvern.com/c-programming-tutorial")

            elif 'c++' in query:
                speak("Showing you the complete course on C++ programming language.")
                webbrowser.open("https://www.youtube.com/playlist?list=PLu0W_9lII9agpFUAlPFe_VNSlXW5uE0YL")
                webbrowser.open("https://www.learnvern.com/course/cpp-tutorial")

            elif 'java' in query:
                speak("Showing you the complete course on Java programming language.")
                webbrowser.open("https://www.youtube.com/playlist?list=PLu0W_9lII9agS67Uits0UnJyrYiXhDS6q")
                webbrowser.open("https://www.learnvern.com/course/core-java-programming-tutorial")

            elif 'python' in query:
                speak("Showing you the complete course on Python programming language.")
                webbrowser.open("https://www.learnvern.com/course/core-python-programming-tutorial-in-hindi")
                webbrowser.open("https://youtu.be/gfDE2a7MKjA")

            elif 'jquery' in query:
                speak("Showing you the complete course on J-Query.")
                webbrowser.open("https://www.youtube.com/playlist?list=PLwGdqUZWnOp0X4dVwSsEd6dV49TLLCooI")
                webbrowser.open("https://www.learnvern.com/jquery-tutorial")

            elif 'android' in query:
                speak("Showing you the complete course on Android Development.")
                webbrowser.open("https://www.learnvern.com/course/android-tutorial")
                webbrowser.open("https://www.youtube.com/playlist?list=PLu0W_9lII9aiL0kysYlfSOUgY5rNlOhUd")

            elif 'flutter' in query:
                speak("Showing you the complete course for Flutter Mobile Development")
                webbrowser.open("https://youtu.be/VPvVD8t02U8")

            elif 'react native' in query:
                speak("Study Mobile App Development with React Native.")
                webbrowser.open("https://www.learnvern.com/react-native-tutorial")
                webbrowser.open("https://www.youtube.com/playlist?list=PL8kfZyp--gEXs4YsSLtB3KqDtdOFHMjWZ")

            elif 'react' in query:
                speak("Study the web development with React Js.")
                webbrowser.open("https://www.learnvern.com/course/reactjs-tutorial")
                webbrowser.open("https://www.youtube.com/playlist?list=PLu0W_9lII9agx66oZnT6IyhcMIbUMNMdt")

            elif 'typescript' in query:
                speak("Study the Typescript for better web development.")
                webbrowser.open("https://www.youtube.com/playlist?list=PL4cUxeGkcC9gUgr39Q_yD6v-bSyMwKPUI")
                webbrowser.open("https://www.typescriptlang.org/docs/")

            elif 'angular' in query:
                speak("Study the web development with Angular.")
                webbrowser.open("https://youtu.be/k5E2AVpwsko")
                webbrowser.open("https://www.learnvern.com/course/advanced-angularjs-tutorial")

            elif 'php' in query:
                speak("Study the web development with PHP.")
                webbrowser.open("https://www.youtube.com/playlist?list=PL4cUxeGkcC9gUgr39Q_yD6v-bSyMwKPUI")
                webbrowser.open("https://www.w3schools.com/php/default.asp")
                webbrowser.open("https://www.php.net/downloads.php")

            elif 'mongo db' in query:
                speak("Study the advance database with Mongo DB.")
                webbrowser.open("https://www.geeksforgeeks.org/mongodb-an-introduction/")
                webbrowser.open("https://www.youtube.com/watch?v=oSIv-E60NiU&list=RDCMUCeVMnSShP_Iviwkknt83cww&start_radio=1&t=2s")
                webbrowser.open("https://www.mongodb.com/docs/")

            elif 'mysql' in query:
                speak("Study the database MySql.")
                webbrowser.open("https://www.youtube.com/watch?v=7S_tz1z_5bA")
                webbrowser.open("https://dev.mysql.com/doc/")

            elif 'node' in query:
                speak("Study the backend of web with nodejs.")
                webbrowser.open("https://nodejs.org/en/docs/")
                webbrowser.open("https://www.youtube.com/watch?v=IIpiLZGTWuo&list=PLwGdqUZWnOp00IbeN0OtL9dmnasipZ9x8")

            elif 'swift' in query:
                speak("Swift is a high-level general-purpose, multi-paradigm, compiled programming language developed by Apple Inc. and the open-source community..")
                webbrowser.open("https://youtu.be/8Xg7E9shq0U")

            elif 'perl' in query:
                speak("Perl is a high-level, interpreted, general-purpose programming language . Let's study it.")
                webbrowser.open("https://www.mindluster.com/certificate/3428?gclid=Cj0KCQjw2cWgBhDYARIsALggUhrga25UAPIQ72DiUAzWrJL_EKLQuwbJ2G1YhX9GtwJef-il9F8vp6oaAoy3EALw_wcB")
                webbrowser.open("https://youtube.com/playlist?list=PLWPirh4EWFpE0UEJPQ2PUeXUfvJDhPqSD")

            elif 'c sharp' in query:
                speak("Study the legendary programming language C Sharp.")
                webbrowser.open("https://www.codecademy.com/learn/learn-c-sharp")
                webbrowser.open("https://youtu.be/SuLiu5AK9Ps")

            elif 'sleep' in query:
                speak("I am going for a sleep")
                time.sleep(60)


            elif 'quit' in query:
                speak("Good Bye Boss. Have a nice day. ")
                exit()

    def sleep():
        speak("I am going for a sleep")
        time.sleep(60)





    root = Tk()
    root.title("Debuggers")
    root.geometry("900x450+200+200")
    root.resizable(False,False)
    root.configure(bg="#3e8187")



    #icon
    # image_icon1=PhotoImage(file="speaker logo.png")
    # root.iconphoto(False,image_icon1)

    # Top Frame
    Top_frame = Frame(root,bg="#154c79", width=900, height=100)
    Top_frame.place(x=0,y=0)


    Label(Top_frame,text="Education", font="arial 36 bold", bg="#154c79", fg="white").place(x=350,y=20)


    ################
    Top_frame = Frame(root,bg="#2e2e2d", width=250, height=500)
    Top_frame.place(x=0,y=100)

    btn=Button(root,text="Speak", width=10, font="arial 14 bold", bg="#39c790",command=main)
    btn.place(x=400,y=160)

    btn2=Button(root,text="Standard", width=10, font="arial 14 bold", bg="#39c790",command=standard)
    btn2.place(x=650,y=160)

    btn3=Button(root,text="Sleep", width=10, font="arial 14 bold", bg="#39c790",command=sleep)
    btn3.place(x=400,y=280)

    btn4=Button(root,text="Exit", width=10, font="arial 14 bold", bg="#39c790",command=root.destroy)
    btn4.pack()
    btn4.place(x=650,y=280)



    root.mainloop()

def translator():
    def transhien():
        recognizer = speech_recognition.Recognizer()
        with speech_recognition.Microphone() as source:
            print("speak now")
            voice = recognizer.listen(source,0,8)
            text = recognizer.recognize_google(voice,language="hi")
            print(text)

        # print(googletrans.LANGUAGES)
        translator = googletrans.Translator()
        translation = translator.translate(text,dest="en")
        print(translation.text)
        converted_audio = gtts.gTTS(translation.text, lang="en")
        converted_audio.save("hello.mp3")
        # playsound.playsound("hello.mp3")
        music_dir = 'C:\\Users\\vivek singh\\Desktop\\New folder (3)\\Speech_Recoginition'
        songs = os.listdir(music_dir)
        # print(songs)
        os.startfile(os.path.join(music_dir, songs[12]))

    def transenhi():
        recognizer = speech_recognition.Recognizer()
        with speech_recognition.Microphone() as source:
            print("speak now")
            voice = recognizer.listen(source,0,8)
            text = recognizer.recognize_google(voice,language="en")
            print(text)

        # print(googletrans.LANGUAGES)
        translator = googletrans.Translator()
        translation = translator.translate(text,dest="hi")
        print(translation.text)
        converted_audio = gtts.gTTS(translation.text, lang="hi")
        converted_audio.save("hello.mp3")
        # playsound.playsound("hello.mp3")
        music_dir = 'C:\\Users\\vivek singh\\Desktop\\New folder (3)\\Speech_Recoginition'
        songs = os.listdir(music_dir)
        # print(songs)
        os.startfile(os.path.join(music_dir, songs[12]))


    root = Tk()
    root.title("Debuggers")
    root.geometry("900x450+200+200")
    root.resizable(False, False)
    root.configure(bg="#3e8187")


    # icon
    # image_icon = PhotoImage(file="speaker logo.png")
    # root.iconphoto(False, image_icon)

    # Top Frame
    Top_frame = Frame(root, bg="#154c79", width=900, height=100)
    Top_frame.place(x=0, y=0)


    Label(Top_frame, text="Voice Translator", font="arial 36 bold",
        bg="#154c79", fg="white").place(x=300, y=20)


    ################
    Top_frame = Frame(root, bg="#2e2e2d", width=250, height=500)
    Top_frame.place(x=0, y=100)

    btn1 = Button(root, text="Hindi", width=10, font="arial 14 bold", bg="#39c790")
    btn1.place(x=300, y=160)

    btn2 = Button(root, text="English", width=10,
                font="arial 14 bold", bg="#39c790")
    btn2.place(x=530, y=160)

    Label(root,text="to",font="arial 20 bold", bg="#3e8187", fg="Black").place(x=460,y=160)


    # img = Image.open("R.png")
    # img = img.resize((50, 50), Image.ANTIALIAS)
    # img = ImageTk.PhotoImage(img)

    # label = Label(root, image=img, bg="#3e8187")
    # label.pack()
    # label.place(x=450, y=150)

    btn3 = Button(root, text="Speak", width=10, font="arial 14 bold", bg="#39c790", command=transhien)
    btn3.place(x=740, y=160)

    btn4 = Button(root, text="English", width=10, font="arial 14 bold", bg="#39c790")
    btn4.place(x=300, y=250)
    btn5 = Button(root, text="Hindi", width=10,
                font="arial 14 bold", bg="#39c790")
    btn5.place(x=530, y=250)

    Label(root,text="to",font="arial 20 bold", bg="#3e8187", fg="Black").place(x=460,y=250)

    # img1 = Image.open("a.png")
    # img1 = img1.resize((50, 50), Image.ANTIALIAS)
    # img1 = ImageTk.PhotoImage(img1)
    # label1 = Label(root, image=img1, bg="#3e8187")
    # label1.pack()
    # label1.place(x=450, y=250)

    btn6 = Button(root, text="Speak", width=10, font="arial 14 bold", bg="#39c790",command=transenhi)
    btn6.place(x=740, y=250)


    root.mainloop()



root = Tk()
root.title("Debuggers")
root.geometry("900x450+200+200")
root.resizable(False,False)
root.configure(bg="#3e8187")



#icon
image_icon=PhotoImage(file="speaker logo.png")
root.iconphoto(False,image_icon)

# Top Frame
Top_frame = Frame(root,bg="#154c79", width=900, height=100)
Top_frame.place(x=0,y=0)


Label(Top_frame,text="Admin Panel", font="arial 36 bold", bg="#154c79", fg="white").place(x=300,y=20)


################
Top_frame = Frame(root,bg="#2e2e2d", width=250, height=500)
Top_frame.place(x=0,y=100)


Label(root,text="Education",font="arial 24 bold", bg="#3e8187", fg="Black").place(x=350,y=160)
btn=Button(root,text="Open", width=10, font="arial 14 bold", bg="#39c790",command=education)
btn.place(x=600,y=160)
Label(root,text="Medical",font="arial 24 bold", bg="#3e8187", fg="black").place(x=350,y=230)
btn2=Button(root,text="Open", width=10, font="arial 14 bold", bg="#39c790")
btn2.place(x=600,y=230)
Label(root,text="Translator",font="arial 24 bold", bg="#3e8187", fg="black").place(x=350,y=300)
btn3=Button(root,text="Open", width=10, font="arial 14 bold", bg="#39c790",command=translator)
btn3.place(x=600,y=300)






root.mainloop()
