from datetime import datetime
from colorama import Fore, Back, Style, init
import json
init(True)


def error(text, color):
    log(f"{Fore.LIGHTRED_EX}[ERROR]{Style.RESET_ALL}{color} {text}",
        Fore.LIGHTRED_EX)


def warn(text, color):
    log(f"{Fore.LIGHTYELLOW_EX}[WARN]{Style.RESET_ALL}{color} {text}",
        Fore.LIGHTYELLOW_EX)


def log(text, color):  # log function
    now = datetime.now().strftime("%X")
    print(f"{color}{Style.DIM}[{now}]:{Style.RESET_ALL}{color} {text}")


def isChanged(a, b):  # function for checking if presence has changed or not
    if not a or not b:
        return True
    else:
        return (a["lastLocation"] != b["lastLocation"]) or (a["userPresenceType"] != b["userPresenceType"])


def loadConfig():
    # load usernames / nicknames
    f = open("./config.json")
    config = json.load(f)
    f.close()
    # load ROBLOSECURITY if it exists
    loggedin = True
    cookie = ""
    try:
        f = open("./roblosecurity.json")
        cookie = json.load(f)["roblosecurity"]
        f.close()
    except FileNotFoundError:
        log("starting in logged out mode...", Fore.LIGHTMAGENTA_EX)
        loggedin = False
    return config["usernames"], loggedin, cookie
