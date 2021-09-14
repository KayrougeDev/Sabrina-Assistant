import time
import threading
import database

diary_list = []

def convert_name(text:str):
    try:
        s = text
        s = s.replace("_", " ")
        return s
    except:
        print("Une erreur est survenue")


class Diary:
    def __init__(self, args:str):
        self.args = args.split("-")
        if len(self.args) == 3:
            diary_list.append(self)
            dhd = self.get_diary_date_formated().split("_")
            dd_list = dhd[0].split("/")
            dh_list = dhd[1].split(":")
            Y = dd_list[2]
            M = dd_list[1]
            D = dd_list[0]
            H = dh_list[0]
            MIN = dh_list[1]
            self.diaryH = Y + M + D + H + MIN
            self.diaryH = int(self.diaryH)
            database.addDiary(self.args[0], self.args[1], self.diaryH)
            self.diary_list_index = len(diary_list)
            self.thread = threading.Timer(60.0, self.timeCheck)
            self.timeCheck()
        elif len(self.args) < 3:
          print("Pas assez d'argument ({}) !".format(str(len(self.args))))
        elif len(self.args) > 3:
          print("Trop d'arguments ({}) !".format(str(len(self.args))))


    def get_diary_values(self):
        return self.args

    def get_diary_name_formated(self):
        try:
            s = self.get_diary_values()[0]
            return s
        except:
            print("Une erreur est survenue")

    def get_diary_name_unformated(self):
        try:
            convert_name(self.get_diary_values()[0])
        except:
            print("Une erreur est survenue")

    def get_diary_desc_formated(self):
        try:
            s = self.get_diary_values()[1]
            return s
        except:
            print("Une erreur est survenue")

    def get_diary_desc_unformated(self):
        try:
            convert_name(self.get_diary_values()[1])
        except:
            print("Une erreur est survenue")

    def get_diary_date_formated(self):
        try:
            s = self.get_diary_values()[2]
            return s
        except:
            print("Une erreur est survenue")

    def get_diary_date_unformated(self):
        try:
            convert_name(self.get_diary_values()[2])
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
            self.thread.start()

    def stop_diary(self):
        self.endDiary()
        self.thread.cancel()

    def endDiary(self):
        database.removeDiary(self.get_diary_name_formated())

    def checkIsTime(self):
        dhd = self.get_diary_date_formated().split("_")
        y = time.strftime("%Y")
        m = time.strftime("%m")
        d = time.strftime("%d")
        h = time.strftime("%H")
        min = time.strftime("%M")
        localH = y + m + d + h + min
        localH = int(localH)
        print(self.diaryH, localH)
        if localH >= self.diaryH:
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




