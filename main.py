### Original Developer : Alif Aditya Wicaksono

import time
import logging
import AutoLoginService
from Account import UserParameters

# Set the threshold for selenium to WARNING
from selenium.webdriver.remote.remote_connection import LOGGER as seleniumLogger
seleniumLogger.setLevel(logging.NOTSET)

# Set the threshold for urllib3 to WARNING
from urllib3.connectionpool import log as urllibLogger
urllibLogger.setLevel(logging.WARNING)

print("starting....")

user_account = UserParameters()
login_service = AutoLoginService.ITSAutoLogger(user_account)

login_service.start()

while True:
    connected = login_service.checkLoginStatus()
    if connected:
        print("Connected \t" + time.strftime("%H:%M:%S :: %d/%m/%Y"))
    else:
        print("Trying to Login...")
        tryLogin = login_service.login()
        if tryLogin:
            print("Success !")
        else:
            print("Unkown failure.... Waiting 5 minutes before tying again....")
            time.sleep(60 * 5)
    time.sleep(60 * 10)
