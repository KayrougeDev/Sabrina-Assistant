import pathlib
import os, sys

#Pour la conversion en éxécutable
HERE = os.path.dirname(sys.argv[0])
sys.path.insert(0, HERE)
os.chdir(HERE)

#Pour un placement
HERE = os.path.dirname(sys.argv[0])
APPDIR = os.path.abspath(HERE)

sys.path.insert(0, APPDIR)
os.chdir(APPDIR)

def getConfigDir(appName=''):
    """
    Retourne le dossier de configuration.
    Si le paramètre appName n'est pas vide, on crée un sous-dossier.
    Emplacement par défaut :
        linux : ~/.config
        macOS : ~/Library/Preference
        windows : C:/Users/<USER>/AppData/Roaming
    """
    # on démarre dans le dossier de l'utilisateur (home) :
    configDir = pathlib.Path.home()
    # la suite dépend de l'OS :
    platform = sys.platform
    if platform.startswith('linux'):
        configDir = configDir / '.config'
    elif platform.startswith('win'):
        configDir = configDir / 'AppData/Roaming'
    elif platform.startswith('darwin'):
        configDir = configDir / 'Library/Preferences'
    # si on a passé une valeur à "appName",
    # on crée un sous-dossier :
    if (appName != ''):
        configDir = configDir / appName
        configDir.mkdir(parents=True, exist_ok=True)
    # un print pour vérifier et on renvoie "configDir" :
    print(configDir)
    return configDir




"""
Variables globales du programme.
    * APP_NAME : le nom du programme et donc du dossier à créer pour la configuration.
        À adapter au vrai nom du logiciel
    * DATA_FILE_DIR : le dossier de configuration du programme.
        Il est calculé par la fonction "getConfigDir"
"""
APP_NAME = 'SabrinaAssist'
DATA_FILE_DIR = getConfigDir(APP_NAME)

import chat