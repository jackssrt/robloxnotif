from colorama import Fore, Back, Style, init
from datetime import datetime

init(True)


def error(text: str, color: str = "") -> None:
    log(f"{Fore.LIGHTRED_EX}[ERROR]{Style.RESET_ALL}{color} {text}", Fore.LIGHTRED_EX)


def warn(text: str, color: str = "") -> None:
    log(
        f"{Fore.LIGHTYELLOW_EX}[WARN]{Style.RESET_ALL}{color} {text}",
        Fore.LIGHTYELLOW_EX,
    )


def log(text: str, color: str = "") -> None:  # log function
    now = datetime.now().strftime("%X")
    print(f"{color}{Style.DIM}[{now}]:{Style.RESET_ALL}{color} {text}")
