"""
Assistant Personnel V 1.2

 
 
"""

# Les imports
#import PyQt5 as pqt
from main import DATA_FILE_DIR, chooseFileDir, chooseFileDirToSave

import diary
import codeqr as qrcode
import threading

# Attention ne pas faire de runandwait et de init, utilise vocal_engine.speak(message) ca va tout faire tout seul
import pyttsx3


# Colorama sert a metre de la couleur dans la console, avec Fore, par exemple Fore.RED va mettre le texte en rouge
# et Fore.RESET remet la couleur par default (si ca ne marche pas faire Fore.WHITE pour remettre en blanc
import colorama
from colorama import Fore
import pygame

from tkinter import *
from tkinter.messagebox import *

# Tout les codes d'initialisation
colorama.init()
pygame.init()

print(Fore.GREEN + "Sabrina 1.2" + Fore.WHITE)


DATA_FILE = DATA_FILE_DIR / "user.data.assist"
if not DATA_FILE.exists():
    with open(DATA_FILE, "w+") as f:
        f.close()
        
def writeData(v1, v2, v3):
    with open(DATA_FILE, "w") as data:
        data.write(v1 + "\n")
        data.write(v2 + "\n")
        data.write(v3)
        data.close()

DIARY_DATA_DIR = DATA_FILE_DIR / "diary"
if not DIARY_DATA_DIR.exists():
    DIARY_DATA_DIR.mkdir()


engine = pyttsx3.init()
volume = engine.getProperty('volume')
rate = engine.getProperty('rate')
engine.setProperty('volume', volume-1.25)
engine.setProperty('voice', 'french')
engine.setProperty('rate', rate-50)

def speak(msg:str):
    engine.say(msg)
    engine.runAndWait()

def pSpeak(msg:str):
    print(msg)
    engine.say(msg)
    engine.runAndWait()


root = Tk()
root.geometry('950x500')
root.title("Sabrina 1.2")
root.config(bg='#ffd8a8')

try:
    img = PhotoImage(file='icon.png')
    root.iconphoto(True, img)
except:
    showwarning("Icone", "Impossible de charger l'icone !")

def readData(index:int):
  with open(DATA_FILE, "r") as data:
    value_list = data.readlines()
    data.close()
    return value_list[index]
    
def _askUserInfoWIndow():
    win = Tk()
    win.geometry("300x300")
    win.title("Info des utilisateurs")
    e1 = Entry(win)
    e2 = Entry(win)
    e3 = Entry(win)
    e1.pack(expand=YES)
    e2.pack(expand=YES)
    e3.pack(expand=YES)
    def valid():
        writeData(e1.get(), e2.get(), e3.get())
        updateData()
        win.destroy()
    Button(win,text="Valider",command=valid).pack(expand=YES)

# variable de base
TEMP_userfirstname = ""
TEMP_usersurname = ""
TEMP_birthdate = ""

def updateData():
    global TEMP_userfirstname, TEMP_usersurname, TEMP_birthdate
    try:
        TEMP_userfirstname = readData(0)
        TEMP_usersurname = readData(1)
        TEMP_birthdate = readData(2)
        TEMP_userfirstname = TEMP_userfirstname[:len(TEMP_userfirstname)-1]
        TEMP_usersurname = TEMP_usersurname[:len(TEMP_usersurname)-1]
    except:
        _askUserInfoWIndow()


updateData()

def clearData():
    f = open(DATA_FILE, "w")
    f.write("")
    f.close()

def ask_yes_no(msg:str):
    v = input(msg + " Y/n: ")
    if v == "Y":
        return True
    elif v == "n":
        return False
    else:
        print("invalide")
        return ask_yes_no(msg)





def clearDataWindow():
    if askyesno("Tout supprimer", "Êtes-vous sur de vouloir supprimer les données pour toujours (c'est long) ?\nLe programme va se fermer."):
        clearData()
        root.destroy()

