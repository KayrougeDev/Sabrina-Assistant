import sqlite3
from tkinter.messagebox import showerror, showinfo
from colorama import Fore


try:
    connect = sqlite3.connect("DB/NABRISA.db")
    cursor = connect.cursor()
    
    try:
        cursor.execute("SELECT * FROM NABRISA_agenda")
    except Exception as e:
        if str(e).__contains__("NABRISA_agenda"):
            cursor.execute('CREATE TABLE "NABRISA_agenda" ("agenda_name" TEXT,"agenda_desc" TEXT,"agenda_date" TEXT)')
            print("La table 'NABRISA_agenda' n'existait pas est a été créé.")

    def getCurrentDiary():
        req = cursor.execute("SELECT * FROM NABRISA_agenda")
        current = []
        for row in req.fetchall():
            current.append(row[0])
        return current

    def getAllDiary():
        return cursor.execute("SELECT * FROM NABRISA_agenda").fetchall()

    def removeDiary(diaryName:str):
        cursor.execute("DELETE FROM NABRISA_agenda WHERE agenda_name = ?", (diaryName,))
        connect.commit()
        print(Fore.BLUE + "L'agenda "+diaryName.replace("_", " ")+" a été supprimer" + Fore.WHITE)

    def addDiary(diaryName:str, diaryDesc:str, diaryDate:str):
        cursor.execute("INSERT INTO NABRISA_agenda VALUES(?,?,?)", (diaryName, diaryDesc, diaryDate))
        connect.commit()
        showinfo("Agenda", "L'agenda "+diaryName.replace("_", " ")+"a été créé !")

    def closeConnection():
        cursor.close()
        connect.close()
        print("Database closed !")

except Exception as e:
    showerror("Erreur SQL",e)
    print("[ERREUR SQL]",e)
    connect.rollback()

