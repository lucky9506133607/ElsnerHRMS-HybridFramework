import time

from selenium.webdriver.common.by import By

class LoginPage:
    # Login Page
    toggle_icon_xpath = "//*[@id='root']/section/aside/div/div[1]/div/i"
    dashboard_xpath = "//*[@id='root']/section/aside/div/div[2]/div/div[1]/ul/li[1]"
    menu_in_out_xpath = "//*[@id='root']/section/aside/div/div[2]/div/div[1]/ul/li[2]"
    Attendance_regularization_xpath = "//*[@id='root']/section/aside/div/div[2]/div/div[1]/ul/li[3]"
    work_from_home_xpath = "//*[@id='root']/section/aside/div/div[2]/div/div[1]/ul/li[4]/div"
    manage_leave_application_xpath = "//*[@id='root']/section/aside/div/div[2]/div/div[1]/ul/li[5]/div"
    user_reports_xpath = "//*[@id='root']/section/aside/div/div[2]/div/div[1]/ul/li[6]"
    organization_policies = "//*[@id='root']/section/aside/div/div[2]/div/div[1]/ul/li[7]"
    tickets = "//*[@id='root']/section/aside/div/div[2]/div/div[1]/ul/li[8]/div"

    def __init__(self,driver):
        self.driver = driver

    def expand_sidebar(self):
        self.driver.find_element(By.XPATH, self.toggle_icon_xpath).click()

    def clickToggle(self, username):
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