from appium import webdriver
from appium.options.android import UiAutomator2Options

def get_driver():
    options = UiAutomator2Options()
    options.platform_name = 'Android'
    options.platform_version = '14'
    options.device_name = '29271JEGR02209'
    options.automation_name = 'Appium'
    options.app = "/Users/idreameducation/Downloads/360.apk"
    options.no_reset = False
    options.app_wait_activity = "com.toro.horizon360.modules.login.view.LoginActivity"
    options.app_wait_package = "com.toro.horizon360"

    driver = webdriver.Remote('http://localhost:4723/wd/hub', options=options)
    return driver
