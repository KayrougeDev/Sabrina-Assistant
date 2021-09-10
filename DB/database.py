import sqlite3
from tkinter.messagebox import showerror, showinfo


try:
    connect = sqlite3.connect("DB/base.db")
    cursor = connect.cursor()

    def getCurrentDiary():
        req = cursor.execute("SELECT * FROM NABRISA_agenda")
        current = []
        for row in req.fetchall():
            current.append(row[0])
        return current

    def removeDiary(diaryName):
        cursor.execute("DELETE FROM NABRISA_agenda WHERE agenda_name = ?", (diaryName,))
        connect.commit()
        showinfo("Agenda", "L'agenda "+diaryName.replace("_", " ")+" a été supprimer")

    def addDiary(diaryName:str, diaryDesc:str, diaryDate:str):
        s = (diaryName, diaryDesc, diaryDate)
        cursor.execute("INSERT INTO NABRISA_agenda VALUES(?,?,?)", s)
        connect.commit()
        showinfo("Agenda", "L'agenda "+diaryName.replace("_", " ")+" a été créé !")

    def closeConnection():
        cursor.close()
        connect.close()
        print("Database closed !")

except Exception as e:
    showerror("Erreur SQL",e)
    print("[ERREUR SQL]",e)
    connect.rollback()

