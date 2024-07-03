# -*- coding: utf-8 -*-
import os

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest
from selenium.webdriver.common.by import By

class TestAddNewContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(60)

    
    def test_add_new_contact(self):
        wd = self.wd
        # open home page
        wd.get("http://localhost/addressbook/addressbook/")
        # login
        wd.find_element(By.NAME, "user").click()
        wd.find_element(By.NAME, "user").clear()
        wd.find_element(By.NAME, "user").send_keys("admin")
        wd.find_element(By.NAME, "pass").click()
        wd.find_element(By.NAME, "pass").clear()
        wd.find_element(By.NAME, "pass").send_keys("secret")
        wd.find_element(By.XPATH, "//input[@value='Login']").click()
        # open add new page
        wd.find_element(By.LINK_TEXT, "add new").click()
        # fill address book entry
        wd.find_element(By.NAME, "firstname").click()
        wd.find_element(By.NAME, "firstname").clear()
        wd.find_element(By.NAME, "firstname").send_keys("Alexander")
        wd.find_element(By.NAME, "middlename").click()
        wd.find_element(By.NAME, "middlename").clear()
        wd.find_element(By.NAME, "middlename").send_keys("Sergeevich")
        wd.find_element(By.NAME, "lastname").click()
        wd.find_element(By.NAME, "lastname").clear()
        wd.find_element(By.NAME, "lastname").send_keys("Pyshkin")
        wd.find_element(By.NAME, "nickname").click()
        wd.find_element(By.NAME, "nickname").clear()
        wd.find_element(By.NAME, "nickname").send_keys("Poet")
        wd.find_element(By.XPATH, "//input[@type='file']").send_keys(os.path.join(os.getcwd(), 'photo.jpg'))
        wd.find_element(By.NAME, "title").click()
        wd.find_element(By.NAME, "title").clear()
        wd.find_element(By.NAME, "title").send_keys("Title")
        wd.find_element(By.NAME, "theform").click()
        wd.find_element(By.NAME, "company").click()
        wd.find_element(By.NAME, "company").clear()
        wd.find_element(By.NAME, "company").send_keys("Company LLC")
        wd.find_element(By.NAME, "address").click()
        wd.find_element(By.NAME, "address").clear()
        wd.find_element(By.NAME, "address").send_keys("Saint-Petersburg")
        wd.find_element(By.NAME, "home").click()
        wd.find_element(By.NAME, "home").clear()
        wd.find_element(By.NAME, "home").send_keys("1234567890")
        wd.find_element(By.NAME, "mobile").click()
        wd.find_element(By.NAME, "mobile").clear()
        wd.find_element(By.NAME, "mobile").send_keys("9876543210")
        wd.find_element(By.NAME, "work").click()
        wd.find_element(By.NAME, "work").clear()
        wd.find_element(By.NAME, "work").send_keys("1472583690")
        wd.find_element(By.NAME, "fax").click()
        wd.find_element(By.NAME, "fax").clear()
        wd.find_element(By.NAME, "fax").send_keys("3692580147")
        wd.find_element(By.NAME, "email").click()
        wd.find_element(By.NAME, "email").clear()
        wd.find_element(By.NAME, "email").send_keys("alex@mal.com")
        wd.find_element(By.NAME, "email2").click()
        wd.find_element(By.NAME, "email2").clear()
        wd.find_element(By.NAME, "email2").send_keys("alex2@mail.com")
        wd.find_element(By.NAME, "email3").click()
        wd.find_element(By.NAME, "email3").clear()
        wd.find_element(By.NAME, "email3").send_keys("alex3@mail.com")
        wd.find_element(By.NAME, "homepage").click()
        wd.find_element(By.NAME, "homepage").clear()
        wd.find_element(By.NAME, "homepage").send_keys("http://www.pyshkin.com")
        wd.find_element(By.NAME, "bday").click()
        Select(wd.find_element(By.NAME, "bday")).select_by_visible_text("17")
        wd.find_element(By.XPATH, "//option[@value='17']").click()
        wd.find_element(By.NAME, "bmonth").click()
        Select(wd.find_element(By.NAME, "bmonth")).select_by_visible_text("November")
        wd.find_element(By.XPATH, "//option[@value='November']").click()
        wd.find_element(By.NAME, "byear").click()
        wd.find_element(By.NAME, "byear").clear()
        wd.find_element(By.NAME, "byear").send_keys("1994")
        wd.find_element(By.NAME, "aday").click()
        Select(wd.find_element(By.NAME, "aday")).select_by_visible_text("20")
        wd.find_element(By.XPATH, "//div[@id='content']/form/select[3]/option[22]").click()
        wd.find_element(By.NAME, "amonth").click()
        Select(wd.find_element(By.NAME, "amonth")).select_by_visible_text("August")
        wd.find_element(By.XPATH, "//div[@id='content']/form/select[4]/option[9]").click()
        wd.find_element(By.NAME, "ayear").click()
        wd.find_element(By.NAME, "ayear").clear()
        wd.find_element(By.NAME, "ayear").send_keys("1999")
        wd.find_element(By.NAME, "address2").click()
        wd.find_element(By.NAME, "address2").clear()
        wd.find_element(By.NAME, "address2").send_keys("Moscow")
        wd.find_element(By.NAME, "phone2").click()
        wd.find_element(By.NAME, "phone2").clear()
        wd.find_element(By.NAME, "phone2").send_keys("my home")
        wd.find_element(By.NAME, "notes").click()
        wd.find_element(By.NAME, "notes").clear()
        wd.find_element(By.NAME, "notes").send_keys("note")
        # enter address book entry
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[21]").click()
        # return home page
        wd.find_element(By.LINK_TEXT, "home page").click()
        # logout
        wd.find_element(By.LINK_TEXT, "Logout").click()
    
    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
