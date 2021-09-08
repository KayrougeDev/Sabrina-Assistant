from tkinter import *
import pygame
import sabrina
import webbrowser

window = sabrina.root

pygame.mixer.init()
pygame.mixer.music.load("sendUser.ogg")
while pygame.mixer.get_busy():
    pass

def musique():
    pygame.mixer.music.play()

# une frame juste pour aligner horizontalement
frame = Frame(window, bg='#1BB3A4')
frame.pack(side=RIGHT, padx=10)

sabrinaFrame = Frame(window, bg='#1BB3A4')
sabrinaFrame.pack(side=LEFT, padx=10)




# le champ d'entrée pour mettre la question
commandEntry = Entry(frame, bg='WHITE', font=("Book Antika", 15))
commandEntry.pack(side=BOTTOM, padx=10)


    
def sPrint(msg:str):
    SabrinaLabel(msg)
    sabrina.engine.say(msg)
    sabrina.engine.runAndWait()
    
    
def awserToUser(msg:str):
    if msg.__contains__("nom") and msg.__contains__("famille") and not msg.__contains__("diary"):
        sPrint(sabrina.TEMP_usersurname)
    elif msg.__contains__("nom") and not msg.__contains__("prénom") and not msg.__contains__("diary"):
      sPrint(sabrina.TEMP_usersurname)
    elif msg.__contains__("prénom"):
        sPrint(sabrina.TEMP_userfirstname)
    elif msg.__contains__("Boys"):
        webbrowser.open_new("https://www.youtube.com/watch?v=LT9yUYFkJMA")
        sPrint("C'est partie pour Boys !")
    elif msg.__contains__("Rick"):
        webbrowser.open_new("https://youtu.be/dQw4w9WgXcQ")
        sPrint("Never Gonna Give You Up !")
    elif msg.__contains__("anniv") or msg.__contains__("naissance"):
      if not msg.__contains__("diary"):
        sPrint(sabrina.TEMP_birthdate)
    elif msg.__contains__("qrcode"):
        sPrint("Pour utiliser les Qr Codes allez dans outils dans la barre de navigation en haut.")
    else:
        sPrint("Je ne comprend pas !")


#Le label utilisateur
def Userlabel():
    awserToUser(commandEntry.get())
    label = Label(frame, text=commandEntry.get(), bg='#1BB3A4', font=("Book Antika", 15))
    label.pack()


#Le label utilisateur
def SabrinaLabel(msg:str):
    label = Label(sabrinaFrame, text=msg, bg='#1BB3A4', font=("Book Antika", 15))
    label.pack()
    

def _sendUserMsg(event):
    sendUserMsg()

def sendUserMsg():
    Userlabel()
    musique()

window.bind("<space>", _sendUserMsg)

# le bouton
myButton = Button(
    frame,
    text='Envoyer.', 
    command=sendUserMsg)
myButton.pack(side=BOTTOM)

print("Sabrina a correctement démarrer.")

sPrint("Bonjour {}, Je suis Sabrina votre assistante personelle.".format(sabrina.TEMP_userfirstname))

window.mainloop()
