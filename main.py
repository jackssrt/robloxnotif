from modules.utils import loadConfig, isChanged, log
from modules.notifications import notify
from modules.errorhandlers import handleMainLoopError, handleUnexpectedError
from colorama import Fore, Back, Style
import requests
from time import sleep
import json


def main():
    try:  # main loop
        last = {}
        usernames, loggedIn, cookie = loadConfig()
        while True:
            try:
                data = {}
                if loggedIn:
                    x = requests.post(
                        'https://presence.roblox.com/v1/presence/users',
                        data={"userIds": list(usernames.keys())},
                        cookies={".ROBLOSECURITY": cookie}
                    )
                else:
                    x = requests.post(
                        'https://presence.roblox.com/v1/presence/users',
                        data={"userIds": list(usernames.keys())}
                    )
                data = x.json()

                if last == {}:
                    log("Running boot notifications: ", Fore.CYAN)

                for a in range(len(data['userPresences'])):
                    if last != {}:
                        if isChanged(data['userPresences'][a], last['userPresences'][a]):
                            notify(usernames, data['userPresences'][a], False)
                    else:
                        # run boot notifications
                        notify(usernames, data['userPresences'][a], True)
                last = data
            except (requests.exceptions.ConnectionError, requests.exceptions.SSLError, KeyError, json.decoder.JSONDecodeError) as e:
                handleMainLoopError(e, data)
            log("***---***", Fore.WHITE)
            sleep(10)
    except Exception as e:
        handleUnexpectedError(e)


if __name__ == "__main__":
    main()
