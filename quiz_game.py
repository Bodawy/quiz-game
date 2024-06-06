# Modules
import pyfiglet
import termcolor
import pyttsx3
import winsound

# Style
print(termcolor.colored(pyfiglet.figlet_format("Welcome to"), color='yellow'))
print(termcolor.colored(pyfiglet.figlet_format("Quiz Game"), color='green'))

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print(termcolor.colored('Correct!', color='green'))
    winsound.PlaySound('correct.wav', winsound.SND_FILENAME)
    score += 1
else:
    print(termcolor.colored('Incorrect!', color='red'))
    winsound.PlaySound('incorrect.wav', winsound.SND_FILENAME) 

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print(termcolor.colored('Correct!', color='green'))
    winsound.PlaySound('correct.wav', winsound.SND_FILENAME)
    score += 1
else:
    print(termcolor.colored('Incorrect!', color='red'))
    winsound.PlaySound('incorrect.wav', winsound.SND_FILENAME) 

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print(termcolor.colored('Correct!', color='green'))
    winsound.PlaySound('correct.wav', winsound.SND_FILENAME)
    score += 1
else:
    print(termcolor.colored('Incorrect!', color='red'))
    winsound.PlaySound('incorrect.wav', winsound.SND_FILENAME) 

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print(termcolor.colored('Correct!', color='green'))
    winsound.PlaySound('correct.wav', winsound.SND_FILENAME)
    score += 1
else:
    print(termcolor.colored('Incorrect!', color='red'))
    winsound.PlaySound('incorrect.wav', winsound.SND_FILENAME) 

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")