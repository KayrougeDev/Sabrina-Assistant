import pathlib
from main import DATA_FILE_DIR

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
        elif len(self.args) < 3:
          print("Pas assez d'arguments ({}) !".format(str(len(self.args))))
        elif len(self.args) > 3:
          print("Trop d'arguments ({}) !".format(str(len(self.args))))

    def get_diary_data_dir(self):
        return self.DIARY_DATA_DIR

    def get_diary_file(self):
        return self.diary_file

    def substring(msg:str):
        msg = msg[:len(msg)-1]
        return msg

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