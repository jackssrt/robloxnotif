from types import prepare_class
from modules.enums import Presence
from modules.utils import log
from win10toast import ToastNotifier
from colorama import Fore, Back, Style, init
from time import sleep
from playsound import playsound
init(True)
toast = ToastNotifier()


def notify(usernames, a, boot):  # function responsible for showing notification and playing sound
    thestring = ""
    theicon = "robloxnotif.ico"
    thecolor = Fore.WHITE
    thesound = "robloxnotif"
    if usernames[str(a["userId"])].startswith("!") or usernames[str(a["userId"])].startswith("[!]"):
        thesound = "fav"
    if str(a["userPresenceType"]) == str(Presence.Playing.value):
        thestring = "playing: " + a["lastLocation"]
        if a["lastLocation"] == "":
            thestring = "playing something"
        theicon = "playing.ico"
        thecolor = Fore.LIGHTGREEN_EX  # better for powershell
    elif str(a["userPresenceType"]) == str(Presence.Online.value):
        thestring = "online"
        theicon = "online.ico"
        thecolor = Fore.LIGHTCYAN_EX  # better for powershell
    elif str(a["userPresenceType"]) == str(Presence.InStudio.value):
        thestring = "in studio: " + a["lastLocation"]
        if a["lastLocation"] == "":
            thestring = "in studio making something"
        theicon = "studio.ico"
        thecolor = Fore.LIGHTYELLOW_EX  # better for powershell
    elif (str(a["userPresenceType"]) == str(Presence.Offline.value)) and (not boot):
        thestring = "now offline"
        thecolor = Fore.LIGHTBLACK_EX  # better for powershell
        theicon = "offline.ico"
    if thestring != "":

        log(usernames[str(a["userId"])]+" is "+thestring, thecolor)
        toast.show_toast(usernames[str(a["userId"])] + " is", thestring,
                         duration=3, icon_path="./icons/" + theicon, threaded=True)
        playsound(f"./sounds/{thesound}.wav")
        while toast.notification_active():
            sleep(0.1)


def errorNotify(title, body):
    toast.show_toast(title, body, "./icons/robloxnotif.ico", 5, True)
    playsound("./sounds/error.wav")
    while toast.notification_active():
        sleep(0.1)
