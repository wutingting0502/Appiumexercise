import os
import unittest
from appium import webdriver
from time import sleep
import time

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class ContactsAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1'
        desired_caps['deviceName'] = '127.0.0.1:62001'
        desired_caps['app'] = PATH(
            'C:/android-sdk-windows/build-tools/27.0.3/com.tencent.padbrowser-2.3.5.135.apk'
        )
        desired_caps['appPackage'] = 'com.tencent.padbrowser'
        desired_caps['appActivity'] = '.MainActivity'
        desired_caps['noReset'] = 'true'
        desired_caps['newCommandTimeout'] = 20


        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        waitFor(5)

    def tearDown(self):
        self.driver.quit()

    def test_add_contacts(self):

        browserfield= self.driver.find_element_by_id("com.tencent.padbrowser:id/etAddressBox")
        browserfield.clear()
        browserfield.send_keys("www.baidu.com")



        # for some reason "save" breaks things
        #alert = self.driver.switch_to_alert()

        # no way to handle alerts in Android
        #self.driver.find_element_by_android_uiautomator('new UiSelector().clickable(true)').click()

        #self.driver.press_keycode(3)

def waitFor(t):
  time.sleep(t)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ContactsAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)