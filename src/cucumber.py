from datetime import datetime
import os
from colorama import Fore, Style


mrh = Fore.LIGHTRED_EX
pth = Fore.LIGHTWHITE_EX
hju = Fore.LIGHTGREEN_EX
kng = Fore.LIGHTYELLOW_EX
bru = Fore.LIGHTBLUE_EX
reset = Style.RESET_ALL
htm = Fore.LIGHTBLACK_EX


def log(message):
    now = datetime.now().isoformat(" ").split(".")[0]
    print(f"{htm}[{now}]{pth} {message}{reset}")

def _banner():
    banner = r""
    log_line()


def _clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def log_line():
    print(pth + "~" * 60)