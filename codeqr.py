from pathlib import Path
import qrcode
import qrcode.constants
from cv2 import QRCodeDetector, imread
from main import DATA_FILE_DIR
from tkinter.messagebox import showinfo
from colorama import Fore

DEFAULT_VERSION, DEFAULT_BOXE_SIZE, DEFAULT_BORDER = 3, 3, 5

QR_FILE_DIR = DATA_FILE_DIR / "QrCode"
if not QR_FILE_DIR.exists():
    QR_FILE_DIR.mkdir()


def createQrCode(name:str,QRversion:int,QrBoxeSize:int,QrBorder:int,data,color:str,color_back:str):
    try:
        qr = qrcode.QRCode(
            version=QRversion,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=QrBoxeSize,
            border=QrBorder
        )
        l = 0
        while l < len(data):
            if l == len(data)-1:
                qr.add_data(data[l])
            else:
                qr.add_data(data[l]+"\n")
            l += 1

    
        qr.make(fit=True)

        img = qr.make_image(fill_color=color, back_color=color_back)
        img.save(name)
        showinfo("QrCode", "QrCode créé: "+name)
    except:
        print(Fore.RED + "Une erreur est survenue avec la création du QrCode (peut arriver quand l'enregistrement est annuler)" + Fore.WHITE)




def read(name:str):
    try:
        dir = QR_FILE_DIR / (name+".png")
        dufg = QRCodeDetector()
        val, points, qrcode = dufg.detectAndDecode(imread(str(dir)))
        return val
    except:
        return "Une erreur est survenue pendant la lecture du qrcode\n\nAucun Qr Code détecter."


def readPath(name:Path):
    try:
        dir = name
        dufg = QRCodeDetector()
        val, points, qrcode = dufg.detectAndDecode(imread(str(dir)))
        return val
    except:
        return "Une erreur est survenue pendant la lecture du qrcode\n\nAucun Qr Code détecter ou lien vers le fichier invalide."

