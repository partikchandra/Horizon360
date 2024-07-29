import pytest
from Horizon360.page_objects.test_Loginpage import LoginTest as login
from page_objects.homepage import homepage as home
from utils.driver_factory import get_driver
import time 

# @pytest.fixture(scope="module")
# def driver(uid, port):
#     driver = get_driver(uid, port)
#     yield driver
#     driver.quit()
    
# Test Case for Allow Different App permissions before landing user to home screen
def homepagepermissions(d1):
    try:
        print("Allow Visible")
        login(d1).login_QA("prachi.auti+test1@toro.com","Prachi@93")
        home(d1).clickallowNotifications()
        home(d1).clicklocPermission()
        home(d1).clickwhileUsingTheApp()
        home(d1).clickhamburgerMenu()
        home(d1).clicksignOutbutton()
        home(d1).clickyesbutton()
    except Exception as e:
        print(f"No more permission dialogs found.")

# Test Case for Allow Different App permissions before landing user to home screen
def VerifyNotificationsdonotallow(d2):
    try:
        print("Allow Visible")
        login(d2).login_QA("prachi.auti+test1@toro.com","Prachi@93")
        home(d2).clickdontallowNotifications()
        home(d2).clicklocPermission()
        home(d2).clickwhileUsingTheApp()
        home(d2).clickhamburgerMenu()
        home(d2).clicksignOutbutton()
        home(d2).clickyesbutton()
    except Exception as e:
        print(f"No more permission dialogs found.")
    
def test_1_allcases():
 #   d1 =  get_driver('18211JEC202141', 8201)
    d2 =  get_driver('00008101-000108111E60001E', 8202)
# #homepagepermissions(d1)
    VerifyNotificationsdonotallow(d2)