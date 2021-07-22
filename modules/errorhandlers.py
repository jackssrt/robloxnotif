import json
import requests.exceptions
from colorama import Fore, Back, Style, init
import traceback
from modules.console import warn, error
from modules.notifications import errorNotify
init(True)


def logError(e, msg):

    with open("./error.log", "w", encoding="utf-8") as f:
        traceback.print_exc(file=f)
    text = f"""Robloxnotif has errored:
Error: {type(e).__name__} {e}
Message: {msg}
Check error.log for a traceback."""
    error(text, Fore.LIGHTRED_EX)
    first, *others = text.splitlines()
    errorNotify(first, "\n".join(others))


def logErrorWarn(e, msg):
    with open("error.log", "w", encoding="utf-8") as f:
        traceback.print_exc(file=f)

    text = f"""Robloxnotif has errored but it will continue running.
Error: {type(e).__name__} {e}
Message: {msg}
Check error.log for a traceback."""
    warn(text, Fore.LIGHTYELLOW_EX)

    first, *others = text.splitlines()
    errorNotify(first, "\n".join(others))


def handleMainLoopError(e, data):
    if type(e) == KeyError:
        try:
            text = str(data["errors"][0]["code"])
            text2 = str(data["errors"][0]["message"])
            logErrorWarn(e, f"Api error: code {text}:\n{text2}")
        except KeyError:
            handleUnexpectedError(e)
    elif type(e) == requests.exceptions.SSLError:
        logErrorWarn(e, "Normal connection error, Retrying...")
    elif type(e) == requests.exceptions.ConnectionError:
        logErrorWarn(e, "Normal connection error, Retrying...")
    elif type(e) == json.decoder.JSONDecodeError:
        logErrorWarn(e, "JSON decoding error, Retrying...")
    # if you are here to add handling for another type of exception
    # remember to add it to the list in the except line that calls this function.


def handleUnexpectedError(e):
    logError(e, "Unexpected error, Can't continue running.")
    exit()  # exit to prevent spamming roblox with requests


def corruptedJson(e, filename):
    logError(
        e, f"Corrupt JSON File\nLooks like the JSON file \"{filename}\" is corrupt!")
    exit()
