from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from appium.options.android import UiAutomator2Options

from pages.login import login


options = UiAutomator2Options()
options.platform_name = 'Android'
options.platform_version = '13'
options.device_name = '18211JEC202141'
options.automation_name = 'Appium'
options.app = "/Users/sharadbagul/Downloads/app-stage1.apk"
options.no_reset = False
options.app_wait_activity = "com.toro.horizon360.modules.login.view.LoginActivity"
options.app_wait_package = "com.toro.horizon360"

def main():
    driver = webdriver.Remote('http://localhost:4723/wd/hub', options=options)    

    # Policy Page
    # WebDriverWait(driver,  20).until(EC.element_to_be_clickable(By.XPATH, '//android.widget.TextView[@text="Save Changes"]')).click()
    
    # home_page = Diag(driver)
    
    Login = login(driver)

    time.sleep(2)
    
    try:
        Login.onboard()

    except Exception as e:
        print(e)

    # Close the driver
    driver.quit()  

if __name__ == "__main__":
    main()