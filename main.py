### Original Developer : Alif Aditya Wicaksono

import time
import logging
import sys
import AutoLoginService
from systemd.journal import JournalHandler
from Account import UserParameters

# Set the threshold for selenium to WARNING
from selenium.webdriver.remote.remote_connection import LOGGER as seleniumLogger
seleniumLogger.setLevel(logging.NOTSET)

# Set the threshold for urllib3 to WARNING
from urllib3.connectionpool import log as urllibLogger
urllibLogger.setLevel(logging.WARNING)

# Get an instance of the logger
LOGGER = logging.getLogger(__name__)

# Instantiate the JournaldLogHandler to hook into systemd
JOURNALD_HANDLER = JournalHandler()
JOURNALD_HANDLER.setFormatter(logging.Formatter(
    '[%(levelname)s] %(message)s'
))

# Add the journald handler to the current logger
LOGGER.addHandler(JOURNALD_HANDLER)
LOGGER.setLevel(logging.INFO)

LOGGER.info("starting....")

user_account = UserParameters()
login_service = AutoLoginService.ITSAutoLogger(user_account, LOGGER)

login_service.start()

while True:
    connected = login_service.checkLoginStatus()
    if connected:
        LOGGER.info("Connected \t" + time.strftime("%H:%M:%S :: %d/%m/%Y"))
    else:
        LOGGER.info("Trying to Login...")
        tryLogin = login_service.login()
        if tryLogin:
            LOGGER.info("Success !")
        else:
            LOGGER.info("Unkown failure.... Waiting 5 minutes before tying again....")
            time.sleep(60 * 5)
    time.sleep(60 * 10)
