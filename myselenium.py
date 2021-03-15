# Write a code for autologin facebook and gmail account
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
class Login:
    def __init__(self):
        self.service = Service("C:\\Users\\Dileep-Pcs\\Downloads\\Compressed\\chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.maximize_window()
    def geturl(self):
        self.url="http://www.facebook.com"
    def getlogin(self):
        self.driver.get(self.url)
        self.username = self.driver.find_element_by_id('email')
        self.password = self.driver.find_element_by_id('pass')
        self.username.clear()
        self.password.clear()
        self.username.send_keys('')
        self.password.send_keys('')
        self.login=self.driver.find_element_by_name('login')
        self.login.click()
if __name__=='__main__':
    facebook = Login()
    facebook.geturl()
    facebook.getlogin()






