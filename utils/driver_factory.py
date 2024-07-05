from appium import webdriver
from appium.options.android import UiAutomator2Options

def get_driver():
    options = UiAutomator2Options()
    options.platform_name = 'Android'
    options.platform_version = '13'
    options.device_name = '18211JEC202141'
    options.automation_name = 'Appium'
    options.app = "/Users/sharadbagul/Downloads/app-stage1.apk"
    options.no_reset = False
    options.app_wait_activity = "com.toro.horizon360.modules.login.view.LoginActivity"
    options.app_wait_package = "com.toro.horizon360"

    return webdriver.Remote('http://localhost:4723/wd/hub', options=options)   
