from selenium.webdriver.common.by import By


class AdbookSessionHelper:

    def __init__(self, adbook_app):
        self.adbook_app = adbook_app

    def login(self, username, password):
        wd = self.adbook_app.wd
        self.adbook_app.open_home_page()
        wd.find_element(By.NAME, 'user').click()
        wd.find_element(By.NAME, 'user').clear()
        wd.find_element(By.NAME, 'user').send_keys(username)
        wd.find_element(By.NAME, 'pass').click()
        wd.find_element(By.NAME, 'pass').clear()
        wd.find_element(By.NAME, 'pass').send_keys(password)
        wd.find_element(By.XPATH, "//input[@value='Login']").click()

    def logout(self):
        wd = self.adbook_app.wd
        wd.find_element(By.LINK_TEXT, 'Logout').click()

    def is_logged_in(self):
        wd = self.adbook_app.wd
        return len(wd.find_elements(By.LINK_TEXT, 'Logout')) > 0

    def is_logged_in_as(self, username):
        wd = self.adbook_app.wd
        return self.get_logged_user() == username

    def get_logged_user(self):
        wd = self.adbook_app.wd
        return wd.find_element(By.XPATH, '//*[@id="top"]/form/b').text[1:-1]

    def ensure_logout(self):
        wd = self.adbook_app.wd
        if self.is_logged_in():
            self.logout()

    def ensure_login(self, username, password):
        wd = self.adbook_app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)
