from selenium import webdriver
import time
from Account import UserParameters

test = True

class ITSAutoLogger:
    def __init__(self, UserInfo : UserParameters):
        self.driver = webdriver.Firefox(executable_path='./firefox_geckodriver/geckodriver')
        print("Using ->", UserInfo)
        self.Username = UserInfo.username
        self.Password = UserInfo.password
        self.LoginPage = "https://myits-app.its.ac.id/internet/index.php"
        
    def start(self):
        self.driver.get(self.LoginPage)
        time.sleep(3)
        
        if 'Akses internet hanya diperbolehkan dari alamat IP internal ITS' in self.driver.page_source:
            print("your extrenal to ITS intranet, please login from intranet")
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
            
            print("|> Looking for button...")
            self.driver.find_element_by_link_text('Akses Internet Personal').click()
            time.sleep(10)
            
            print("|> Writing Username")
            self.driver.find_element_by_id('username').send_keys(self.Username)
            time.sleep(1)

            print("|> Waiting for animation...")
            self.driver.find_element_by_id('continue').click()
            time.sleep(10)

            print("|> Writing Password")
            self.driver.find_element_by_id('password').send_keys(self.Password)
            time.sleep(2)

            print("|> Loggin in...")
            self.driver.find_element_by_id('login').click()
            time.sleep(4)
            
            return self.checkLoginStatus()
        except:
            return False
        
