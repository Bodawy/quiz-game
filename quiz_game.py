# Module
import pyfiglet
import termcolor
import pyttsx3
import winsound

# Speak function
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Title 
print(termcolor.colored(pyfiglet.figlet_format("Welcome to"), color='yellow'))
print(termcolor.colored(pyfiglet.figlet_format("Quiz Game"), color='green'))

# Ask to play?
playing = input("Do you want to play? ")

if playing.lower() != "yes":
    speak("Okay bye!")
    print("Okay bye!")
    quit()

speak("Okay! Let's play :)")
print("Okay! Let's play :)")

score = 0

speak("What does CPU stand for? ")
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print(termcolor.colored('Correct!', color='green'))
    winsound.PlaySound('correct.wav', winsound.SND_FILENAME)
    score += 1
else:
    print(termcolor.colored('Incorrect!', color='red'))
    winsound.PlaySound('incorrect.wav', winsound.SND_FILENAME) 

speak("What does GPU stand for? ")
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print(termcolor.colored('Correct!', color='green'))
    winsound.PlaySound('correct.wav', winsound.SND_FILENAME)
    score += 1
else:
    print(termcolor.colored('Incorrect!', color='red'))
    winsound.PlaySound('incorrect.wav', winsound.SND_FILENAME) 

speak("What does RAM stand for? ")
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print(termcolor.colored('Correct!', color='green'))
    winsound.PlaySound('correct.wav', winsound.SND_FILENAME)
    score += 1
else:
    print(termcolor.colored('Incorrect!', color='red'))
    winsound.PlaySound('incorrect.wav', winsound.SND_FILENAME) 

speak("What does PSU stand for? ")
answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print(termcolor.colored('Correct!', color='green'))
    winsound.PlaySound('correct.wav', winsound.SND_FILENAME)
    score += 1
else:
    print(termcolor.colored('Incorrect!', color='red'))
    winsound.PlaySound('incorrect.wav', winsound.SND_FILENAME) 

# Score bar
if score < 2 :
    print('#'*20)
    print(termcolor.colored(f"You got " + str(score) + " questions correct!", color="red"))
    print(termcolor.colored(f"You got " + str((score / 4) * 100) + "%.", color='red'))
    print('#'*20)

elif score >= 2 :
    print('#'*20)
    print(termcolor.colored(f"You got " + str(score) + " questions correct!", color="green"))
    print(termcolor.colored(f"You got " + str((score / 4) * 100) + "%.", color='green'))
    print('#'*20)    