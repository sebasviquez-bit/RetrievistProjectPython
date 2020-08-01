from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from POMProjectDemo.BaseClass.BaseClass import baseClass


class homePage(baseClass):

#Constructor:

    def __init__(self, driver):
        self.driver = driver

#Elements:

        self.BrowseMenu = "body > header > div.c-header-brand > a.hamburger.js-hamburger > span"
        self.DealsMenu = "#menu-item-783 > a"
        self.GiftIcon = "body > header > div.c-header-main-nav > div.header-main-nav--icons.js-nav-fade > a > svg > path"
        self.Bedding = "#menu-item-783 > a"
        self.Collars = "#menu-item-1067 > a > img"
        self.Crates = "#menu-item-1068 > a > img"
        self.Leashes = "#menu-item-1071 > a > img"
        self.Treats = "#menu-item-1070 > a > img"
        self.Toys = "#menu-item-1069 > a > img"
        self.DealsMenu = "#menu-item-783 > a"
        self.DealsMenu_Title = "body > main > section > h1"
        self.DealsMenu_Product = "body > main > section > div > a:nth-child(1) > div.card__img > div"
        self.DealsMenu_Filter = "body > main > section > a"
        self.DealsMenu_Category = "body > main > div > section > div.cat-filter__header.js-drawer-mobile-trigger > h4"
        self.DealsMenu_Price = "body > main > div > div.sort-buttons.sort-price.js-drawer-mobile > div.sort-price__header.js-drawer-mobile-trigger > h4"
        self.DealsMenu_Reviews = "body > main > div > div.sort-reviews.js-drawer-mobile > div.sort-reviews__header.js-drawer-mobile-trigger > h4"
        self.GiftIcon = "body > header > div.c-header-main-nav > div.header-main-nav--icons.js-nav-fade > a > svg > path"
        self.GiftFinderTitle = "#relationship > h2"
        self.MyDogButton = "#relationship > div.c-tags.select-single > a:nth-child(1)"
        self.NotMyDogButton = "#relationship > div.c-tags.select-single > a:nth-child(2)"
        self.NextButton = "#relationship > div.c-progress-btns > a"
        self.EmailCase = "#sailthru-subscribe-id--1 > div.sailthru_form_input.form-group > input"
        self.EmailSubmitButton = "#sailthru-subscribe-id--1 > span > button"
        self.EmailSubsConfirm = "#subscription > div > div.sailthru_shortcode > div > div > div.success"
        self.MyAccountIcon = "body > header > div.c-header-main-nav > div.header-main-nav--icons.js-nav-fade > a.js-account-btn"
        self.LoginForm = "loginform_content_caption"
        self.UserName = "#gigya-login-form > div:nth-child(1) > div.gigya-composite-control.gigya-composite-control-textbox > input"
        self.Password = "#gigya-login-form > div:nth-child(1) > div.gigya-composite-control.gigya-composite-control-password > input"
        self.LoginButton = "#gigya-login-form > div:nth-child(1) > div.gigya-composite-control.gigya-composite-control-submit.js-submit-login > input"
        self.GoogleButton = "Google_btn"
        self.FaceBookButton = "#loginform_social_0_uiContainer > div > table > tbody > tr > td.gigya-login-providers-list-container > div > div > div > span.gigya-login-provider.gigya-login-provider-last"
        self.PasswReset = "#gigya-login-form > div.gigya-layout-row.with-divider > div.gigya-layout-cell.responsive.with-social-login > div > a"
        self.CreateAccount = "#gigya-login-form > div.gigya-layout-row.with-divider > div.gigya-layout-cell.responsive.with-site-login > a"
        self.MyAccountTitle = "body > main > section.account__dashboard > div.account__heading > h1"
        self.LogOutButton = "body > main > section.account__dashboard > div.account__heading > a"

#Functions:

    def Click_BrowseMenu(self):

        self.driver.find_element_by_css_selector(self.BrowseMenu).click()
        self.driver.find_element_by_css_selector(self.Bedding).is_displayed()
        self.driver.find_element_by_css_selector(self.Collars).is_displayed()
        self.driver.find_element_by_css_selector(self.Crates).is_displayed()
        self.driver.find_element_by_css_selector(self.Leashes).is_displayed()
        self.driver.find_element_by_css_selector(self.Treats).is_displayed()
        self.driver.find_element_by_css_selector(self.Toys).is_displayed()

    def Click_DealsMenu(self):

        self.driver.find_element_by_css_selector(self.DealsMenu).click()
        self.driver.find_element_by_css_selector(self.DealsMenu_Title).is_displayed()
        self.driver.find_element_by_css_selector(self.DealsMenu_Product).is_displayed()
        self.driver.find_element_by_css_selector(self.DealsMenu_Filter).is_displayed()
        self.driver.find_element_by_css_selector(self.DealsMenu_Category).is_displayed()
        self.driver.find_element_by_css_selector(self.DealsMenu_Price).is_displayed()
        self.driver.find_element_by_css_selector(self.DealsMenu_Reviews).is_displayed()

    def Click_GiftIcon(self):

        self.driver.find_element_by_css_selector(self.GiftIcon).click()
        self.driver.find_element_by_css_selector(self.GiftFinderTitle).is_displayed()
        self.driver.find_element_by_css_selector(self.MyDogButton).is_displayed()
        self.driver.find_element_by_css_selector(self.NotMyDogButton).is_displayed()
        self.driver.find_element_by_css_selector(self.NextButton).is_displayed()

    def SingIN(self):

        self.driver.find_element_by_css_selector(self.MyAccountIcon).click()
        self.driver.find_element_by_id(self.LoginForm).is_displayed()
        self.driver.find_element_by_css_selector(self.UserName).send_keys("sxv@akc.org")
        self.driver.find_element_by_css_selector(self.Password).send_keys("cypreshill2*")
        self.driver.find_element_by_css_selector(self.LoginButton).is_displayed()
        self.driver.find_element_by_css_selector(self.PasswReset).is_displayed()
        self.driver.find_element_by_css_selector(self.CreateAccount).is_displayed()
        self.driver.find_element_by_css_selector(self.FaceBookButton).is_displayed()
        self.driver.find_element_by_id(self.GoogleButton).is_displayed()
        self.driver.find_element_by_css_selector(self.LoginButton).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, self.MyAccountTitle)))
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, self.LogOutButton))).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, self.MyAccountIcon)))


    def SignUp_Email(self):

        self.driver.find_element_by_css_selector(self.EmailCase).send_keys("sebas.viquez@gmail.com")
        self.driver.find_element_by_css_selector(self.EmailSubmitButton).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, self.EmailSubsConfirm)))

