from time import strftime
import diary
import pathlib

DATA_FILE_DIR = pathlib.Path() / "Data"
if not DATA_FILE_DIR.exists():
    DATA_FILE_DIR.mkdir()

TEMP_input = input("Entre une date dans le format: JJ/MM/AAAA_HH:MM, je te conseille de mettre un truc rapide comme la date du jour ou tu fait le teste et pour l'heure mes pour dans 1-2 minute, si yaa un probleme dit le moi: ")

d = diary.Diary(DATA_FILE_DIR, "anniv_mathias-anniv_de_mathias_bientot-"+TEMP_input)

dhd = d.get_diary_date_formated().split("_")

dd_list = dhd[0].split("/")
dh_list = dhd[1].split(":")

Y = dd_list[2]
M = dd_list[1]
D = dd_list[0]

H = dh_list[0]
MIN = dh_list[1]

diaryH = Y + M + D + H + MIN

diaryH = int(diaryH)

print(diaryH)


def checkIsTime():
    y = strftime("%Y")
    m = strftime("%m")
    d = strftime("%d")
    h = strftime("%H")
    min = strftime("%M")
    localH = y + m + d + h + min
    localH = int(localH)
    if localH >= diaryH:
        print("IsTime")
        return True
    else:
        return False

while True:
    if checkIsTime():
        break