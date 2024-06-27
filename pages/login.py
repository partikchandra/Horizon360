from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
import time
from appium.options.android import UiAutomator2Options


# rpu2307+h251@gmail.com & ttt@0000

class login:
    def __init__(self, driver):
        self.driver = driver
        self.username = (By.ID, "com.toro.horizon360:id/email_edit_text")
    
    def loginfunc(self):

        try:
            user = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((self.username)))
            user.send_keys("rpu2307+h251@gmail.com")
        except Exception as e:
            print("Error ", e)