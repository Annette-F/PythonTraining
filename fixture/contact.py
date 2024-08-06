from selenium.webdriver.common.by import By
from model.contact import Contact


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

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value('firstname', contact.firstname)
        self.change_field_value('lastname', contact.lastname)
        self.change_field_value('company', contact.company)
        self.change_field_value('address', contact.address)
        self.change_field_value('home', contact.phonehome)
        self.change_field_value('email', contact.email)

    def create(self, contact):
        wd = self.app.wd
        self.open_add_new_page()
        self.fill_contact_form(contact)
        # enter address book entry
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[21]").click()
        self.return_home_page()
        self.contact_cashe = None

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
        self.contact_cashe = None

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.select_contact_by_index(index)
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        wd.find_element(By.LINK_TEXT, 'home').click()
        self.contact_cashe = None

    def edit_first_contact(self):
        wd = self.app.wd
        self.edit_contact_by_index(0)
        self.contact_cashe = None

    def edit_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_edit_form_contact_by_index(index)
        # fill modification form
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element(By.NAME, 'update').click()
        self.return_home_page()
        self.contact_cashe = None

    def return_home_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, 'home page').click()

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements(By.NAME, 'selected[]'))
    contact_cashe = None

    def get_contact_list(self):
        if self.contact_cashe is None:
            wd = self.app.wd
            # self.open_add_new_page()
            self.contact_cashe = []
            for element in wd.find_elements(By.NAME, 'entry'):
                text = element.text
                contact_id = element.find_element(By.NAME, 'selected[]').get_attribute('value')
                self.contact_cashe.append(Contact(firstname=text, id=contact_id))
        return list(self.contact_cashe)



    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_edit_form_contact_by_index(index)
        firstname = wd.find_element(By.NAME, 'firstname').get_attribute('value')
        lastname = wd.find_element(By.NAME, 'lastname').get_attribute('value')
        id = wd.find_element(By.NAME, 'id').get_attribute('value')
        phonehome = wd.find_element(By.NAME, 'home').get_attribute('value')
        return Contact(firstname=firstname, lastname=lastname, id=id, phonehome=phonehome)