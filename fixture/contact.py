from selenium.webdriver.common.by import By
from model.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_add_new_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith('/edit.php') and len(wd.find_elements(By.NAME, 'submit')) > 0):
            wd.find_element(By.LINK_TEXT, 'add new').click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)

    contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value('firstname', contact.firstname)
        self.change_field_value('lastname', contact.lastname)
        self.change_field_value('company', contact.company)
        self.change_field_value('address', contact.address)
        self.change_field_value('home', contact.phonehome)
        self.change_field_value('mobile', contact.mobilephone)
        self.change_field_value('work', contact.workphone)
        self.change_field_value('phone2', contact.secondaryphone)
        self.change_field_value('email', contact.email)

    def create(self, contact):
        wd = self.app.wd
        self.open_add_new_page()
        self.fill_contact_form(contact)
        # enter address book entry
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[21]").click()
        self.open_home_page()
        self.contact_cache = None

    def open_edit_form_first_contact(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//img[@title='Edit']").click()

    def open_edit_form_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements(By.XPATH, "//img[@title='Edit']")[index].click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element(By.NAME, 'selected[]').click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements(By.NAME, 'selected[]')[index].click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.delete_contact_by_index(0)
        self.contact_cache = None

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.select_contact_by_index(index)
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        wd.find_element(By.LINK_TEXT, 'home').click()
        self.contact_cache = None

    def edit_first_contact(self):
        wd = self.app.wd
        self.edit_contact_by_index(0)
        self.contact_cache = None

    def edit_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_edit_form_contact_by_index(index)
        # fill modification form
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element(By.NAME, 'update').click()
        self.open_home_page()
        self.contact_cache = None

    def open_home_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, 'home page').click()

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements(By.NAME, 'selected[]'))

    contact_cache = None

    def get_contact_list(self):  # из курса
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for row in wd.find_elements(By.NAME, 'entry'):
                cells = row.find_elements(By.TAG_NAME, 'td')
                firstname = cells[1].text
                lastname = cells[2].text
                id = cells[0].find_element(By.TAG_NAME, 'input').get_attribute('value')
                all_phones = cells[5].text.splitlines()
                phonehome = all_phones[0] if len(all_phones) > 0 else None
                mobilephone = all_phones[1] if len(all_phones) > 1 else None
                workphone = all_phones[2] if len(all_phones) > 2 else None
                secondaryphone = all_phones[3] if len(all_phones) > 3 else None
                self.contact_cache.append(
                    Contact(firstname=firstname, lastname=lastname, id=id, phonehome=phonehome,
                            mobilephone=mobilephone, workphone=workphone, secondaryphone=secondaryphone))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):  # из курса
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements(By.NAME, 'entry')[index]
        cell = row.find_elements(By.TAG_NAME, 'td')[7]
        cell.find_element(By.TAG_NAME, 'a').click()

    def open_contact_view_by_index(self, index):  # из курса
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements(By.NAME, 'entry')[index]
        cell = row.find_elements(By.TAG_NAME, 'td')[6]
        cell.find_element(By.TAG_NAME, 'a').click()

    # def get_contact_list(self):
    #     if self.contact_cache is None:
    #         wd = self.app.wd
    #         # self.open_add_new_page()
    #         self.contact_cache = []
    #         for element in wd.find_elements(By.NAME, 'entry'):
    #             text = element.text
    #             contact_id = element.find_element(By.NAME, 'selected[]').get_attribute('value')
    #             self.contact_cache.append(Contact(firstname=text, id=contact_id))
    #     return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element(By.NAME, 'firstname').get_attribute('value')
        lastname = wd.find_element(By.NAME, 'lastname').get_attribute('value')
        id = wd.find_element(By.NAME, 'id').get_attribute('value')
        phonehome = wd.find_element(By.NAME, 'home').get_attribute('value')
        mobilephone = wd.find_element(By.NAME, 'mobile').get_attribute('value')
        workphone = wd.find_element(By.NAME, 'work').get_attribute('value')
        secondaryphone = wd.find_element(By.NAME, 'phone2').get_attribute('value')
        return Contact(firstname=firstname, lastname=lastname, id=id, phonehome=phonehome, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element(By.ID, 'content').text
        phonehome = re.search('H: (.*)', text).group(1)
        mobilephone = re.search('M: (.*)', text).group(1)
        workphone = re.search('W: (.*)', text).group(1)
        secondaryphone = re.search('P: (.*)', text).group(1)
        return Contact(phonehome=phonehome, mobilephone=mobilephone, workphone=workphone, secondaryphone=secondaryphone)
