import time
import logging
from selenium import webdriver
from Account import UserParameters
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options


class ITSAutoLogger:
    def __init__(self, UserInfo : UserParameters, logger : logging.Logger):
        self.logger = logger
        options = Options()
        options.headless = True
        self.driver = webdriver.Firefox(
            executable_path = './firefox_geckodriver/geckodriver',
            options         = options
        )
        self.logger.info("Using ->", UserInfo)
        self.Username = UserInfo.username
        self.Password = UserInfo.password
        self.LoginPage = "https://myits-app.its.ac.id/internet/index.php"
        
    def start(self):
        self.driver.get(self.LoginPage)
        time.sleep(3)
        
        if 'Akses internet hanya diperbolehkan dari alamat IP internal ITS' in self.driver.page_source:
            self.logger.info("your extrenal to ITS intranet, please login from intranet")
            time.sleep(60 * 60)
            exit()
        
        #check if login page
        if 'Akses Internet Personal' in self.driver.page_source:
            self.login()
    
    def checkLoginStatus(self) -> bool:
        self.driver.get(self.LoginPage)
        time.sleep(3)
        
        if 'Anda telah terhubung dengan internet ITS' in self.driver.page_source:
            return True
        else:
            return False
    
    def login(self) -> bool:
        try:
            self.driver.get(self.LoginPage)
            time.sleep(10)
            
            self.logger.info("|> Looking for button...")
            self.driver.find_element(By.LINK_TEXT, 'Akses Internet Personal').click()
            time.sleep(10)
            
            self.logger.info("|> Writing Username")
            self.driver.find_element(By.ID, 'username').send_keys(self.Username)
            time.sleep(1)

            self.logger.info("|> Waiting for animation...")
            self.driver.find_element(By.ID, 'continue').click()
            time.sleep(10)

            self.logger.info("|> Writing Password")
            self.driver.find_element(By.ID, 'password').send_keys(self.Password)
            time.sleep(2)

            self.logger.info("|> Loggin in...")
            self.driver.find_element(By.ID, 'login').click()
            time.sleep(4)
            
            return self.checkLoginStatus()
        except Exception as Ex:
            self.logger.info("|> Error Found :", Ex)
            return False
        
