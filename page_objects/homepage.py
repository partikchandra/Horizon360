from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class homepage(object):
    def __init__(self, driver):
        self.driver = driver
        self.allowNotifications = (By.ID, "com.android.permissioncontroller:id/permission_allow_button")
        self.dontallowNotifications = (By.ID, "com.android.permissioncontroller:id/permission_deny_button")
        self.locPermission = (By.ID, "com.toro.horizon360:id/positive_btn")
        self.whileUsingTheApp = (By.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button")
        self.hamburgermenu = (By.ID, "com.toro.horizon360:id/toolbar_hamburger")
        self.sign_out_button = (By.ID, "com.toro.horizon360:id/nav_sign_out_txt")
        self.yesbutton = (By.ID, "com.toro.horizon360:id/positive_btn")

    # Functions to perform operations on Home page
    #Click Allow Notifications popup
    def clickallowNotifications(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.allowNotifications)).click()

    #Click Don't Allow Notifications popup
    def clickdontallowNotifications(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.dontallowNotifications)).click()
            
    #Click Location Persmission popup  
    def clicklocPermission(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.locPermission)).click()
            
    #Click While using app permission   
    def clickwhileUsingTheApp(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.whileUsingTheApp)).click()
            
    #Click Hamburger Menu Option   
    def clickhamburgerMenu(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.hamburgermenu)).click()
            
    #Click Sign Out Button   
    def clicksignOutbutton(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.sign_out_button)).click()

    #Click Sign Out Button   
    def clickyesbutton(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.yesbutton)).click()


   
