from model.addressbook import Addressbook


def test_delete_first_contact_from_modify_page(adbook_app):
    if adbook_app.addressbook.count() == 0:
        adbook_app.addressbook.add(Addressbook(firstname='Alex', lastname='Subbotin'))
    adbook_app.addressbook.delete_from_modify_page()


def test_del_first_contact(adbook_app):
    if adbook_app.addressbook.count() == 0:
        adbook_app.addressbook.add(Addressbook(firstname='Tom', lastname='Soyer', nickname='cowboy'))
    adbook_app.addressbook.del_one_contact()
