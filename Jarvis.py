import pyttsx3
import os
import datetime
import webbrowser

print("************ASSISTANT************")
pyttsx3.speak("Hello this is Jarvis your assistant")
pyttsx3.speak("Please enter your name to let us serve you better ")

name = input("Your Name please: ")

print("If you are new to this app then type man or help")

hour = int(datetime.datetime.now().hour)

if hour >= 0 and hour < 12:
    greetings = "Good Morning " + name + " ,How may I help you ? "

elif hour >= 12 and hour < 18:
    greetings = "Good Afternoon " + name + " ,How may I help you ? "   

else:
    greetings = "Good Evening " + name + " ,How may I help you ? "  
      

pyttsx3.speak(greetings)

Assistant_on = True

while Assistant_on:
    pyttsx3.speak("What can I help you with ?")
    command = input("How may I help you ? ").lower()
    print("")
    
    if "open chrome" in command or "run chrome" in command or "chrome" in command:
        pyttsx3.speak("Chrome has been opened for you")
        os.system("chrome")                
            
    elif "hi" in command or"hello" in command:
        pyttsx3.speak("Hello, I am your assistant")
                
    elif "open google" in command or "google" in command:
        pyttsx3.speak("Google.com has been opened for you ")
        webbrowser.open("google.com")
       
    elif "youtube" in command or "open youtube" in command or "youtube.com" in command:
        pyttsx3.speak("Youtube has been opened for you")
        webbrowser.open("youtube.com")
                
    elif "whatsapp" in command or "open whatsapp" in command or "run whatsapp" in command:
        pyttsx3.speak("Whatsapp has been opened for you")
        os.system("WhatsApp")
                            
    elif "cmd" in command or "run cmd" in command or "execute cmd" in command:
        pyttsx3.speak("Command prompt has been opened for you")
        os.system("cmd")
    
    elif "run music player" in command or "music player" in command:
        pyttsx3.speak("Music Player has been opened for you")
        os.system("PotPlayer")
        
    elif "run notepad" in command or "execute notepad" in command or "notepad" in command:
        pyttsx3.speak("Notepad has been opened for you")
        os.system("notepad")
        
    elif "dj" in command or "run dj" in command or "open dj" in command:
        pyttsx3.speak("Virtual Dj has been opened for you")
        os.system("VirtualDJ8")
    
    elif "add" in command or "addition" in command:
        pyttsx3.speak("Enter the first number")
        x = int(input("First Number : "))
        pyttsx3.speak("Enter the second number")
        y = int(input("Second Number: "))
        sum = x + y
        pyttsx3.speak("The sum is")
        pyttsx3.speak(sum)
        print("The sum is ", sum)
        
    elif "reverse" in command or "rverse string" in command:
        pyttsx3.speak("Enter the string plaease")
        z = input("String: ")
        r_z = z[::-1]
        print("reverse: ",r_z)
        pyttsx3.speak("The reverse strring is :")
        pyttsx3.speak(r_z)
            
    elif "stop" in command or "exit" in command or "bye" in command or "quit" in command:
        pyttsx3.speak("Nice talking to you"+ name +" see you later!!")
        Assistant_on = False
        
    elif "help" in command or "man" in command or "how to use" in command:
        print("This is your assistant")
        print("It can open")
        print("chrome")
        print("command prompt")
        print("Just type the app name or type a complete phrase")
        print("Like : chrome or please open chrome ,etc")
            
    else:
        pyttsx3.speak("Sorry, this command is not supported at the moment")
        
