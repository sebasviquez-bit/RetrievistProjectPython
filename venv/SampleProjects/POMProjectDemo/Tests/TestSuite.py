import time
from POMProjectDemo.BaseClass.BaseClass import baseClass
from POMProjectDemo.Pages.HomePage import homePage
import pytest


class testSuite (baseClass):

# HomePage Tests >

    def test_Click_BrowseMenu(self):

        driver = self.driver
        BrowseMenu = homePage(driver)
        BrowseMenu.Click_BrowseMenu()

    def test_Click_DealsMenu(self):

        driver = self.driver
        DealsMenu = homePage(driver)
        DealsMenu.Click_DealsMenu()

    def test_Click_GiftIcon(self):

        driver = self.driver
        GiftIcon = homePage(driver)
        GiftIcon.Click_GiftIcon()

    def test_SignIN(self):

        driver = self.driver
        MyAccount = homePage(driver)
        MyAccount.SingIN()

    def test_SignUp_Email(self):

       driver = self.driver
       EmailCase = homePage(driver)
       EmailCase.SignUp_Email()




