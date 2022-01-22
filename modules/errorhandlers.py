import json
from typing import List
from modules.classes import ApiError
import requests.exceptions
from colorama import Fore, Back, Style
import traceback
from modules.console import warn, error
from modules.notifications import errorNotify


def logError(e: BaseException, msg: str) -> None:

    with open("./error.log", "w", encoding="utf-8") as f:
        traceback.print_exc(file=f)
    text = f"""[FATAL] {type(e).__name__} {e}
{msg}
Check error.log for a traceback."""
    error(text, Fore.LIGHTRED_EX)
    first, *others = text.splitlines()
    errorNotify(first, "\n".join(others))


def logErrorWarn(e: BaseException, msg: str) -> None:
    with open("error.log", "w", encoding="utf-8") as f:
        traceback.print_exc(file=f)

    text = f"""{type(e).__name__} {e}
{msg}
Check error.log for a traceback."""
    warn(text, Fore.LIGHTYELLOW_EX)

    first, *others = ("[WARN] " + text).splitlines()
    errorNotify(first, "\n".join(others))


def handleApiError(e: BaseException, errors: List[ApiError]):
    for error in errors:
        text = str(error.code)
        text2 = error.message
        logErrorWarn(e, f"Api error: {text}\n{text2}")


def handleMainLoopError(e: BaseException) -> None:
    if type(e) == requests.exceptions.SSLError:
        logErrorWarn(e, "Normal connection error, Retrying...")
    elif type(e) == requests.exceptions.ConnectionError:
        logErrorWarn(e, "Normal connection error, Retrying...")
    elif type(e) == json.decoder.JSONDecodeError:
        logErrorWarn(e, "JSON decoding error, Retrying...")
    # if you are here to add handling for another type of exception
    # remember to add it to the list in the except line that calls this function.


def handleUnexpectedError(e: BaseException) -> None:
    logError(e, "Unexpected error, Can't continue running.")
    exit()  # exit to prevent spamming roblox with requests


def corruptedJson(e: BaseException, filename: str):
    logError(e, f'Corrupt JSON File\nLooks like the JSON file "{filename}" is corrupt!')
    exit()
