from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
import time
from appium.options.android import UiAutomator2Options

from pages.login import login


options = UiAutomator2Options()
options.platform_name = 'Android'
options.platform_version = '14'
options.device_name = '29271JEGR02209'
options.automation_name = 'Appium'
options.app = "/Users/idreameducation/Downloads/360.apk"
options.no_reset = True

def main():
    driver = webdriver.Remote('http://localhost:4723/wd/hub', options=options)    
    
    # home_page = Diag(driver)
    Login = login(driver)

    time.sleep(2)
    
    try:
        Login.loginfunc()

    except Exception as e:
        print(e)

    # Close the driver
    driver.quit()  

if __name__ == "__main__":
    main()