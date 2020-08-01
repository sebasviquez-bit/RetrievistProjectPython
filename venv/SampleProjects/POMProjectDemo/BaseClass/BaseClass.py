import os

from applitools.selenium import Eyes, MatchLevel, StitchMode, StdoutLogger
from selenium import webdriver
import unittest


class baseClass(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome('/Users/user/PycharmProjects/AKCProject/chromedriver')
        self.driver.get("https://test-commerce-content.pantheonsite.io/")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def eyes_setup(self): #This function needs to be set correctly

         self.driver.eyes = Eyes
         self.driver.eyes.setApiKey("pQamgLj3eFvTyisdPKdOm7dXxPtyM1JhNt6Wd4q5Ofk110")
         self.driver.eyes.setLogHandler(StdoutLogger)
         self.driver.eyes.setForceFullPageScreenshot()
         self.driver.eyes.setStitchMode(StitchMode.CSS)
         self.driver.eyes.setMatchLevel(MatchLevel.LAYOUT)

    def tearDown(self):

        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main
