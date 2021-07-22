from json.decoder import JSONDecodeError
from modules.console import log
from modules.errorhandlers import corruptedJson, logError
from colorama import Fore, Back, Style, init
import json
import os
init(True)


def isChanged(a, b):  # function for checking if presence has changed or not
    if not a or not b:
        return True
    else:
        return (a["lastLocation"] != b["lastLocation"]) or (a["userPresenceType"] != b["userPresenceType"])


def loadJson(path):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except JSONDecodeError as e:
        corruptedJson(e, os.path.basename(path))


def loadConfig():
    # load usernames / nicknames
    try:
        config = loadJson("./config.json")
    except FileNotFoundError as e:
        logError(
            e, "Could not find a config.json!\nHave you setup robloxnotif correctly or is it missing??")
        exit()
    # load ROBLOSECURITY if it exists
    loggedin = True
    cookie = ""
    try:
        cookie = loadJson("./roblosecurity.json")["roblosecurity"]
    except FileNotFoundError:
        log("starting in logged out mode...", Fore.LIGHTMAGENTA_EX)
        loggedin = False
    return config["usernames"], loggedin, cookie
