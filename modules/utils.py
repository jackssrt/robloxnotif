from json.decoder import JSONDecodeError
from modules.classes import Config
from modules.console import log

from colorama import Fore, Back, Style
import json
import os
import re

regex = re.compile(
    r"(\".*?\"|\'.*?\')|(/\*.*?\*/|//[^\r\n]*$)", re.MULTILINE | re.DOTALL)


def loadJson(path: str):
    try:
        if not os.path.exists(path) or not os.path.isfile(path):
            raise FileNotFoundError("File doesnt exist")
        # taken from jsonc-parser

        def __re_sub(match: re.Match):
            if match.group(2) is not None:
                return ""
            else:
                return match.group(1)
        with open(path, "r")as f:
            data = f.read()
        return json.loads(regex.sub(__re_sub, data))
    except JSONDecodeError as e:
        from modules.errorhandlers import corruptedJson
        corruptedJson(e, os.path.basename(path))


def loadConfig(filename_c: str = "config.jsonc", filename_r: str = "roblosecurity.jsonc") -> Config:
    # load usernames / nicknames
    try:
        config = loadJson(filename_c)
    except FileNotFoundError as e:
        from modules.errorhandlers import logError
        logError(
            e, "Could not find a config.jsonc!\nHave you setup robloxnotif correctly or is it missing??")
        exit()

    # load ROBLOSECURITY if it exists
    loggedin = True
    cookie = ""
    try:
        cookie = loadJson(filename_r)["roblosecurity"]
    except FileNotFoundError:
        log("starting in logged out mode...", Fore.LIGHTMAGENTA_EX)
        loggedin = False
    return Config(config["usernames"], loggedin, cookie)
