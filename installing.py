from selenium import webdriver        # google translate e bağlanıp 10 sn açık tutar , sonra kapanır.
import time

# driver = webdriver.Chrome()
driver = webdriver.Edge()

url = "https://translate.google.com/"

driver.get(url)
time.sleep(10)