from selenium.webdriver.common.by import By


class AdbookSessionHelper:

    def __init__(self, adbook_app):
        self.adbook_app = adbook_app

    def login(self, username, password):
        wd = self.adbook_app.wd
        self.adbook_app.open_home_page()
        wd.find_element(By.NAME, "user").click()
        wd.find_element(By.NAME, "user").clear()
        wd.find_element(By.NAME, "user").send_keys(username)
        wd.find_element(By.NAME, "pass").click()
        wd.find_element(By.NAME, "pass").clear()
        wd.find_element(By.NAME, "pass").send_keys(password)
        wd.find_element(By.XPATH, "//input[@value='Login']").click()

    def logout(self):
        wd = self.adbook_app.wd
        wd.find_element(By.LINK_TEXT, "Logout").click()