def dataQrCode():
    dataIn = [
        TEMP_userfirstname,
        TEMP_usersurname,
        TEMP_birthdate
    ]
    qrcode.createQrCode(
        chooseFileDirToSave("Sauvegarder un QrCode - Sabrina"),
        qrcode.DEFAULT_VERSION,
        qrcode.DEFAULT_BOXE_SIZE,
        qrcode.DEFAULT_BORDER, dataIn, "red", "white"
    )

def customQRCode():
    win = Tk()
    win.geometry("300x300")
    win.title("Qr Code Gen")
    data = []
    e1 = Entry(win)
    e1.pack(expand=YES)
    def add_data():
        data.append(e1.get())
    def valid():
        qrcode.createQrCode(
            chooseFileDirToSave("Sauvegarder un QrCode - Sabrina"),
            qrcode.DEFAULT_VERSION,
            qrcode.DEFAULT_BOXE_SIZE,
            qrcode.DEFAULT_BORDER, data, "blue", "white"
        )
        win.destroy()
    Button(win,text="Ajouter donnée",command=add_data).pack(expand=YES)
    Button(win,text="Valider",command=valid).pack(expand=YES)

def readDataQrCode():
    r = qrcode.readPath(chooseFileDir("Choisir un QrCode - Sabrina"))
    r = str(r)
    r = r.split("\n")
    writeData(r[0], r[1], r[2])
    updateData()
    showinfo("QrCode", "Le qrcode a correctement été lu !")

def readQRCode():
    r = qrcode.readPath(chooseFileDir("Choisir un QrCode - Sabrina"))
    win = Tk()
    win.geometry("300x300")
    win.title("Lecture du QrCode")
    e1 = Label(win, text=r)
    e1.pack(expand=YES)
    win.mainloop()

def createDiary():
    win = Tk()
    win.geometry("300x300")
    win.title("Agenda")
    name = Entry(win)
    name.pack(expand=YES)
    desc = Entry(win)
    desc.pack(expand=YES)
    
    e1 = Entry(win)
    e1.pack(expand=YES)
    e2 = Entry(win)
    e2.pack(expand=YES)
    e3 = Entry(win)
    e3.pack(expand=YES)
    e4 = Entry(win)
    e4.pack(expand=YES)
    e5 = Entry(win)
    e5.pack(expand=YES)
    def valid():
        name2 = name.get().replace(" ", "_")
        desc2 = desc.get().replace(" ", "_")
        descs = name2 + "-" + desc2
        date = e1.get() + "/" + e2.get() + "/" + e3.get() + "_" + e4.get() + ":" + e5.get()
        final = descs + "-" + date
        d = diary.Diary(DATA_FILE_DIR, final)
        showinfo("Agenda", "Agenda créé")
        win.destroy()
    Button(win,text="Valider",command=valid).pack(expand=YES)

def actualDiaryWindow():
    t = threading.enumerate()
    showinfo("Agenda", "Agenda en cours"+str(t))

#Un menu
menubar = Menu(root)
menubar.config(bg='#ffd8a8')

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Re-entrer les infos", command=_askUserInfoWIndow)
menu1.add_command(label='Supprimer toutes les donnés', command=clearDataWindow)
menu1.add_separator()
menu1.add_command(label="Créer un qrcode de données", command=dataQrCode)
menu1.add_command(label="Créer un qrcode personalisé", command=customQRCode)
menu1.add_separator()
menu1.add_command(label="Lire un qrcode de données", command=readDataQrCode)
menu1.add_command(label="Lire un qrcode", command=readQRCode)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Créer un agenda (Presque fonctionelle)", command=createDiary)
menu2.add_command(label="Agenda en cours (En developement)", command=actualDiaryWindow)



menubar.add_cascade(label="Outils", menu=menu1)
menubar.add_cascade(label="Agenda", menu=menu2)


root.config(menu=menubar)
