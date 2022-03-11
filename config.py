# Copyright (c) 2021 Itz-fork

import os


if os.environ.get("LOGS_CHANNEL"):
    log_channel = int(os.environ.get("LOGS_CHANNEL"))
else:
    log_channel = None

class Config(object):
    APP_ID = int(os.environ.get("APP_ID", 13554562))
    API_HASH = os.environ.get("API_HASH", "f018746a92d8e774664bebfb6f28abe5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5034854533:AAGmanPp5Xh1Dj46xnBwIdQiVVhzPNIl3RM")
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "853523454").split())
    DOWNLOAD_LOCATION = "./NexaBots"
    IS_PUBLIC_BOT = bool(os.environ.get("IS_PUBLIC_BOT", False))
    LOGS_CHANNEL = log_channel
    TG_MAX_SIZE = 2040108421
    # Mega User Account
    MEGA_EMAIL = os.environ.get("MEGA_EMAIL")
    MEGA_PASSWORD = os.environ.get("MEGA_PASSWORD")

# Text Prints
B_START_TEXT = """
   __  ___                                     ___       __ 
  /  |/  /__ ___ ____ _      ___  ___   ____  / _ )___  / /_
 / /|_/ / -_) _ `/ _ `/ _   / _ \/_ /  /___/ / _  / _ \/ __/
/_/  /_/\__/\_, /\_,_/ (_) /_//_//__/       /____/\___/\__/ 
           /___/

Process: {}
"""

PROCESS_TEXT = """
Process: {}
"""

LOGGED_AS_USER = """
Successfully Logged Into Mega.nz User Account
"""

LOGIN_ERROR_TEXT = """
Unable to find Mega Email and Password, Loging as an anonymous User...
"""

ERROR_TEXT = """
 _____                     
| ____|_ __ _ __ ___  _ __ 
|  _| | '__| '__/ _ \| '__|
| |___| |  | | | (_) | |   
|_____|_|  |_|  \___/|_|  

Log: {}

Save the Log file and Send it to @Nexa_bots for Help :)
"""

START_TEXT="""
    _   __                   ____        __      
   / | / /__  _  ______ _   / __ )____  / /______
  /  |/ / _ \| |/_/ __ `/  / __  / __ \/ __/ ___/
 / /|  /  __/>  </ /_/ /  / /_/ / /_/ / /_(__  ) 
/_/ |_/\___/_/|_|\__,_/  /_____/\____/\__/____/ 


Bot is Running Now! Join @NexaBotsUpdates
"""
