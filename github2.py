from githubUserInfo import username, password     # kullanıcı adı ve şifrenin çekildiğ, .py uzantılı dosya
from selenium import webdriver
from selenium.webdriver.common.by import By        # selenium - css selector kullanımında sorun var !!!!
from selenium.webdriver.common.keys import Keys
import time

class GitHub:
    def __init__(self,username,password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        self.followers = []

    def signIn(self):
        self.browser.get("http://github.com/login")
        time.sleep(2)

        self.browser.find_element(By.XPATH,"//*[@id='login_field']").send_keys(self.username) # //*[@id="login_field"]
        self.browser.find_element(By.XPATH,"//*[@id='password']").send_keys(self.password) # //*[@id="password"]

        time.sleep(2)

        self.browser.find_element(By.XPATH,"//*[@id='login']/div[4]/form/div/input[11]").click()  # //*[@id="login"]/div[4]/form/div/input[11]

        time.sleep(2)
    
    def getFollowers(self):
        self.browser.get(f"https://github.com/{self.username}?tab=followers")
        time.sleep(2)
        items = self.browser.find_elements(By.XPATH,"//*[@id='user-profile-frame']/div/div[1]/div[2]")
        for i in items:
            self.followers.append(i.find_element(By.XPATH,"//*[@id='user-profile-frame']/div/div[1]/div[2]/a/span[1]").text)
        
    

github = GitHub(username, password)
github.signIn()
github.getFollowers()
print(github.getFollowers)