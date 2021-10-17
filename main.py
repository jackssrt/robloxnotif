from modules.classes import ApiError, Presence
from modules.utils import loadConfig
from modules.console import log
from modules.notifications import notify
from modules.errorhandlers import handleApiError, handleMainLoopError, handleUnexpectedError
from colorama import Fore, Back, Style
import requests
from time import sleep
import json


def main():
    try:  # main loop
        last: list[Presence] = []
        config = loadConfig()
        shouldWait: bool = False
        while True:
            if len(last) != 0:
                log("***---***", Fore.WHITE)
            if shouldWait:
                sleep(10)
            shouldWait = True
            try:
                x = requests.post(
                    'https://presence.roblox.com/v1/presence/users',
                    data={"userIds": list(config.usernames.keys())},
                    cookies={
                        ".ROBLOSECURITY": config.cookie} if config.loggedIn else {}
                )
                _data: dict = x.json()
                if _data["userPresences"]:
                    presences = [Presence(**i)
                                 for i in _data["userPresences"]]
                elif _data["errors"]:
                    errors = [ApiError(**i) for i in _data["errors"]]
                    handleApiError(errors)
                    continue
                if len(last) == 0:
                    log("Running boot notifications: ", Fore.CYAN)

                for a in range(len(presences)):
                    if len(last) != 0:
                        if presences[a] != last[a]:
                            notify(config.usernames,
                                   presences[a], False)
                    else:
                        # run boot notifications
                        notify(config.usernames,
                               presences[a], True)
                last = presences.copy()
            except (requests.exceptions.ConnectionError, requests.exceptions.SSLError, json.decoder.JSONDecodeError) as e:
                handleMainLoopError(e)

    except Exception as e:
        handleUnexpectedError(e)


if __name__ == "__main__":
    main()
