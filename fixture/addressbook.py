from selenium.webdriver.common.by import By

from model.addressbook import Addressbook


class AdbookHelper:

    def __init__(self, adbook_app):
        self.adbook_app = adbook_app

    def open_add_new_page(self):
        wd = self.adbook_app.wd
        if not (wd.current_url.endswith('/edit.php') and len(wd.find_elements(By.NAME, 'submit')) > 0):
            wd.find_element(By.LINK_TEXT, "add new").click()

    def change_field_value(self, field_name, text):
        wd = self.adbook_app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)

    def fill_contact_form(self, addressbook):
        wd = self.adbook_app.wd
        self.change_field_value("firstname", addressbook.firstname)
        self.change_field_value("lastname", addressbook.lastname)
        self.change_field_value("company", addressbook.company)
        self.change_field_value("address", addressbook.address)
        self.change_field_value("home", addressbook.phonehome)
        self.change_field_value("email", addressbook.email)

    def create(self, addressbook):
        wd = self.adbook_app.wd
        self.open_add_new_page()
        self.fill_contact_form(addressbook)
        # enter address book entry
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[21]").click()
        self.return_home_page()
        self.contact_cashe = None

    def open_modification_form_first_contact(self):
        wd = self.adbook_app.wd
        wd.find_element(By.XPATH, "//img[@title='Edit']").click()

    def select_first_contact(self):
        wd = self.adbook_app.wd
        wd.find_element(By.XPATH, "//input[@name='selected[]']").click()

    def delete_first_contact(self):
        wd = self.adbook_app.wd
        self.select_first_contact()
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        wd.find_element(By.LINK_TEXT, "home").click()
        self.contact_cashe = None



    def modify_first_contact(self, new_contact_data):
        wd = self.adbook_app.wd
        self.open_modification_form_first_contact()
        # fill modification form
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element(By.NAME, "update").click()
        self.return_home_page()
        self.contact_cashe = None

    def return_home_page(self):
        wd = self.adbook_app.wd
        wd.find_element(By.LINK_TEXT, "home page").click()

    def count(self):
        wd = self.adbook_app.wd
        return len(wd.find_elements(By.NAME, "selected[]"))

    contact_cashe = None

    def get_contact_list(self):
        if self.contact_cashe is None:
            wd = self.adbook_app.wd
            # self.open_add_new_page()
            self.contact_cashe = []
            for element in wd.find_elements(By.NAME, 'entry'):
                text = element.text
                contact_id = element.find_element(By.NAME, 'selected[]').get_attribute('value')
                self.contact_cashe.append(Addressbook(firstname=text, id=contact_id))
        return list(self.contact_cashe)