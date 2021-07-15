# Personal Assistant - Jarvis

## Overview:
Jarvis is a personal assistant written in python 3.
<br> It has been made to increase productivity and reduce difficulties.
<br> It is the Task-1 for IIEC-RISE 2.0.

## Python libraries used:
- pyttsx3: to provide voice-based output.
- os: to do operating-system-based tasks like launching some applications.
- datetime: for getting current date and time.
- webbrowser: to do browser-related tasks like opening web pages.

## Accepted Commands:
- "chrome" to open Chrome browser.
- "google" to open google.com.
- "youtube" to open youtube.com.
- "whatsapp" to open Whatsapp (desktop application).
- "cmd" to start the command prompt in windows.
- "music player" to launch music player application.
- "notepad" to start the notepad application.
- "add" to add numbers on the fly.
- "reverse" to reverse a string on the fly. 
- "help" or "man" to get some guidance.
- "stop" or "quit" to exit.

## Demo Video: 
https://youtu.be/K3utthJaocY

## Futures scope:
- currently, I am adding threading to it, so the program dosen't stop when an app is launched.
- More commands can be added.
- Voice based input can be added.
- Support for other operating systems (as it is designed for windows only).
- Artificial Intelligence can be added to provide the functionality to find the apps installed on OS and automatically add them to the menu. 
 
 ## Notes and known issues:
 - This app works only on Windows.
 - To launch an app from this app, the path is required to be set in env. var.
 - The app will stop or hang when it launches apps like chrome.
