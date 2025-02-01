import speech_recognition as aa
import pyttsx3 #The pyttsx3 module is used for offline text-to-speech (TTS) conversion. Unlike gTTS, it doesn't require an internet connection.
import pywhatkit #The pywhatkit module is used for automation, such as sending WhatsApp messages, playing YouTube videos, and performing Google searches.
import datetime
import wikipedia
import webbrowser
listener = aa.Recognizer()
machine =pyttsx3.init()

def talk(text):
    machine.say(text)
    machine.runAndWait()
 
def input_instruction():
    global instruction
    try:
        with aa.Microphone() as origin:
            print("listening")
            speech =listener.listen(origin)
            instruction=listener.recognize_google(speech)   
            instruction=instruction.lower()
            if "virat" in instruction:
                instruction=instruction.replace("virat"," ")
                print(instruction)

    except Exception as e:
        print(f"Error: {e}") 
        pass
    return instruction
def play_virat():
    instruction=input_instruction()
    if(instruction):
        print(instruction)
        if "play" in instruction:
            song=instruction.replace('play', "")
            talk("playing"+ song) 
            pywhatkit.playonyt(song) #playing youtube
        if 'time' in  instruction:
            time=datetime.datetime.now().strftime('%I:%M %p')
            talk('current time' + time)
        elif 'date' in instruction:
            date=datetime.datetime.now().strftime('%d %m %Y')
            talk('todays date' + date)
        elif 'how are you ' in instruction:
            talk("i am fine, how about you")
        elif 'what is your name' in instruction:
            talk("I am virat")
        elif 'explain' in instruction:
            human = instruction.replace('explain', "")
            info = wikipedia.summary(human, 1)
            print(info)
            talk(info)
        elif "search" in instruction:
            a=instruction.replace('search',"")
            pywhatkit.search(a)

        elif "send" in instruction:
            name=instruction.replace('send',"")
            msg="hello ,this is assistant"
            pywhatkit.sendwhatmsg_instantly("+919154715354",msg ) 
        elif "open" in instruction:
            web=instruction.replace('open',"")
            webbrowser.open(web)
        elif 'who is' in instruction:
            human=instruction.replace('who is', " ")
            info=wikipedia.summary(human ,1)
            print(info)
            talk(info)
        else:
            talk("please say once more")

play_virat()
