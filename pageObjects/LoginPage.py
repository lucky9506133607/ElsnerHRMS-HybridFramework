import time

from selenium.webdriver.common.by import By

class LoginPage:
    # Login Page
    textbox_username_xpath = "//*[@id='basic_email']"
    textbox_password_id = "basic_password"
    button_login_xpath = "//*[@id='basic']/div[5]/div/div/div/div/button"
    link_logout_linktext = "Logout"

    def __init__(self,driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT, self.link_logout_linktext).click()