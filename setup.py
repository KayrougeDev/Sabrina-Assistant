from cx_Freeze import setup, Executable
import os.path
import sys

# Permet d'éviter une erreur de type "KeyError: TCL_LIBRARY"

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))

# Si vous souhaitez pouvoir exporter sur un autre système d'exploitation, ces lignes sont nécessaires.

base = None

if sys.platform == "win32":
	base = "Win32GUI"

	# Fichier que l'on souhaite inclure dans le dossier de l'exécutable

	includefiles = [
		"chat.py",
		"sabrina.py",
		"codeqr.py",
		"diary.py",
		"icon.png"
	]

	# Paramètres de l'exécutable

	target = Executable(
		script = "main.py",
		copyright= "",
		icon="icon.png",
		base = base
	)

	setup(
		name = "SabrinaAssist",
	    version = "1.0",
	    description = "Assistante Personelle",
	    options = { "build_exe": { 'include_files': includefiles } },
	    executables = [ target ]
    )