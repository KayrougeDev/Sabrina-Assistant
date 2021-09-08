import pathlib
import time
import threading
import os

diary_list = []

class Diary:
    def __init__(self, data_dir:pathlib.Path, args:str):
        self.DIARY_DATA_DIR = data_dir / "diary"
        if not self.DIARY_DATA_DIR.exists():
            self.DIARY_DATA_DIR.mkdir()

        self.args = args.split("-")
        if len(self.args) == 3:
            f = 0
            self.diary_file = self.DIARY_DATA_DIR / self.args[0]
            data = open(self.diary_file, "w+")
            while f < len(self.args):
                data.write(self.args[f] + "\n")
                f += 1
            data.close()
            self.timeCheck()
            self.diary_list_index = len(diary_list)
        elif len(self.args) < 3:
          print("Pas assez d'argument ({}) !".format(str(len(self.args))))
        elif len(self.args) > 3:
          print("Trop d'arguments ({}) !".format(str(len(self.args))))

    def get_diary_data_dir(self):
        return self.DIARY_DATA_DIR

    def get_diary_file(self):
        return self.diary_file


    def get_diary_values(self):
        with open(self.get_diary_file(), "r") as file:
            value_list = file.readlines()
            file.close()
            return value_list

    def get_diary_name_formated(self):
        try:
            s = self.get_diary_values()[0]
            return s[:len(s)-1]
        except:
            print("Une erreur est survenue")

    def get_diary_name_unformated(self):
        try:
            s = self.get_diary_values()[0]
            s = s.replace("_", " ")
            return s[:len(s)-1]
        except:
            print("Une erreur est survenue")

    def get_diary_desc_formated(self):
        try:
            s = self.get_diary_values()[1]
            return s[:len(s)-1]
        except:
            print("Une erreur est survenue")

    def get_diary_desc_unformated(self):
        try:
            s = self.get_diary_values()[1]
            s = s.replace("_", " ")
            return s[:len(s)-1]
        except:
            print("Une erreur est survenue")

    def get_diary_date_formated(self):
        try:
            s = self.get_diary_values()[2]
            return s[:len(s)-1]
        except:
            print("Une erreur est survenue")

    def get_diary_date_unformated(self):
        try:
            s = self.get_diary_values()[2]
            s = s.replace("_", " ")
            return s[:len(s)-1]
        except:
            print("Une erreur est survenue")

    def timeCheck(self):
        """
        while True:
            if self.checkIsTime():
                break
            time.sleep(60)
        """
        if not self.checkIsTime():
            t = threading.Timer(60.0, self.timeCheck)
            t.start()
            self.thread = t

    def stop_diary(self):
        self.endDiary()
        self.thread.cancel()

    def endDiary(self):
        if os.path.exists(self.diary_file):
            os.remove(self.diary_file)
        else:
            print("Impossible de supprimer le fichier car il n'existe pas")

    def checkIsTime(self):
        dhd = self.get_diary_date_formated().split("_")
        dd_list = dhd[0].split("/")
        dh_list = dhd[1].split(":")
        Y = dd_list[2]
        M = dd_list[1]
        D = dd_list[0]
        H = dh_list[0]
        MIN = dh_list[1]
        diaryH = Y + M + D + H + MIN
        diaryH = int(diaryH)
        y = time.strftime("%Y")
        m = time.strftime("%m")
        d = time.strftime("%d")
        h = time.strftime("%H")
        min = time.strftime("%M")
        localH = y + m + d + h + min
        localH = int(localH)
        print(diaryH, localH)
        if localH >= diaryH:
            self.endDiary()
            print("Agenda terminer")
            return True
        else:
            return False

        



"""
d = Diary(DATA_FILE_DIR, "anniv_mathias-anniv_de_mathias_bientot-09/08/2021_12:30")

print(d.get_diary_data_dir())
print(d.get_diary_name_formated())
print(d.get_diary_name_unformated())
print(d.get_diary_desc_formated())
print(d.get_diary_desc_unformated())
print(d.get_diary_date_formated())
print(d.get_diary_date_unformated())

"""




