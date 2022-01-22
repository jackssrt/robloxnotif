from os import path
from platform import system
from time import sleep
from typing import Dict

from colorama import Back, Fore, Style

from modules.classes import Presence
from modules.enums import PresenceType
from modules.utils import log

thePlatform = system()


# function responsible for showing notification and playing sound
def notify(usernames: Dict[str, str], a: Presence, boot: bool):
    thestring = ""
    theicon = "robloxnotif.ico"
    thecolor = Fore.WHITE
    thesound = "robloxnotif"
    if usernames[str(a.userId)].startswith("!") or usernames[str(a.userId)].startswith(
        "[!]"
    ):
        thesound = "fav"
    if str(a.userPresenceType) == str(PresenceType.Playing.value):
        thestring = "playing: " + a.lastLocation
        if a.lastLocation == "":
            thestring = "playing something"
        theicon = "playing"
        thecolor = Fore.LIGHTGREEN_EX  # better for powershell
    elif str(a.userPresenceType) == str(PresenceType.Online.value):
        thestring = "online"
        theicon = "online"
        thecolor = Fore.LIGHTCYAN_EX  # better for powershell
    elif str(a.userPresenceType) == str(PresenceType.InStudio.value):
        thestring = "in studio: " + a.lastLocation
        if a.lastLocation == "":
            thestring = "in studio making something"
        theicon = "studio"
        thecolor = Fore.LIGHTYELLOW_EX  # better for powershell
    elif (str(a.userPresenceType) == str(PresenceType.Offline.value)) and (not boot):
        thestring = "now offline"
        thecolor = Fore.LIGHTBLACK_EX  # better for powershell
        theicon = "offline"
    if thestring != "":

        log(usernames[str(a.userId)] + " is " + thestring, thecolor)
        if thePlatform == "Linux" or thePlatform == "Darwin":
            from notifypy import Notify

            notif = Notify()
            notif.title = usernames[str(a.userId)] + " is"
            notif.message = thestring
            notif.icon = f"./icons/png/{theicon}.png"
            notif.audio = path.realpath(f"./sounds/{thesound}.wav")
            notif.application_name = "robloxnotif"
            notif.send(block=True)

        elif thePlatform == "Windows":
            import win10toast
            from playsound import playsound

            toast = win10toast.ToastNotifier()
            toast.show_toast(
                usernames[str(a.userId)] + " is",
                thestring,
                duration=3,
                icon_path="./icons/" + theicon + ".ico",
                threaded=True,
                sound=False,
            )
            try:
                playsound(path.realpath(f"./sounds/{thesound}.wav"))
            except UnicodeDecodeError:
                pass
            while toast.notification_active():
                sleep(0.1)


def errorNotify(title, body):
    if thePlatform == "Linux" or thePlatform == "Darwin":
        from notifypy import Notify

        notif = Notify()
        notif.title = title
        notif.message = body
        notif.icon = "./icons/png/robloxnotif.png"
        notif.audio = path.realpath("./sounds/error.wav")
        notif.application_name = "robloxnotif"
        notif.send(block=True)

    elif thePlatform == "Windows":
        import win10toast
        from playsound import playsound

        toast = win10toast.ToastNotifier()
        toast.show_toast(
            title,
            body,
            duration=5,
            icon_path="./icons/robloxnotif.ico",
            threaded=True,
            sound=False,
        )
        try:
            playsound(path.realpath("./sounds/error.wav"))
        except UnicodeDecodeError:
            pass
        while toast.notification_active():
            sleep(0.1)
