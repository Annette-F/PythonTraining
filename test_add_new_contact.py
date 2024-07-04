# -*- coding: utf-8 -*-
import os

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest
from selenium.webdriver.common.by import By
from addressbook import Addressbook
from adbook_application import Adbook_application


class TestAddNewContact(unittest.TestCase):
    def setUp(self):
        self.adbook_app = Adbook_application()

    def test_add_new_contact(self):
        self.adbook_app.login("admin", "secret")
        self.adbook_app.add_address_book_entry(Addressbook("Alexander", "Sergeevich", "Pyshkin", "Poet", "Title", "Company LLC",
                                    "Saint-Petersburg", "1234567890", "9876543210", "1472583690", "3692580147",
                                    "alex@mal.com", "alex2@mail.com", "alex3@mail.com", "http://www.pyshkin.com", "17",
                                    "November", "1994", "20", "August", "1999", "Moscow", "my home", "note"))
        self.adbook_app.logout()



    def tearDown(self):
        self.adbook_app.adbook_destroy()


if __name__ == "__main__":
    unittest.main()