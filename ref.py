from src.core import *
from src.cucumber import _banner, log, mrh, pth, hju, kng, bru, htm
from global_config import *
import time
import pygetwindow as gw
import random
from pywinauto.keyboard import send_keys
from pywinauto.application import Application


# Function to search and click on the link
def click_link(bot_name):  # Give time for the link to display

    link = fr"pic\bots\{bot_name}.png"
    try:
        link_location = pyautogui.locateOnScreen(link, confidence=0.8)
        time.sleep(1)

    except Exception as e:
        log(f'Error while searching for image {bot_name}: {e}')

    if link_location:
        log(hju + "Link found. Clicking on it...")
        pyautogui.click(pyautogui.center(link_location))
        time.sleep(3)
        # Delay before pressing Enter
        send_keys('{ENTER}')  # Press Enter after 3 seconds
    else:
        log("Failed to find the link.")

def click_bot():
    time.sleep(1)  # Give time for the link to appear

    for image_path in bot_image_paths:
        try:
            link_location = pyautogui.locateOnScreen(image_path, confidence=0.8)
            if link_location:  # If the image is found, exit the loop
                break
        except Exception as e:
            log(f'Error while searching for image {image_path}: {e}')

    if link_location:
        log(hju + "Link found. Clicking on it...")
        pyautogui.click(pyautogui.center(link_location))
        time.sleep(1)  # Delay before pressing Enter
        send_keys('{ENTER}')  # Press Enter after 1 second
    else:
        log("Failed to find the link.")

# Function to interact with the bot
def focus_mini_app(bot_name):
    log(f"Focusing on the mini-app window for {bot_name}...")
    mini_app_window = gw.getWindowsWithTitle('TelegramDesktop')[0]

    if mini_app_window:
        print("mini_app_window", mini_app_window)
        mini_app_window.activate()  # Chuyển tiêu điểm sang cửa sổ TelegramDesktop
        log(f"TelegramDesktop window '{mini_app_window.title}' is now active.")

        # Lấy vị trí và kích thước của cửa sổ TelegramDesktop
        bbox = mini_app_window.box
        center_x, center_y = bbox.left + bbox.width // 2, bbox.top + bbox.height // 2

        # Nhấn chuột vào giữa cửa sổ (hoặc vị trí dự kiến của mini-app)
        pyautogui.click(center_x, center_y)
        log(f"Clicked at {center_x}, {center_y} to focus mini-app.")
    else:
        log(f"Mini-app window for {bot_name} not found. Please check!")
        raise Exception(f"Mini-app window for {bot_name} not found.")
    
def interact_with_bot(app, bot_name, code, account_num, row):
    log("Focusing on the Telegram window...")
    main_window = app.top_window()
    main_window.set_focus()

    log(f"Pressing the search button")
    click_seach()

    log(f"Entering the bot name: ...")
    main_window.type_keys(bot_name)
    time.sleep(2)

    log("Scrolling down 1 to 2 times")
    num_down_presses = random.randint(1, 2)
    for _ in range(num_down_presses):
        main_window.type_keys('{DOWN}')
        time.sleep(0.5)
    main_window.type_keys('{ENTER}')
    time.sleep(5)

    # Click on the link to launch the mini-application
    click_link(bot_name)

    time.sleep(2)

    bots_follow = ["bump", "dotcoin", 'otter_loot', 'fastmint', 'padton']

    if bot_name in bots_follow:
        click_bot()

    if bot_name == "fastmint":
        fastmint()

    time.sleep(2)

    # Focus on the mini-app window before pressing F12
    focus_mini_app(bot_name)

    # Open Developer Tools (press F12)
    log("Pressing F12 to open Developer Tools...")
    send_keys('{F12}')

    click_console(bot_name)

    # Switch to English layout
    keyboard.write('`')  # Simulating the ` key for switching console

    # Press Ctrl+` to activate command line
    log("Activating command line with Ctrl+`...")
    keyboard.press_and_release('ctrl+`')
    time.sleep(1)

    # Send the code string
    send_keys(code)
    time.sleep(1)

    # Press Enter
    send_keys('{ENTER}')
    time.sleep(1)

    # Copy data from clipboard and write to Excel
    write_to_excel(account_num, bot_name, row)

    # Function to write data to Excel
    log("Closing 2 windows")
    keyboard.press_and_release('alt+F4')
    time.sleep(0.5)

    # Handle specific bots
    bot_functions = {
        "matchquest": match_quest,
        "duckchain": duck_chain,
        "kucoin": kucoin,
        "birds": birds,
        "money_dogs": money_dogs,
        "catsdogs": catsdogs,
        "bitget": bitget,
        "coub": coub,
        "etherdrops": etherdrops,
        "padton": padton,
        "fabrika": fabrika,
        "pumpad": pumpad,
        "kiloextrade": kiloextrade,
    }

    if bot_name in bot_functions:
        bot_functions[bot_name]()

    keyboard.press_and_release('alt+F4')
    time.sleep(1)

    close_app()

    keyboard.press_and_release('Esc')
    time.sleep(0.5)

# Main function for working with multiple accounts
def main(account, bots_list, row):
    try:
        app, exe_file = launch_telegram(account)
        open_bot(app)
        for bot in bots_list:
            # Get the specific code for the bot or use the default if not found
            code = codes.get(bot, "copy+9Telegram.WebApp.initData+0")
            interact_with_bot(app, bot, code, account, row)
    except Exception as e:
        log(mrh + f"Error while interacting with account {account} with bot {bot}: {e}")
        open("error.log", "a", encoding="utf-8").write(
            f"Error while interacting with account {account} with bot {bot}: {e} \n")

    finally:
        close_telegram(account, exe_file)


# Loading accounts and bots
accounts_list = load_accounts_from_file('acc.txt')
bots_list = load_bots_from_file('bots.txt')

# Get the total number of accounts
total_accounts = len(accounts_list)

_banner()
log(f'Starting query collection for bots: {bru} {bots_list}')
log(f'Total accounts to process: {bru} {total_accounts}')

row = 1

for index, account in enumerate(accounts_list, start=1):
    log(f'Processing account {bru} {index} of {total_accounts}...')
    row += 1
    main(account, bots_list, row)