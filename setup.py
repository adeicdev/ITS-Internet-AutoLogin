import os
import sys
import shutil
import subprocess

# check if linux
if sys.platform != "linux":
    print("This systemd setup is for linux os only !")
    #exit()

# check if root !
if os.geteuid() != 0:
    print("Please get root privilages such as sudo")
    exit()

subprocess.run(["pip", "install", "selenium"])

print("Copying the service file")
shutil.copy('./its_autologin.service', "/etc/systemd/system/its_autologin.service")

currect_cwd = os.getcwd()
current_usr = os.getlogin()

service_file_str = open('/etc/systemd/system/its_autologin.service').read()

service_file_str = service_file_str.replace("$PWD"    , currect_cwd)
service_file_str = service_file_str.replace("$usrname", current_usr)

project_config_file = open('/etc/systemd/system/its_autologin.service', "w")
project_config_file.write(service_file_str)
project_config_file.close()

print("Reloading systemd")
subprocess.run(["systemctl", "daemon-reload"])

print("Enabling ITS its_autologin.service")
subprocess.run(["systemctl", "enable", "its_autologin.service"])

print("Starting its_autologin.service")
subprocess.run(["systemctl", "start", "its_autologin.service"])
