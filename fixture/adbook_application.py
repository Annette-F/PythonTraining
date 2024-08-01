from selenium import webdriver
from fixture.adbook_session import AdbookSessionHelper
from fixture.addressbook import AdbookHelper


class Adbook_application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(60)
        self.adbook_session = AdbookSessionHelper(self)
        self.addressbook = AdbookHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/addressbook/")

    def adbook_destroy(self):
        self.wd.quit()