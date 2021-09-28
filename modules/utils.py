from json.decoder import JSONDecodeError
from modules.console import log

from colorama import Fore, Back, Style, init
import json
import os
from jsonc_parser.parser import JsoncParser
from jsonc_parser.errors import FileError, FunctionParameterError, ParserError

init(True)


def isChanged(a, b):  # function for checking if presence has changed or not
    if not a or not b:
        return True
    else:
        return (a["lastLocation"] != b["lastLocation"]) or (a["userPresenceType"] != b["userPresenceType"])


def loadJson(path):

    try:
        return JsoncParser.parse_file(path)
    except ParserError as e:
        from modules.errorhandlers import corruptedJson
        corruptedJson(e, os.path.basename(path))


def loadConfig():
    # load usernames / nicknames
    try:
        config = loadJson("./config.jsonc")
    except FileError as e:
        from modules.errorhandlers import logError
        logError(
            e, "Could not find a config.jsonc!\nHave you setup robloxnotif correctly or is it missing??")
        exit()
    # load ROBLOSECURITY if it exists
    loggedin = True
    cookie = ""
    try:
        cookie = loadJson("./roblosecurity.jsonc")["roblosecurity"]
    except (FileError, FunctionParameterError):
        log("starting in logged out mode...", Fore.LIGHTMAGENTA_EX)
        loggedin = False
    return config["usernames"], loggedin, cookie
